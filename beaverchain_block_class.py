# This file outlines the structure of a single block
import hashlib

class Block:
    # Initialize Block
    def __init__(self, index, timestamp, vote, prev_hash):
        self.timestamp = timestamp          # Time block is created
        self.index = index                  # Block index in chain
        self.prev_hash = prev_hash          # Previous block hash
        self.vote = vote                    # Vote data
        self.hash = self.hash_block()       # Calls function to create hash

    # Create hash for block using the index, time, vote info, and previous hash
    def hash_block(self):
        hasher = hashlib.sha256()
        hasher.update((str(self.index) +
                      str(self.timestamp) +
                      str(self.prev_hash) +
                      str(self.vote)).encode())
        return hasher.hexdigest()
