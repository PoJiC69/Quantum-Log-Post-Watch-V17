"""
Satellite Relay V17
Simulates long-range TerraNet relay.
"""

import time


class SatelliteRelay:
    def __init__(self, satellite_id="TERRANET-ORBITAL-1"):
        self.satellite_id = satellite_id

    def uplink(self, packet: dict) -> dict:
        time.sleep(0.5)
        return {
            "satellite": self.satellite_id,
            "direction": "uplink",
            "packet": packet,
        }

    def downlink(self, packet: dict) -> dict:
        time.sleep(0.5)
        return {
            "satellite": self.satellite_id,
            "direction": "downlink",
            "packet": packet,
        }
