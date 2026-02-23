"""
Anomaly Detection Engine (V17)
Detects unusual patterns in sensor & network data.
"""

import statistics


class AnomalyDetector:
    def __init__(self, window_size=10, threshold=2.5):
        self.window_size = window_size
        self.threshold = threshold
        self.history = []

    def update(self, value):
        self.history.append(value)
        if len(self.history) > self.window_size:
            self.history.pop(0)

        if len(self.history) < 5:
            return {"anomaly": False, "z_score": 0}

        mean = statistics.mean(self.history)
        stdev = statistics.stdev(self.history) or 1e-6
        z_score = abs((value - mean) / stdev)

        return {
            "anomaly": z_score > self.threshold,
            "z_score": z_score,
            "mean": mean,
        }
