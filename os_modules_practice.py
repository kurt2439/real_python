import os
import glob

path = "book1-exercises/chp09/practice_files/images/"
for file in os.listdir( path ):
    print( file )

png_files = os.path.join( path + "*.png" )

for match in glob.glob( png_files ):
    print ( match )

print( "\nNow use os.walk" )

for current_folder, subfolders, file_names in os.walk( path ):
    for file in file_names:
        if file[-4:len(file)].lower() == ".png":
            target_file = os.path.join( current_folder, file )[0:-4] + ".jpg"
            os.rename( os.path.join( current_folder, file), target_file )
            if os.path.exists( target_file ):
                print( "File {} has been converted to JPG".format( target_file ) )
        else:
            print( "File name is {}".format( os.path.join( current_folder, file ) ) )
