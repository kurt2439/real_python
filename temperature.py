def c_to_f( celc ):
    return float(celc) * 9/5 + 32

def f_to_c( far ):
    return ( float(far) - 32 ) * 5/9

c = input("Input Celcius: ")
print( "Fahrenheit:",c_to_f( c ) )

f = input("Input Fahrenheit: ")
print( "Celcius:",f_to_c( f ) )
