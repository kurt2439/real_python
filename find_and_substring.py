s = "AAA"
print( s.find("a") )

s2 = "version 2.0"
num = 2.0
print( s2.find( str(num) ) )

text = input( "Enter some characters or strings: " )
target = input( "Enter a string to search for: " )
print( "The first occurance of {} is at: ".format( target ), text.find( target ) )
