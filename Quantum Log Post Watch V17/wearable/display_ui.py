"""
Wearable Display UI (V17)
Simple text UI for OLED / LCD displays.
"""

class DisplayUI:
    def render(self, state):
        print("=== TerraNet Wearable ===")
        print(f"Mode    : {state['mode']}")
        print(f"Entropy : {state['entropy']:.2f}")
        print(f"Signal  : {state['signal']}")
        print("=========================\n")
