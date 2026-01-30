# ego_vs_soul_power_efficiency.py
from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

# ----------- Model Config -----------
@dataclass
class OneBodyCfg:
    T: float = 180.0      # total time [s]
    dt: float = 0.01      # step [s]
    L: float = 1.0        # inductance
    C: float = 1.0        # capacitance
    R_hi: float = 2.5     # high resistance (ego)
    R_lo: float = 0.005   # near-zero resistance (soul)
    tau_R: float = 60.0   # time constant of R decay (soul)
    V_rated: float = 0.6  # rated voltage amplitude (soul)
    V_ego0: float = 3.0   # ego initial high voltage
    tau_V_ego: float = 20.0 # ego 'fuel' decay
    breath_T: float = 8.0 # breathing period

cfg = OneBodyCfg()

N  = int(cfg.T/cfg.dt) + 1
t  = np.linspace(0, cfg.T, N)

# --- Scenarios ---
# Ego: high V, high R, V decays by fuel burnout
V_ego = cfg.V_ego0*np.exp(-t/cfg.tau_V_ego)*np.sin(2*np.pi*t/cfg.breath_T)
R_ego = cfg.R_hi*(1 + 0.25*np.tanh(2*np.sin(2*np.pi*t/cfg.breath_T)))  # stress coupling

# Soul: rated V, R decays to near zero
V_soul = cfg.V_rated*np.sin(2*np.pi*t/cfg.breath_T)
R_soul = cfg.R_lo + (cfg.R_hi - cfg.R_lo)*np.exp(-t/cfg.tau_R)

# Effortless mode: turn V off after 2/3 time → near-perpetual oscillation
V_off_start = int(0.66*N)
V_soul[V_off_start:] = 0.0

# --- Integrator for L dI/dt + R I + q/C = V ---
def simulate(V, R):
    q = 0.0; I = 0.0
    I_series = np.zeros(N); q_series = np.zeros(N)
    dIdt_series = np.zeros(N)
    P_in = np.zeros(N); P_R = np.zeros(N)
    E_L  = np.zeros(N); E_C = np.zeros(N)
    eta  = np.zeros(N)

    for i in range(N):
        Vi, Ri = float(V[i]), float(max(1e-6, R[i]))

        def deriv(q,I,Vi,Ri):
            dqdt = I
            dIdt = (Vi - Ri*I - q/cfg.C)/cfg.L
            return dqdt, dIdt

        if i < N-1:
            k1q,k1i = deriv(q,I, V[i],R[i])
            k2q,k2i = deriv(q+0.5*k1q*cfg.dt, I+0.5*k1i*cfg.dt, V[i+1],R[i+1])
            k3q,k3i = deriv(q+0.5*k2q*cfg.dt, I+0.5*k2i*cfg.dt, V[i+1],R[i+1])
            k4q,k4i = deriv(q+k3q*cfg.dt,   I+k3i*cfg.dt,   V[i+1],R[i+1])
            q += (k1q+2*k2q+2*k3q+k4q)*(cfg.dt/6)
            I += (k1i+2*k2i+2*k3i+k4i)*(cfg.dt/6)
            dIdt = (k1i+2*k2i+2*k3i+k4i)/6
        else:
            dIdt = 0.0

        I_series[i] = I; q_series[i] = q; dIdt_series[i] = dIdt

        # Powers and energies
        P_in[i] = max(0.0, Vi*I)    # only absorbed power
        P_R[i]  = (I**2)*Ri         # Joule loss
        E_L[i]  = 0.5*cfg.L*(I**2)
        E_C[i]  = 0.5*(q**2)/cfg.C
        denom   = P_in[i] + 1e-9
        useful  = max(0.0, P_in[i]-P_R[i])  # stored/returned portion
        eta[i]  = np.clip(useful/denom, 0.0, 1.0)

    win = int(4.0/cfg.dt)  # 4 s moving average for readability
    def ma(x): return np.convolve(x, np.ones(win)/win, mode="same") if win>1 else x

    return {
        "I": I_series, "q": q_series, "dIdt": dIdt_series,
        "P_in": P_in, "P_R": P_R, "E_L": E_L, "E_C": E_C,
        "eta": eta, "eta_ma": ma(eta),
        "P_in_ma": ma(P_in), "P_R_ma": ma(P_R),
    }

res_ego  = simulate(V_ego,  R_ego)
res_soul = simulate(V_soul, R_soul)

# Cumulative energies
cum_Ein_ego   = np.cumsum(res_ego["P_in"]) * cfg.dt
cum_loss_ego  = np.cumsum(res_ego["P_R"])  * cfg.dt
cum_store_ego = np.cumsum(np.maximum(0.0, res_ego["P_in"]-res_ego["P_R"])) * cfg.dt

cum_Ein_soul   = np.cumsum(res_soul["P_in"]) * cfg.dt
cum_loss_soul  = np.cumsum(res_soul["P_R"])  * cfg.dt
cum_store_soul = np.cumsum(np.maximum(0.0, res_soul["P_in"]-res_soul["P_R"])) * cfg.dt

# ---------- Plot ----------
plt.style.use("seaborn-v0_8")
fig, axes = plt.subplots(4, 2, figsize=(14, 12), sharex=True)

# (1) Waveforms
axes[0,0].plot(t, V_ego, color="#e31a1c", label="Voltage V", alpha=0.9)
axes[0,0].plot(t, res_ego["I"], color="#1f78b4", label="Current I")
axes[0,0].set_title("Ego love: High V & High R → burnout")
axes[0,0].set_ylabel("V / I [PU]"); axes[0,0].legend()

axes[0,1].plot(t, V_soul, color="#e31a1c", label="Voltage V", alpha=0.9)
axes[0,1].plot(t, res_soul["I"], color="#1f78b4", label="Current I")
axes[0,1].axvline(t[V_off_start], ls="--", color="k", alpha=0.5, label="V turned off")
axes[0,1].set_title("Soul love: Rated V, R↓ → near-perpetual current")
axes[0,1].set_ylabel("V / I [PU]"); axes[0,1].legend()

# (2) Resistance & Efficiency
axes[1,0].plot(t, R_ego, color="#33a02c", label="Resistance R")
axes[1,0].plot(t, res_ego["eta_ma"], color="#6a3d9a", label="Efficiency η (MA)")
axes[1,0].set_ylabel("R / η"); axes[1,0].legend()

axes[1,1].plot(t, R_soul, color="#33a02c", label="Resistance R")
axes[1,1].plot(t, res_soul["eta_ma"], color="#6a3d9a", label="Efficiency η (MA)")
axes[1,1].set_ylabel("R / η"); axes[1,1].legend()

# (3) Power balance
axes[2,0].plot(t, res_ego["P_in_ma"], color="#ff7f00", label="Input power V·I (MA)")
axes[2,0].plot(t, res_ego["P_R_ma"],  color="#b15928", label="Joule loss I²R (MA)")
axes[2,0].set_ylabel("Power [PU]"); axes[2,0].legend()

axes[2,1].plot(t, res_soul["P_in_ma"], color="#ff7f00", label="Input power V·I (MA)")
axes[2,1].plot(t, res_soul["P_R_ma"],  color="#b15928", label="Joule loss I²R (MA)")
axes[2,1].set_ylabel("Power [PU]"); axes[2,1].legend()

# (4) Cumulative energy
axes[3,0].plot(t, cum_Ein_ego,   color="#fb9a99", label="Cum. input energy")
axes[3,0].plot(t, cum_loss_ego,  color="#e31a1c", label="Cum. Joule loss")
axes[3,0].plot(t, cum_store_ego, color="#1f78b4", label="Cum. stored/returned")
axes[3,0].set_xlabel("Time [s]"); axes[3,0].set_ylabel("Energy [PU]"); axes[3,0].legend()

axes[3,1].plot(t, cum_Ein_soul,   color="#fb9a99", label="Cum. input energy")
axes[3,1].plot(t, cum_loss_soul,  color="#e31a1c", label="Cum. Joule loss")
axes[3,1].plot(t, cum_store_soul, color="#1f78b4", label="Cum. stored/returned")
axes[3,1].axvline(t[V_off_start], ls="--", color="k", alpha=0.5)
axes[3,1].set_xlabel("Time [s]"); axes[3,1].set_ylabel("Energy [PU]"); axes[3,1].legend()

fig.suptitle("Love-OS: Power vs Efficiency — Ego (left) vs Soul (right)", y=1.02, fontsize=14)
fig.tight_layout()
fig.savefig("ego_vs_soul_power_efficiency.png", dpi=160)
