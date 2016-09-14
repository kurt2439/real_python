with open( "election.py", "r" ) as infile, open( "election2.py", "w") as outfile:
    for line in infile.readlines():
        outfile.write( line )

# Unnecessary because with...as does this for us
#infile.close()

outfile = open( "election2.py", "a" )
outfile.write("an additional line\n")
