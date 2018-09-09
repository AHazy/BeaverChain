# This file creates the blockchain container, adds the genesis block, and links succeeding blocks
from beaverchain_genesis import create_genesis_block
from beaverchain_new_block import *
# Initialize list with genesis block and reference it with prev_block
beaverchain = [create_genesis_block()]
prev_block = beaverchain[0]

# Arbitrary number for now.  Need to change
total_blocks = 20

# Loop to add blocks
for i in range(0, total_blocks):
    block_to_add = new_block(prev_block)
    beaverchain.append(block_to_add)
    prev_block = block_to_add
