def enrollment_stats( university_list ):
    students_enrolled = []
    tuition_paid = []
    
    for university in university_list:
        students_enrolled.append( university[1] )
        tuition_paid.append( university[2] )

    return [students_enrolled, tuition_paid ]

def mean( nums ):
    sum = 0
    for num in nums:
        sum += num
    return sum / len( nums )

def median( nums ):
    nums.sort()
    print("Sorted list:",nums)
    length = len( nums )
    middle = length / 2
    if length % 2 == 0 :
        print("Middle index is",middle)
        return ( nums[middle-1] + nums[middle] ) / 2 
    else:
        return nums[ (int( middle - .5) ) ]

universities = [
        ['CalTech', 2175, 37704],
        ['Harvard',19627,39849],
        ['MIT',10566,40732],
        ['Princeton',7802,37000],
        ['Rice',5879,35551],
        ['Stanford',19535,40569],
        ['Yale',11701,40500]
]

stats = enrollment_stats( universities )
enrollment = stats[0]
tuition = stats[1]

print( mean( enrollment ) ) 
print( median( enrollment ) ) 
print( mean( tuition ) ) 
print( median( tuition ) ) 
