"""
BMP280 Sensor Interface (V17)
Simulated pressure & temperature sensor.
Replace with real I2C implementation on hardware.
"""

import random

class BMP280:
    def read(self):
        return {
            "temperature_c": round(20 + random.uniform(-5, 5), 2),
            "pressure_hpa": round(1013 + random.uniform(-20, 20), 2),
            "altitude_m": round(100 + random.uniform(-10, 10), 2),
        }
