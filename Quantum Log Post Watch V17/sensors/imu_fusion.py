"""
IMU Fusion (V17)
Combines accelerometer & gyro into orientation.
"""

import math
import random

class IMUFusion:
    def __init__(self):
        self.orientation = {"roll": 0, "pitch": 0, "yaw": 0}

    def update(self):
        # Simulated drift
        self.orientation["roll"] += random.uniform(-1, 1)
        self.orientation["pitch"] += random.uniform(-1, 1)
        self.orientation["yaw"] += random.uniform(-2, 2)

        return self.orientation

    def get_heading(self):
        return self.orientation["yaw"] % 360
