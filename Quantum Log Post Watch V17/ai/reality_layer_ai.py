"""
Reality Layer AI (V17)
Interprets sensor + map + observer state into perceived reality layer.
"""

class RealityLayerAI:
    def __init__(self):
        self.layers = ["physical", "distortion", "quantum_noise"]

    def evaluate(self, sensor_data, map_data, observer_state):
        distortion = abs(sensor_data.get("magnetic", {}).get("x", 0)) > 40

        active_layer = "physical"
        if distortion:
            active_layer = "distortion"
        elif observer_state.get("entropy", 0) > 0.8:
            active_layer = "quantum_noise"

        return {
            "active_layer": active_layer,
            "confidence": 0.9 if active_layer == "physical" else 0.6,
            "details": {
                "distortion_detected": distortion,
                "observer_entropy": observer_state.get("entropy", 0),
            },
        }
