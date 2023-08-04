"""
open input.txt file and find all small english letters that match such conditions:
target small letter round exactly with three capital english letters on the left and on the right
Match examples:
sdTRYaUVKn  -> matches "a"
NTRSjARTb   -> no match ( not exactly 3 capital letters on the left)
zDFGbOPNq   -> matches "b"
Print Output as : "Result: "<your_found_human_readable_string">
"""

input_file_path = "/home/user/Documents/Automation QA Hillel/input.txt"

def find_matching_letters(input_path):
    result = []
    with open(input_path, 'r') as file:
        text = file.read()
        for i in range(3, len(text) - 3):
            if text[i].islower() and text[i - 3:i].isupper() and text[i + 1:i + 4].isupper():
                result.append(text[i])
    return result

try:
    matching_letters = find_matching_letters(input_file_path)
    if matching_letters:
        result_string = ', '.join(matching_letters)
        print(f"Result: \"{result_string}\"")
    else:
        print("Result: No matches found.")
except FileNotFoundError:
    print("Input file not found.")