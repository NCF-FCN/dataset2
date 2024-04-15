import os

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get all files in the current directory
files_in_dir = os.listdir(current_dir)

# Filter out the .png files
png_files = [file for file in files_in_dir if file.endswith(".png")]

# Write the .png file names to a text file
with open("trainlist.txt", "w") as f:
    for file_name in png_files:
        f.write(file_name + "\n")
