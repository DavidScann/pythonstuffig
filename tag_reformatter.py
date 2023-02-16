# this script was designed to reformat the tags that gallery-dl downloads by default into a format that kohya-trainer likes
# for example: 
# item1
# item2
# item3
# item4
# would be turned into:
# item1, item2, item3, item4
# the reason why this is on here instead of just on the script is because im using this for colab and im too lazy to put everything in so im packing it into a .py file
# ok, have fun (wrote with the help of chatgpt because im a lazy bastard)

# usage: python tag_reformatter.py [path]

import os
import sys

def format_tags(tag_list):
    # Replace underscores with spaces
    tag_list = [tag.replace('_', ' ') for tag in tag_list]

    # Join the items in the list with a comma separator
    return ', '.join(tag_list)

def update_file(file_path):
    # Format the tags
    with open(file_path, 'r') as file:
        items = [line.strip() for line in file]
    output = format_tags(items)

    # Overwrite the file with the output
    with open(file_path, 'w') as file:
        file.write(output)

    # Print a message indicating that the file was updated
    file_name = os.path.basename(file_path)
    print(f"{file_name} has been updated")

# Check if the user provided a folder path as a command line argument
if len(sys.argv) < 2:
    # Print instructions on how to use the script
    print("Please provide a folder path as a command line argument to process .txt and .caption files in the specified folder.")
    print("Usage: python tag_formatter.py /path/to/folder/")
else:
    # Get the folder path from the command line argument
    folder_path = sys.argv[1]

    # Loop through every file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt') or filename.endswith('.caption'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)

            # Update the file and print a message
            update_file(file_path)
