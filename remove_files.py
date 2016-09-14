import os
path = r"book1-exercises/chp09/practice_files/little pics/"

for current_folder, subfolders, files in os.walk( path ):
    for file in files:
        file_path = os.path.join( current_folder, file )
        # Match files no matter the ending case
        if file_path.lower().endswith( ".jpg" ):
            if os.path.getsize( file_path ) < 2000:
                print( "Remove small file", file_path )
                # os.remove( file_path )
