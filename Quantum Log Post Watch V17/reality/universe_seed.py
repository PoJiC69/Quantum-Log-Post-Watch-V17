import random

def generate_universe_seed():
    return random.getrandbits(256)
