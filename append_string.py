#usage: python append_string.py [folder_path] '[tags to be added]'
#example: python append_string.py /content/training_data/ 'hitori_gotoh kita_ikuyo'

import os
import sys

def format_tags(tag_list):
    # Replace underscores with spaces
    tag_list = [tag.replace('_', ' ') for tag in tag_list]

    # Join the items in the list with a comma separator
    return ', '.join(tag_list)

# Check if the user provided a folder path as a command line argument
if len(sys.argv) < 3:
    # Print instructions on how to use the script
    print("Please provide a folder path and a string to append, separated by a space.")
    print("Usage: python append_string.py /path/to/folder/ 'tags'")
else:
    # Get the folder path and string to append from the command line arguments
    folder_path = sys.argv[1]
    append_string = sys.argv[2].replace('_', ', ')

    # Loop through every file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)

            # Open the file
            with open(file_path, 'r') as file:
                # Read the contents of the file into a list
                items = [line.strip() for line in file]

            # Format the tags
            output = format_tags(items)

            # Append the string to the output
            output += ', ' + append_string

            # Overwrite the file with the output
            with open(file_path, 'w') as file:
                file.write(output)
