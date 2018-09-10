~ BeaverChain by Alec Hayden ~
The purpose of this project is to create a transparent and immutable voting platform
for OSU students.  The platform can be altered to be used for any voting application
as it pertains to OSU students.  As an example, the platform is setup to count Yes
or No votes, but it can be changed for anything else such as multiple candidate votes.

Currently, the program creates a Python list that will hold the vote results.  The first
result in the list has an arbitrary value and is not counted in the end vote.  This list
cannot be modified and each vote in the list corresponds with a single block.  The blocks
are connected by referring to the block that came beforehand.  The amount of blocks allowed
on the chain is limited by a specified number that can be changed.  Ideally, this number
will be set to the number of OSU students since that is the number of expected votes.
As votes are entered, the block's hash is returned. This gives the voter a unique string
so they can view their vote in the chain WITHOUT giving any identifying information, such
as their name or ONID.  After the block limit has been reached, the votes are tallied and
the results are displayed.  Then, you can choose to enter a hash to view your vote on it's
personal block.

If I had more time, here are the things I would implement.  At the end of the program, you
can only view one block by giving it's specific hash.  If I had more time, I would've made
this a more robust block explorer with the user being able to reference blocks by time and
vote, as well as representing the blocks in a more visual aspect.  Ideally, the user should
be able to see all blocks comfortably and jump from block to block at will.  The next step
would be to host this program on the web so it can be used across multiple machines instead
of an offline implementation.  Then, I would need to have the Beaverchain constantly running
so that users can connect, vote, and view the blocks whenever they want without interrupting
the chain.

### TO USE BEAVERCHAIN ###
Use the terminal to start up the Beaverchain.
1) cd to beaverchain directory
2) run `python beaverchain.py`
3) enter the votes and view the results!
