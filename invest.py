def invest( amount, rate, time ):
    total = amount
    print("principle amount: $" + str(total) )
    print("annual rate of return: ", str(rate) )
    for year in range(0,time):
        total = total * rate + total
        print("year {}: ${}".format( year, total ) )
    print() 
    return total

invest(100, .05, 8)
invest(2000, .025, 5)
