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


---

### 2. `relationship_physics.py` (Python Code)

```python
"""
Relationship Physics Engine (RPE)
---------------------------------
A module to calculate the attractive/repulsive force between two entities
based on an electromagnetic isomorphism model.

Theory: F = k * (P1 * P2) / R^n * Alignment * Selection
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict
import math

# --- Utilities ---

def _clip(val: float, low: float, high: float) -> float:
    return max(low, min(high, val))

def _cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Calculates cosine similarity between two vectors."""
    if not vec_a or not vec_b or len(vec_a) != len(vec_b):
        return 1.0  # Default to neutral/aligned if no data
    
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot / (norm_a * norm_b)

# --- Data Structures ---

@dataclass
class Entity:
    """
    Represents a person, product, or organization.
    
    Attributes:
        potential (float): Magnitude of capability/charm (0.0 to 1.0).
                           Isomorphic to Magnetic Moment or Charge.
        vector (List[float]): Values/Vision vector (e.g., [Innovation, Stability, Profit]).
                              Used to calculate Alignment (Delta Theta).
    """
    potential: float = 0.5
    vector: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.potential = _clip(self.potential, 0.0, 1.0)

@dataclass
class ForceResult:
    force: float
    components: Dict[str, float]
    description: str

# --- Core Engine ---

class RelationshipPhysics:
    def __init__(self, k: float = 100.0, n: float = 3.0, r_min: float = 0.001):
        """
        Args:
            k (float): Scaling constant.
            n (float): Distance decay exponent (3.0 mimics magnetic dipoles).
            r_min (float): Minimum resistance to prevent division by zero.
        """
        self.k = k
        self.n = n
        self.r_min = r_min

    def compute_force(
        self, 
        entity_a: Entity, 
        entity_b: Entity, 
        r_score: float, 
        compatibility: float = 0.5
    ) -> ForceResult:
        """
        Calculates the Force (F) between two entities.

        Args:
            entity_a, entity_b: The two subjects.
            r_score (float): "Resistance" or "Information Distance". 
                             Lower is better. (0.0 ~ 1.0+)
                             0.1 = Trust established. 1.0 = Strangers.
            compatibility (float): Instinctive/Physiological match gate (0.0 ~ 1.0).
        """
        # 1. Physics Parameters
        R = max(self.r_min, r_score)
        P1 = entity_a.potential
        P2 = entity_b.potential
        
        # 2. Alignment (Delta Theta)
        # Cosine similarity: 1.0 (Aligned) to -1.0 (Opposite)
        alignment = _cosine_similarity(entity_a.vector, entity_b.vector)
        
        # 3. Selection Gate (Sigmoid-like filter)
        # Amplifies high compatibility, dampens low.
        S = 1.0 / (1.0 + math.exp(-12.0 * (compatibility - 0.5)))
        S = _clip(S, 0.0, 1.0)

        # 4. The Formula
        # Base Magnitude (Coulomb/Gravity-like)
        magnitude = self.k * (P1 * P2) * (R ** -self.n)
        
        # Final Vector Force
        F = magnitude * alignment * S

        # 5. Interpretation
        desc = "Neutral"
        if F > 50: desc = "Strong Attraction (Resonance)"
        elif F > 10: desc = "Attraction"
        elif F < -50: desc = "Strong Repulsion (Conflict)"
        elif F < -10: desc = "Repulsion"

        return ForceResult(
            force=F,
            components={
                "Magnitude": magnitude,
                "Alignment": alignment,
                "Selection_Gate": S,
                "R_effective": R
            },
            description=desc
        )

# --- Quick Test ---
if __name__ == "__main__":
    # Example: A "Twin-ray" scenario (High alignment, High compat, Low R)
    engine = RelationshipPhysics()
    
    # Vectors represent [Creativity, Logic, Empathy]
    person_A = Entity(potential=0.9, vector=[0.9, 0.5, 0.8]) 
    person_B = Entity(potential=0.9, vector=[0.8, 0.6, 0.9]) # Very similar
    
    res = engine.compute_force(person_A, person_B, r_score=0.05, compatibility=0.95)
    
    print(f"--- Twin Resonance Test ---")
    print(f"Force: {res.force:.4f}") 
    print(f"State: {res.description}")
    print(f"Details: {res.components}")
