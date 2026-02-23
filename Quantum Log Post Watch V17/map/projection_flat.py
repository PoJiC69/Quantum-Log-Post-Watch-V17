"""
Flat Projection Model (V17)
Converts lat/lon into flat earth polar coordinates.
North Pole = center, Antarctica = outer ring.
"""

import math


class FlatProjection:
    def project(self, lat, lon):
        """
        Convert lat/lon to polar coordinates.
        """
        # Normalize
        lat_rad = math.radians(90 - lat)
        lon_rad = math.radians(lon)

        # radius grows toward Antarctica
        radius = lat_rad * 1000

        x = radius * math.cos(lon_rad)
        y = radius * math.sin(lon_rad)

        return x, y
