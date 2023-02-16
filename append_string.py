#usage: python append_string.py [folder_path] '[tags to be added]'
#example: python append_string.py /content/training_data/ 'hitori_gotoh kita_ikuyo'

import os
import sys

def append_string_to_files(dir_path, appended_string):
    # Split the appended string into separate phrases
    # separated by spaces, then replace underscores with spaces
    # and join the phrases with comma-spaces
    formatted_string = ", ".join([phrase.replace("_", " ") for phrase in appended_string.split()])

    # Walk through the directory, find all the .txt files, and
    # append the formatted string to the end of each file
    for root, _, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path = os.path.join(root, file_name)
                # Use a with statement to ensure the file is closed after writing
                with open(file_path, "a", encoding="utf-8") as file:
                    file.write(", " + formatted_string)

if __name__ == "__main__":
    # Check if the user provided the directory path and appended string as arguments
    if len(sys.argv) == 3:
        # Call the function with the provided directory path and appended string
        append_string_to_files(sys.argv[1], sys.argv[2])
    # Check if the user provided only the appended string as an argument
    elif len(sys.argv) == 2:
        # Call the function with the current directory and the provided appended string
        append_string_to_files(".", sys.argv[1])
    else:
        # If the user did not provide the correct number of arguments, print usage instructions
        print("Usage: python script_name.py [dir_path] appended_string")
