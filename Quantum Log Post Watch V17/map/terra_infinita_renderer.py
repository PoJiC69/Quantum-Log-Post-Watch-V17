"""
Terra Infinita Renderer (V17)
Renders flat-projection world with Antarctic ring boundary.
"""

from .projection_flat import FlatProjection
from .antarctic_ring_engine import AntarcticRingEngine


class TerraInfinitaRenderer:
    def __init__(self):
        self.projection = FlatProjection()
        self.ring = AntarcticRingEngine()

    def render_point(self, lat, lon):
        x, y = self.projection.project(lat, lon)
        boundary = self.ring.check_boundary(x, y)

        return {
            "projected": {"x": x, "y": y},
            "inside_ring": boundary["inside"],
            "distance_to_ring": boundary["distance"],
        }

    def render_grid(self, step=30):
        grid = []
        for lat in range(-90, 91, step):
            for lon in range(-180, 181, step):
                grid.append(self.render_point(lat, lon))
        return grid
