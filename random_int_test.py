from random import randint

nums = [0,0,0,0,0,0]

for i in range(0,10000):
    result = randint(0,5)
    nums[result] += 1

for i in ( 0, 1, 2, 3, 4, 5 ):
    odds = nums[i] / 10000
    num = i + 1
    print("percent of rolls for {} is {}".format( num, odds ) )
