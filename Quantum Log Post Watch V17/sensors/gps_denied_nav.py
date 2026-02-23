"""
GPS-Denied Navigation (V17)
Dead reckoning using IMU + magnetometer.
"""

from .imu_fusion import IMUFusion
from .magnetometer import Magnetometer


class GPSDeniedNavigator:
    def __init__(self):
        self.imu = IMUFusion()
        self.mag = Magnetometer()
        self.position = {"x": 0.0, "y": 0.0}

    def update(self):
        orientation = self.imu.update()
        heading = self.imu.get_heading()

        # simple dead reckoning step
        step = 1.0
        self.position["x"] += step
        self.position["y"] += step

        return {
            "position": self.position,
            "heading": heading,
            "magnetic": self.mag.read(),
        }
