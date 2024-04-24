import os
import shutil

# Define the source and destination directory paths
source_dir_path = "C:\\Users\\mattc\\Documents\\GitHub\\dataset2\\data\\RESIDE-Standard\\SOTS\\outdoor\\hazy"
destination_dir_path = "C:\\Users\\mattc\\Documents\\GitHub\\dataset2\\data\\RESIDE-Standard\\SOTS\\outdoor\\hazy\\temp"

# Iterate over all files in the source directory
for filename in os.listdir(source_dir_path):
    # Split the file name at the first underscore
    parts = filename.split("_", 1)
    # If the file name contains an underscore
    if len(parts) > 1:
        # Change the part of the file name after the first underscore to '5'
        new_filename = parts[0] + "_5.jpg"
        # Copy and rename the file
        shutil.copy(
            os.path.join(source_dir_path, filename),
            os.path.join(destination_dir_path, new_filename),
        )
