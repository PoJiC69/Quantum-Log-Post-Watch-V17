"""
Observer State V17
Represents the observer in the simulation.
"""

import random


class ObserverState:
    def __init__(self):
        self.state = {
            "exists": True,
            "observing": True,
            "coherence": 1.0,
            "entropy_signature": None,
        }

    def update(self, entropy: str):
        """Update observer state from entropy."""
        self.state["entropy_signature"] = entropy
        self.state["coherence"] *= random.uniform(0.95, 1.0)

        if self.state["coherence"] < 0.5:
            self.state["exists"] = False
