# Define a function to find the start and end lines of functions in a C file
def find_function_lines(c_file, function_file, output_file):
    # Open the C file and read its contents into a list of lines
    with open(c_file, 'r') as f:
        lines = f.readlines()

    # Print the number of lines read from the C file
    print(f"Read {len(lines)} lines from C file.")

    # Open the function file and read its contents into a list of function names
    with open(function_file, 'r') as f:
        functions = [line.strip() for line in f.readlines()]

    # Print the list of functions to look for in the C file
    print(f"Looking for functions: {functions}")

    # Initialize an empty dictionary to store the start and end lines of each function
    function_lines = {}
    # Initialize a variable to keep track of the current function being processed
    current_function = None

    # Iterate over each line in the C file
    for i, line in enumerate(lines):
        # If the line contains the start comment of a function
        if '<< Start of runnable implementation >>' in line:
            # Print the line number where the start comment was found
            print(f"Found start comment at line {i + 1}")
            # Look for the function name in the next 5 lines
            for j in range(i, min(i + 5, len(lines))):
                # Iterate over each function in the list of functions
                for function in functions:
                    # If the function name is found in the line
                    if function in lines[j]:
                        # Set the current function to the function found
                        current_function = function
                        # Record the line number where the function name was found as the start line of the function
                        function_lines[function] = [j + 1]
                        # Print the function name and its start line
                        print(f"Found start of function {function} at line {j + 1}")
                        # Break out of the loop once the function name is found
                        break
                # If the function name was found, break out of the loop
                if current_function:
                    break
        # If the line contains the end comment of a function and a function is currently being processed
        elif '<< End of runnable implementation >>' in line and current_function:
            # Record the line number where the end comment was found as the end line of the current function
            function_lines[current_function].append(i + 1)
            # Print the function name and its end line
            print(f"Found end of function {current_function} at line {i + 1}")
            # Reset the current function to None since the end of the function has been found
            current_function = None

    # Print the functions found and their start and end lines
    print(f"Found functions: {function_lines}")

    # Open the output file and write the functions and their start and end lines to it
    with open(output_file, 'w') as f:
        for function, lines in function_lines.items():
            f.write(f'{function} Start - {lines[0]} End - {lines[1]}\n')

# Call the function with the paths to your C file, function file, and output file
find_function_lines('D:/Temp/PythonExcel/DOORS_API/DGU.c', 'D:/Temp/PythonExcel/DOORS_API/Input.txt', 'D:/Temp/PythonExcel/DOORS_API/Output.txt')
