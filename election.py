from random import random

cand_a = 0 
cand_b = 0

num_trials = 10000

for trial in range(0,num_trials):
    a = 0
    b = 0
    if random() <= .87:
        a += 1
    else:
        b += 1
    if random() <= .65:
        a += 1
    else:
        b += 1
    if random() <= .17:
        a += 1
    else:
        b += 1

    if a >= 2:
        cand_a += 1
    else:
        cand_b += 1

cand_a_chance = cand_a / num_trials
cand_b_chance = cand_b / num_trials

print("Candidate A has a {}% chance of winning".format( cand_a_chance ) )
print("Candidate B has a {}% chance of winning".format( cand_b_chance ) )
