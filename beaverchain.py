# This file creates the blockchain container, adds the genesis block, and links succeeding blocks
from beaverchain_genesis import create_genesis_block
from beaverchain_new_block import *

# Initialize list with genesis block and reference it with prev_block
beaverchain = [create_genesis_block()]
prev_block = beaverchain[0]

# Arbitrary number for now.  Need to change
total_blocks = 2
# Variables to hold vote count
total_yes = 0
total_no = 0

# Loop to add blocks
for i in range(0, total_blocks):
    block_to_add = new_block(prev_block)
    beaverchain.append(block_to_add)
    prev_block = block_to_add
    print('This blocks hash is: {}'.format(block_to_add.hash))
    if (block_to_add.vote == 'no') or (block_to_add.vote == 'No') or (block_to_add.vote == 'n') or (block_to_add.vote == 'N'):
        total_no = total_no + 1
    else:
        total_yes = total_yes + 1

# Total votes and print results
total = total_no + total_yes
print('There were a total of {} votes, each on their own immutable block'.format(total))
print('Total Yes Votes: {} Total No Votes: {}'.format(total_yes, total_no))

# Decide winning vote
if total_no > total_yes:
    print('There were more "No" votes than "Yes" votes.')
elif total_yes > total_no:
    print('There were more "Yes" votes than "No" votes.')
else:
    print('The vote resulted in a tie.')

block_view = input('Enter the hash of the block you want to view: ')
for i in range(0, total_blocks):
    if beaverchain[i].hash == block_view:
        print('Block has been found')
        print('Block Vote: {}'.format(beaverchain[i].vote))
