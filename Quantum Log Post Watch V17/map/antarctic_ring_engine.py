"""
Antarctic Ring Engine (V17)
Defines circular boundary representing Antarctic perimeter
in Terra Infinita flat projection model.
"""

import math


class AntarcticRingEngine:
    def __init__(self, radius=20000):
        self.radius = radius  # arbitrary map units

    def distance_from_center(self, x, y):
        return math.sqrt(x**2 + y**2)

    def check_boundary(self, x, y):
        distance = self.distance_from_center(x, y)
        inside = distance <= self.radius

        return {
            "inside": inside,
            "distance": self.radius - distance,
        }
