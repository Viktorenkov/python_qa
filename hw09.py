# write script that will read "input.txt" file and find there all characters from english alphabet
# collect these characters and their positions in file
# after info collected this info as text write to "output.txt" file in such format
# ####################
# <first found letter> -> pos1
# <next_letter> -> pos2
# <next_letter -> pos3
# etc
# #######################

import re

input_file_path = "/home/user/Documents/Automation QA Hillel/input.txt"
output_file_path = "/home/user/Documents/Automation QA Hillel/output.txt"

def find_alphabet_positions(input_path):
    alphabet_positions = {}
    with open(input_path, 'r') as file:
        text = file.read()
        alphabet_chars = sorted({char for char in text if char.isalpha()})
        for char in alphabet_chars:
            positions = [pos.start() for pos in re.finditer(char, text)]
            alphabet_positions[char] = positions
    return alphabet_positions

def write_positions_to_output(output_path, alphabet_positions):
    with open(output_path, 'w') as file:
        for char, positions in alphabet_positions.items():
            file.write(f"{char} -> {', '.join(map(str, positions))}\n")

# Find alphabet characters and their positions in the input file
alphabet_positions = find_alphabet_positions(input_file_path)

# Write the results to the output file
write_positions_to_output(output_file_path, alphabet_positions)

print("Positions written to output.txt successfully.")