def find_function_lines(c_file, function_file, output_file):
    with open(c_file, 'r') as f:
        lines = f.readlines()

    print(f"Read {len(lines)} lines from C file.")

    with open(function_file, 'r') as f:
        functions = [line.strip() for line in f.readlines()]

    print(f"Looking for functions: {functions}")

    function_lines = {}
    current_function = None
    for i, line in enumerate(lines):
        if '<< Start of runnable implementation >>' in line:
            print(f"Found start comment at line {i + 1}")
            for j in range(i, min(i + 5, len(lines))):
                for function in functions:
                    if function in lines[j]:
                        current_function = function
                        function_lines[function] = [j + 1]
                        print(f"Found start of function {function} at line {j + 1}")
                        break
                if current_function:
                    break
        elif '<< End of runnable implementation >>' in line and current_function:
            function_lines[current_function].append(i + 1)
            print(f"Found end of function {current_function} at line {i + 1}")
            current_function = None

    print(f"Found functions: {function_lines}")

    with open(output_file, 'w') as f:
        for function, lines in function_lines.items():
            f.write(f'{function} Start - {lines[0]} End - {lines[1]}\n')

# Call the function with your file paths
find_function_lines('D:/Temp/PythonExcel/DOORS_API/DGU.c', 'D:/Temp/PythonExcel/DOORS_API/Input.txt', 'D:/Temp/PythonExcel/DOORS_API/Output.txt')
