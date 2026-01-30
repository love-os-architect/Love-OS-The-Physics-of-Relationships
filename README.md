
# Relationship Physics Engine (RPE) 🧲

**A physics-based interaction scoring model for CRM, HR, Matching, and Human Relationships.**

> "Love and relationships are not random. They follow the laws of electromagnetism."

## Overview

Most relationship scoring systems (in dating apps, CRM, or HR) use linear addition:
`Score = Income + Age + Skill`

**This is wrong.** The universe works on **resonance, resistance, and vectors.**

The **Relationship Physics Engine (RPE)** calculates the "Force" between two entities (User & Product, Candidate & Company, or Person A & Person B) using a model isomorphic to **Electromagnetism** and **Ohm's Law**.

It accounts for:
* **Chemistry:** Not just conditions, but resonance ($R \to 0$).
* **Alignment:** High capability with wrong direction creates **Repulsion** (The "Brilliant Jerk" problem).
* **Quantum Locking:** The state where distance no longer reduces connection.

## The Physics Formula

The force $F$ is calculated as:

$$F = k \cdot \frac{P_1 \cdot P_2}{R^n} \cdot A(\Delta \theta) \cdot S(c)$$

Where:
* **$F$ (Force):** The attraction (positive) or repulsion (negative) force.
* **$P$ (Polarity/Potential):** The magnitude of capability, charm, or brand power.
* **$R$ (Resistance/Distance):** The "unresolved information" distance (misunderstandings, lack of trust, time lag). As $R \to 0$, $F \to \infty$.
* **$A(\Delta \theta)$ (Alignment Factor):** calculated via cosine similarity.
    * If aligned ($\Delta \theta \approx 0$): Multiplier is $1.0$.
    * If opposed ($\Delta \theta \approx 180^\circ$): Multiplier is $-1.0$ (Repulsion).
* **$S(c)$ (Selection Gate):** A logistic gate for physiological/instinctive compatibility (Twin-ray filter).

## Use Cases

### 1. HR & Team Building
* **Problem:** A candidate has high skills ($P$) but toxic behavior.
* **RPE Solution:** Their Alignment ($\Delta \theta$) is off. The model returns a **negative Force**, predicting team destruction despite high skills.

### 2. CRM & Sales
* **Problem:** Spamming a customer ($V$) who doesn't trust you yet ($R$ is high).
* **RPE Solution:** $I = V/R$. If $R$ is high, Force is low. The model suggests reducing $R$ (building trust) before increasing $V$ (selling).

### 3. Dating & Matching AI
* **Problem:** "On paper, they match, but there's no spark."
* **RPE Solution:** The Selection Gate $S(c)$ and Resistance $R$ account for non-verbal chemistry, filtering out "boring logic matches."

## Installation

```bash
git clone [https://github.com/your-username/relationship-physics-engine.git](https://github.com/your-username/relationship-physics-engine.git)
cd relationship-physics-engine
from relationship_physics import RelationshipPhysics, Entity

# Define two entities (e.g., Candidate and Company)
# vector: [Vision, WorkEthic, RiskTolerance]
candidate = Entity(potential=0.9, vector=[0.9, 0.8, 0.2])
company   = Entity(potential=1.0, vector=[0.9, 0.9, 0.8])

# Calculate Force
# r_score: Current distance/friction (0.001 = super close/trusting)
# compatibility: Instinctive match (0.0-1.0)
engine = RelationshipPhysics()
result = engine.compute_force(
    entity_a=candidate,
    entity_b=company,
    r_score=0.5, 
    compatibility=0.8
)

print(f"Relationship Force: {result.force:.2f}")
# > Relationship Force: 85.4 (High Attraction)
```
License
MIT License. Based on the Love-OS Philosophy: "Code is the poetry of physics."


# Love-OS: The Physics of Human Connection
**Codename: SHAMBHALA - Relationship Dynamics Module**

[![Project Codename](https://img.shields.io/badge/Codename-SHAMBHALA-purple.svg)]()
[![System State](https://img.shields.io/badge/Status-Experimental-orange.svg)]()
[![Language](https://img.shields.io/badge/Python-3.8%2B-blue.svg)]()

## 1. Abstract: Moving from Drama to Dynamics

Why do relationships run out of energy? Why does "trying hard" often lead to more friction?

Traditional psychology treats love as an emotion. **Love-OS treats love as a vector field governed by energy conservation laws.**
This module provides a mathematical framework to distinguish between **"Soul-Love" (Resonance)** and **"Ego-Love" (Interference)** based on vector dynamics.

We do not judge morality. We calculate **sustainability**.

## 2. The Core Logic

The total output ($Y$) of a relationship is determined by the Energy Amplitude ($L$), the Intent Angle ($\theta$), and the Field Synchronization ($R$).

$$Y_{total} = \frac{1}{R_{\text{sync}}} \left( L_A \cos \theta_A + L_B \cos \theta_B \right)$$

### Key Parameters:

* **$L$ (Love Capacity):**
    * The raw magnitude of life force, resilience, and attention available to give.
* **$\theta$ (Intent Angle):**
    * $0^\circ$: Pure Giving / Flow State.
    * $90^\circ$: Indifference / Disconnection.
    * $180^\circ$: Fear / Attachment / Control (Taking energy).
* **$R_{\text{sync}}$ (Synchronization Factor):**
    * A coefficient derived from trust (low latency) and shared values.
    * **High Sync ($R \to 1.0$):** Superconductivity. Energy is amplified.
    * **Low Sync ($R \to 0.0$):** High Resistance. Energy is lost as heat (conflict).

## 3. Soul-Love vs. Ego-Love

We define the **"Soul Mode Score" ($S_{mode}$)** to classify the relationship state:

$$S_{\text{mode}} = R_{\text{sync}} \times \text{Symmetry} \times \text{Alignment}$$

| Mode | Mathematical Definition | Physical Phenomenon |
| :--- | :--- | :--- |
| **Soul-Love** | $S_{mode} \ge 0.67$ | **Constructive Interference.** <br> The system generates more energy than the sum of its parts (Synergy). |
| **Ego-Love** | $S_{mode} < 0.67$ | **Destructive Interference.** <br> High friction. Energy is consumed to maintain the connection (Codependency). |

## 4. Usage

Run the simulation to diagnose the sustainability of a relationship based on observed parameters.

# The Thermodynamics of Love: Voltage vs. Resistance Efficiency ⚡

**A comparative analysis of Ego-driven relationships vs. Soul-driven connections using RLC Circuit Simulation.**

> "Passion is often just Joule Heating caused by high resistance. True love is Superconductivity."

## 📊 The Simulation Results

The following graph demonstrates the time-domain response of two distinct relationship strategies over the same period ($T=100$).

![Simulation Result: Ego vs Soul Efficiency](./images/simulation_ego_vs_soul_efficiency.png)
*(Fig 1. Left: High Voltage/High Resistance approach. Right: Constant Voltage/Low Resistance approach.)*

## 🔬 Scenario A: Ego Love (The "Burnout" Model)
**Strategy:** Force the connection by increasing effort (Voltage) while ignoring internal blockages (Resistance).

* **Input ($V$):** **High Voltage Spikes.** (Desperate texting, expensive gifts, "trying hard").
* **State ($R$):** **High Resistance.** (Fear of rejection, transactional mindset, ego defense).
* **Physics:** $P = V^2 / R$.
    * High Voltage across High Resistance generates massive **Power ($P$)**.
    * However, this power is not converted into magnetic flow ($I$); it is dissipated as **Joule Heat ($Q$)**.
* **Outcome:**
    * **The "Spark":** The relationship feels intense and "hot" initially due to heat dissipation.
    * **The Crash:** The energy source is quickly depleted. When $V$ drops, the Current ($I$) instantly hits zero.
    * **Efficiency:** Extremely Low. The system is thermodynamically unstable.

## 🔬 Scenario B: Soul Love (The "Superconductor" Model)
**Strategy:** Maintain steady presence (Rated Voltage) and focus entirely on removing internal blockages (Reducing Resistance).

* **Input ($V$):** **Constant / Rated Voltage.** (Trust, consistency, "being" rather than "doing").
* **State ($R$):** **Exponential Decay.** (Healing trauma, letting go of control, vulnerability).
* **Physics:** $I = V / R$.
    * As $R \to 0$, even a small $V$ generates a massive **Current ($I$)**.
    * The system enters a **Superconducting State**.
* **Outcome:**
    * **The "Flow":** Initially quiet, but the flow of love ($I$) grows exponentially as resistance drops.
    * **The Inertia (The Miracle):** At $T=80$ (dotted line), even when the Voltage is turned **OFF**, the current continues to flow.
    * **Perpetual Current:** Because $R \approx 0$ and the Inductance ($L$) stores the energy in the magnetic field, the relationship becomes self-sustaining without external effort.

## 💡 Key Engineering Insights

### 1. The Trap of "Passion"
What we culturally identify as "passion" is often just **friction**. It is the sound of energy trying to force its way through a non-conductive ego. It is unsustainable by design.

### 2. The Irreversibility of Cleansing
In Scenario B, the reduction of Resistance ($R$) represents a permanent structural change (purification). Unlike Voltage, which fluctuates, a cleansed wire does not suddenly become rusty. This explains why Soul connections **do not regress**; once the path is clear, it stays clear.

### 3. Efficiency Over Power
* **Ego:** Maximizes **Power Consumption** (Exhausting).
* **Soul:** Maximizes **Transmission Efficiency** (Effortless).

---
*Generated by the Love-OS Architecture Team.*

```bash
python love_dynamics.py
```

"Stop fixing the emotions. Fix the physics."
---

### File 2: `love_dynamics.py`

```python
import numpy as np

class LoveSystem:
    def __init__(self):
        # System Constants
        self.SOUL_THRESHOLD = 0.67  # Threshold for Phase Transition
        self.ALPHA = 0.5            # Sensitivity to Latency (Friction)

    def calculate_state(self, L_a, L_b, theta_a, theta_b, latency):
        """
        Calculates the relationship state based on vector dynamics.
        
        Args:
            L_a, L_b (float): Energy capacity (0.0 to 10.0)
            theta_a, theta_b (float): Intent Angle in degrees (0=Flow, 180=Fear/Ego)
            latency (float): Communication delay/friction (0.0=Instant Trust, 1.0=High Distrust)
        """
        # Convert degrees to radians
        rad_a = np.radians(theta_a)
        rad_b = np.radians(theta_b)

        # 1. Calculate Field Synchronization (R_sync)
        # Using complex numbers to simulate wave interference
        # If vectors point in the same direction, magnitude increases.
        vector_sum = L_a * np.exp(1j * rad_a) + L_b * np.exp(1j * rad_b)
        magnitude_sum = L_a + L_b + 1e-9 # Avoid zero division

        # R_phase: Pure directional alignment (0.0 to 1.0)
        R_phase = np.abs(vector_sum) / magnitude_sum
        
        # R_sync: Adjusting for "Latency" (Trust/Friction factor)
        # Higher latency exponentially decays synchronization.
        R_sync = R_phase * np.exp(-self.ALPHA * latency)

        # 2. Calculate Effective Output (Y_total)
        # This represents the "Work" done by the relationship.
        # If cos(theta) is negative (Ego), output decreases.
        Y_a = L_a * np.cos(rad_a)
        Y_b = L_b * np.cos(rad_b)
        Y_total = (Y_a + Y_b) * R_sync

        # 3. Calculate Soul Mode Score (S_mode)
        # Symmetry: Are both parties contributing equally?
        symmetry = 1.0 - (abs(L_a - L_b) / magnitude_sum)
        
        # Alignment: Are they looking in the same direction?
        alignment = (1.0 + np.cos(rad_a - rad_b)) / 2.0
        
        S_mode = R_sync * symmetry * alignment

        # 4. Classification
        if S_mode >= self.SOUL_THRESHOLD:
            status = "Soul-Love (State of Flow)"
        else:
            status = "Ego-Love (State of Friction)"

        return {
            "R_sync": round(R_sync, 3),
            "Y_total": round(Y_total, 3),
            "S_mode": round(S_mode, 3),
            "Status": status
        }

# --- Main Execution Block ---

def run_simulation():
    system = LoveSystem()
    print("--- Love-OS Relationship Diagnostic Tool ---\n")

    # Scenario 1: High Energy Ego-Love
    # Both have high energy (8.0), but intentions are misaligned and friction is high.
    print("Case 1: High Energy, High Friction (Ego)")
    result1 = system.calculate_state(
        L_a=8.0, L_b=8.0, 
        theta_a=30, theta_b=-30,  # Slight mismatch
        latency=0.8               # High friction/distrust
    )
    print(f"Input: High Energy (8.0), Latency (0.8)")
    print(f"Output: {result1}\n")

    # Scenario 2: Moderate Energy Soul-Love
    # Lower energy (5.0), but perfect alignment and trust.
    print("Case 2: Moderate Energy, Zero Friction (Soul)")
    result2 = system.calculate_state(
        L_a=5.0, L_b=5.0, 
        theta_a=0, theta_b=0,     # Perfect alignment
        latency=0.05              # Instant trust
    )
    print(f"Input: Moderate Energy (5.0), Latency (0.05)")
    print(f"Output: {result2}\n")

if __name__ == "__main__":
    run_simulation()
