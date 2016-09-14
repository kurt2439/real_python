import csv
import os

path = r"book1-exercises/chp09/practice_files/"
csv_file = os.path.join( path, "scores.csv" )
scores = {} 

with open( csv_file, "r" ) as csv_in_fh:
    csv_in = csv.reader( csv_in_fh )
    next( csv_in )
    for row in csv_in:
        print( "Row is", row )
        if row[0] in scores:
            print( "New Row:", row[1] )
            print( "Old Row:", scores[ row[0] ] )
            if row[1] > scores[ row[0] ]:
                print( "New row greater" )
                scores[ row[0] ] = row[1]
        else:
            scores[ row[0] ] = row[1]

for key in sorted( scores ):
    print("{} {}".format( key, scores[ key ] ) )
