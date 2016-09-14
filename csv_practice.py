import os
import csv

path = r"book1-exercises/chp09/practice_files/"

with open( os.path.join( path, "pastimes.csv" ), "r" ) as infile, open( os.path.join( path, "categorized_pastimes.csv"), "w" ) as outfile:
    csv_in = csv.reader( infile )
    csv_out = csv.writer( outfile )
    next( csv_in )
    csv_out.writerow( [ "Name", "Favorite Pastime", "Type of Pastime" ] )
    for row in csv_in:
        pastime = row[1].lower()
        print( "Pastime is", pastime )
        index = pastime.find( 'fight' )
        print ( "Index is", index )
        if row[1].lower().find( "fighting" ) != -1:
            row.append( "Combat" )
        else: 
            row.append( "Other" )
        print( row )
        csv_out.writerow( row )
