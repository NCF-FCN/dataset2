import os

# Define the directory path
dir_path = "C:\\Users\\mattc\\Documents\\GitHub\\dataset2\\data\\RESIDE-Standard\\SOTS\\indoor\\hazy"

# Iterate over all files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a .png image and does not contain "_05" in its name
    if "_5" not in filename:
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)
        # Delete the file
        os.remove(file_path)
