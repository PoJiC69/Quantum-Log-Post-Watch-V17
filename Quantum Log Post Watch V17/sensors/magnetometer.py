"""
Magnetometer Interface (V17)
Simulated geomagnetic field readings.
"""

import random

class Magnetometer:
    def read(self):
        return {
            "x": random.uniform(-50, 50),
            "y": random.uniform(-50, 50),
            "z": random.uniform(-50, 50),
        }
