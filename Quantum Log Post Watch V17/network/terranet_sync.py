"""
TerraNet Sync V17
Handles multi-node synchronization across the TerraNet.
"""

import time
from .consensus_engine import ConsensusEngine


class TerraNetSync:
    def __init__(self, node_id: str):
        self.node_id = node_id
        self.peers = set()
        self.consensus = ConsensusEngine()

    def register_peer(self, peer_id: str):
        self.peers.add(peer_id)

    def broadcast_state(self, state: dict):
        """
        Simulate broadcasting state to peers.
        """
        packet = {
            "from": self.node_id,
            "timestamp": time.time(),
            "state": state,
        }
        return packet

    def receive_state(self, packet: dict):
        """
        Process incoming state and run consensus.
        """
        return self.consensus.evaluate(packet)
