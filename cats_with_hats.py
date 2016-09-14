array = [ 0 for i in range(101) ]
start_pos = 1
while start_pos <= 100:
    for i in range(1,101):
        if i % start_pos == 0:
            if array[i] == False:
                array[i] = True
            else:
                array[i] = False
    start_pos += 1


for i in range (1,101):
    if array[i] is True:
        print("i is {} and value is {}".format( i, array[i] ) )
