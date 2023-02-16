#usage: python append_string.py [folder_path] '[tags to be added]'
#example: python append_string.py /content/training_data/ 'hitori_gotoh kita_ikuyo'

import os
import sys
import fileinput
import re
import multiprocessing

# Define a regular expression to modify the string format
re_format = re.compile(r"[_!,]")

# Define a worker function to modify the file
def modify_file(file_path, modified_string):
    for line in fileinput.input(file_path, inplace=True):
        print(line.rstrip() + ", " + modified_string)

# Get the directory and appended string from command-line arguments
if len(sys.argv) != 3:
    print("Usage: python append_string.py <directory> <appended_string>")
    sys.exit(1)

directory = sys.argv[1]
appended_string = sys.argv[2]

# Modify the appended string format
modified_string = re_format.sub(lambda m: " " if m.group(0) == "_" else "", appended_string) + ", "

# Create a pool of worker processes
pool = multiprocessing.Pool()

# Loop through all the files in the directory
for file in os.scandir(directory):
    if file.name.endswith(".txt") and file.is_file():
        # Schedule the file for processing by a worker process
        pool.apply_async(modify_file, args=(file.path, modified_string))

# Wait for all worker processes to finish
pool.close()
pool.join()
