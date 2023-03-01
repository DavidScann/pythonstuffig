#usage: python prepend_string.py [folder_path] '[tags to be added]'
#example: python prepend_string.py /content/training_data/ 'hitori_gotoh kita_ikuyo'

import os
import sys

def prepend_string_to_files(dir_path, prepended_string):
    # Split the prepended string into separate phrases
    # separated by spaces, then replace underscores with spaces
    # and join the phrases with comma-spaces
    formatted_string = ", ".join([phrase.replace("_", " ") for phrase in prepended_string.split()])

    # Walk through the directory, find all the .txt files, and
    # prepend the formatted string to the beginning of each file
    for root, _, files in os.walk(dir_path):
        for file_name in files:
            if file_name.endswith(".txt"):
                file_path = os.path.join(root, file_name)
                # Read the contents of the file and store it in a variable
                with open(file_path, "r", encoding="utf-8") as file:
                    file_contents = file.read()
                # Write the formatted string and file contents back to the file
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(formatted_string + ", " + file_contents)

if __name__ == "__main__":
    # Check if the user provided the directory path and prepended string as arguments
    if len(sys.argv) == 3:
        # Call the function with the provided directory path and prepended string
        prepend_string_to_files(sys.argv[1], sys.argv[2])
    # Check if the user provided only the prepended string as an argument
    elif len(sys.argv) == 2:
        # Call the function with the current directory and the provided prepended string
        prepend_string_to_files(".", sys.argv[1])
    else:
        # If the user did not provide the correct number of arguments, print usage instructions
        print("Usage: python prepend_string.py [dir_path] prepended_string")
