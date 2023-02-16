#usage: python append_string.py [folder_path] '[tags to be added]'
#example: python append_string.py /content/training_data/ 'hitori_gotoh kita_ikuyo'

import os
import sys

def process_file(file_path, tags):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.strip().replace('_', ' ').replace(' ', ', ')
            f.write(line + ', ' + tags + '\n')

def main():
    folder_path = sys.argv[1]
    tags = sys.argv[2]

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                process_file(file_path, tags)
                print(f'{file} has been updated')

if __name__ == '__main__':
    main()
