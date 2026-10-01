# file_processor.py

import sys

# Check command-line arguments
if len(sys.argv) != 3:
    print("Usage: python file_processor.py <input_file> <output_file>")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Open and read the input file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count the number of lines
line_count = len(lines)

# Extract the first 2 lines
first_two_lines = lines[:2]

# Write the first 2 lines to a new file
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(first_two_lines)

# Display results
print("Total number of lines:", line_count)
print("First 2 lines extracted successfully.")
print("Output file:", output_file)

