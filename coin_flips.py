from random import randint

trials = 10000
flips = 0

for trial in range(0,trials):
    result = randint(0,1)
    flips += 1
    while True:
        new_try = randint(0,1)
        flips += 1
        if new_try == result:
            break

avg_flips = flips / trials
print("The average number of flips to get both heads and tails was:", str(avg_flips) )
