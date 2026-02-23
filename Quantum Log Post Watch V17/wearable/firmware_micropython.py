"""
Wearable Firmware (MicroPython) - V17
Handles sensor polling, UI updates, and TerraNet sync triggers.
"""

import time
from display_ui import DisplayUI
from haptic_feedback import HapticFeedback


class WearableFirmware:
    def __init__(self):
        self.display = DisplayUI()
        self.haptics = HapticFeedback()
        self.state = {
            "entropy": 0.0,
            "signal": "OK",
            "mode": "NORMAL",
        }

    def update_state(self, entropy, signal):
        self.state["entropy"] = entropy
        self.state["signal"] = signal

        if entropy > 0.8:
            self.state["mode"] = "ANOMALY"
            self.haptics.alert(pattern="warning")
        else:
            self.state["mode"] = "NORMAL"

    def loop(self):
        while True:
            self.display.render(self.state)
            time.sleep(1)
