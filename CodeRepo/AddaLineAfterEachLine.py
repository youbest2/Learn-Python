# Define a function that takes an input file, an output file, and a line to add as parameters
def add_line_to_file(input_file, output_file, line_to_add):
    # Print a message indicating the input file is being opened
    print(f"Opening input file: {input_file}")
    # Open the input file in read mode and assign it to the variable 'infile'
    with open(input_file, 'r') as infile:
        # Read all lines from the input file and store them in the variable 'lines'
        lines = infile.readlines()

    # Print a message indicating the number of lines read from the input file
    print(f"Read {len(lines)} lines from input file")

    # Print a message indicating the output file is being opened
    print(f"Opening output file: {output_file}")
    # Open the output file in write mode and assign it to the variable 'outfile'
    with open(output_file, 'w') as outfile:
        # Loop through each line in the 'lines' list
        for line in lines:
            # Write the current line to the output file
            outfile.write(line)
            # Write the specified line to add to the output file
            outfile.write(line_to_add + '\n')

    # Print a message indicating the number of lines written to the output file
    print(f"Wrote {len(lines)*2} lines to output file")  # Multiply by 2 to account for the added lines

# Specify the path to the input file and assign it to the variable 'input_file'
input_file = 'D:\\Temp\\PythonExcel\\DOORS_API\\Input.txt'
# Specify the path to the output file and assign it to the variable 'output_file'
output_file = 'D:\\Temp\\PythonExcel\\DOORS_API\\Output.txt'
# Specify the line to add after each line in the input file and assign it to the variable 'line_to_add'
line_to_add = "/* polyspace <RTE:OVFL:Low:Justified> CCB NOT REQ : N/A : No impact, Data is converted as per requirement */"

# Call the 'add_line_to_file' function with the specified input file, output file, and line to add
add_line_to_file(input_file, output_file, line_to_add)
