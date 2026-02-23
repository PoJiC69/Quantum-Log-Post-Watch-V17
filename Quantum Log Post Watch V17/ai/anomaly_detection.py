class AnomalyDetector:
    def detect(self, entropy):
        return entropy.endswith("00")
