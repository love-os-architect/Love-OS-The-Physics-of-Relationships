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
