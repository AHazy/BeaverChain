# This file creates the first block in the Beaverchain
from beaverchain_block_class import *
from datetime import datetime

# Function to create block with index 0 and arbitrary previous hash
def create_genesis_block():
    return Block(0, datetime.now(), "NULL", "NULL")
