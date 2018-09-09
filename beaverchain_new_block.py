# This file is used to generate and connect all blocks after genesis
from beaverchain_block_class import *
from datetime import datetime
import hashlib

# Function used to create new block and connect to previous
def new_block(prev_block):
    new_index = prev_block.index + 1
    new_timestamp = datetime.now()
    new_hash = prev_block.hash
    new_vote = "Add user input functionality"
    return Block(new_index, new_timestamp, new_vote, new_hash)
