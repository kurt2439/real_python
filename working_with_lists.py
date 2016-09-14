desserts = [ "ice cream", "cookies" ]
print( desserts )
desserts.sort()
print( desserts )
print( desserts.index("ice cream") )
food = desserts[:]
food.extend( [ "broccoli", "turnips" ] )
print( desserts, food )
food.remove("cookies")
print( food[:2] )
breakfast = "cookies, cookies, cookies".split(", ")
print( breakfast )

def between_one_and_twenty( list ):
    for n in list:
        if n >= 1 and n <= 20:
            print(n)

between_one_and_twenty( [2, 4, 8, 16, 32, 64 ] )
