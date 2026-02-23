"""
Consensus Engine V17
Ensures state agreement across TerraNet nodes.
"""

import hashlib
import json


class ConsensusEngine:
    def __init__(self):
        self.ledger = []

    def evaluate(self, packet: dict) -> dict:
        """
        Accept state if hash is unique.
        """
        state_hash = self._hash(packet["state"])

        if state_hash not in self.ledger:
            self.ledger.append(state_hash)
            return {"status": "accepted", "hash": state_hash}

        return {"status": "duplicate", "hash": state_hash}

    def _hash(self, state: dict) -> str:
        encoded = json.dumps(state, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()
