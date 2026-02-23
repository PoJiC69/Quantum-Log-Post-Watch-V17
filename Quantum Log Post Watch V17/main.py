from core.quantum_core import QuantumCore
from network.terranet_sync import TerraNet
from sensors.gps_denied_nav import Navigator
from ai.anomaly_detection import AnomalyDetector
from map.terra_infinita_renderer import TerraRenderer

def main():
    qc = QuantumCore()
    net = TerraNet()
    nav = Navigator()
    ai = AnomalyDetector()
    renderer = TerraRenderer()

    entropy = qc.generate_entropy()
    position = nav.estimate_position()
    anomaly = ai.detect(entropy)

    net.broadcast(entropy, position, anomaly)
    renderer.render(position)

    print("Log cycle complete")

if __name__ == "__main__":
    main()
