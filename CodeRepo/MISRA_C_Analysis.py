# Import necessary libraries
import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import tkinter.messagebox
from idlelib.colorizer import ColorDelegator, color_config


def display_code():
    # Create a new window to display the code
    code_window = tk.Toplevel(root)
    code_window.state('zoomed')  # Maximize the window
    'code_window.geometry("1920x1080")  # Set the size of the window'

    # Create a text widget and add it to the window
    text_widget = tk.Text(code_window)
    text_widget.pack()

    # Set up the colorizer
    delegator = ColorDelegator()
    delegator.setdelegate(text_widget)
    color_config(text_widget)

    # Get the source code of the current file
    with open(__file__, 'r') as f:
        source_code = f.read()

    # Insert the source code into the text widget
    text_widget.insert('end', source_code)

    # Update the display
    text_widget.update_idletasks()


# Add a variable to track whether the "Process Files" button has been clicked
process_files_clicked = False


# Function to handle file selection
def select_file(entry_widget, file_type):
    # Open a file dialog and get the selected file path
    file_path = filedialog.askopenfilename(
        filetypes=[(f"{file_type} files", f"*.{file_type}"), ("All files", "*.*")])
    # If a file path is selected, update the entry widget with the file path
    if file_path:
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)


# Function to open the output file
def open_output_file(output_file):
    # Check if the "Process Files" button has been clicked
    if process_files_clicked:
        # If the output file exists, open it
        if os.path.exists(output_file):
            os.system(f"start {output_file}")
        # If the output file does not exist, print an error message
        else:
            print(f"Output file '{output_file}' not found.")
    # If the "Process Files" button has not been clicked, show an info message box
    else:
        tk.messagebox.showinfo("Info", "Please generate the output file first by clicking on 'Process Files'.")


# Function to find function lines in a C file
def find_function_lines(c_file, function_file, output_file):
    # Open the C file and read all lines into a list
    with open(c_file, 'r') as f:
        lines = f.readlines()

    # Print the number of lines read from the C file
    print(f"Read {len(lines)} lines from C file.")

    # Open the function file and read all lines into a list, stripping trailing whitespaces
    with open(function_file, 'r') as f:
        functions = [line.strip() for line in f.readlines()]

    # Initialize an empty dictionary to store the lines where each function starts and ends
    function_lines = {}
    current_function = None

    # Loop over each line in the C file
    for i, line in enumerate(lines):
        # If the line contains the start comment
        if '<< Start of runnable implementation >>' in line:
            # Look at the next 5 lines or until the end of the file, whichever comes first
            for j in range(i, min(i + 5, len(lines))):
                # For each function we are looking for
                for function in functions:
                    # If the function is in the current line
                    if function in lines[j]:
                        # Set the current function to this function
                        current_function = function

                        # Store the line number where the function starts
                        function_lines[function] = [j + 1]
                        # Break the loop as we found the function
                        break

                # If we found the function, break the loop
                if current_function:
                    break

        # If the line contains the end comment and, we are inside a function
        elif '<< End of runnable implementation >>' in line and current_function:
            # Store the line number where the function ends
            function_lines[current_function].append(i + 1)

            # Reset the current function as we are now outside a function
            current_function = None

    # Print the functions and their start and end lines
    print(f"Found functions: {function_lines}")

    # Open the output file and write the functions and their start and end lines
    with open(output_file, 'w') as f:
        for function, lines in function_lines.items():
            f.write(f'{function} Start - {lines[0]} End - {lines[1]}\n')


# Function to process files
def process_files():
    # Declare the variable as global so we can modify it
    global process_files_clicked
    # Get the file paths from the entry widgets
    c_file = c_entry.get()
    function_file = function_entry.get()
    output_file = output_entry.get()

    # Call the function to find function lines in the C file
    find_function_lines(c_file, function_file, output_file)

    # New code to process the Excel file
    excel_file = excel_entry.get()
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # If the 'Line' column exists in the DataFrame
    if 'Line' in df.columns:
        # Open the output file and read all lines into a list
        with open(output_file, 'r') as f:
            lines = f.readlines()
        # Create a list of ranges where each range is a dictionary with the start and end line numbers
        ranges = [{"start": int(line.split(' Start - ')[1].split(' End - ')[0]), "end": int(line.split(' End - ')[1])}
                  for line in lines]
        # Filter the DataFrame to only include rows where the 'Line' value is within any of the ranges
        filtered_df = df[df['Line'].apply(lambda x: any([x >= r["start"] and x <= r["end"] for r in ranges]))]
        # Write the filtered DataFrame to a new Excel file
        filtered_df.to_excel(os.path.join(os.path.dirname(excel_file), "filtered_new_misra_report.xlsx"), index=False)
    # Set the variable to True after processing the files
    process_files_clicked = True
    # Show a message box when the processing is completed
    tk.messagebox.showinfo("Info", "Processing completed.")


# Create the main application window
root = tk.Tk()
root.title("Function Line Finder")
root.geometry("520x160")  # Set dimensions to 8cm x 6cm (assuming 96 DPI)

# Create widgets
c_label = tk.Label(root, text="C File:")
c_entry = tk.Entry(root, width=50)  # Increase the width to show full path
c_entry.insert(0, "D:/Temp/PythonExcel/DOORS_API/DGU.c")

function_label = tk.Label(root, text="Function File:")
function_entry = tk.Entry(root, width=50)  # Increase the width to show full path
function_entry.insert(0, "D:/Temp/PythonExcel/DOORS_API/Input.txt")

output_label = tk.Label(root, text="Output File:")
output_entry = tk.Entry(root, width=50)  # Increase the width to show full path
output_entry.insert(0, "D:/Temp/PythonExcel/DOORS_API/Output.txt")

# New widgets for the Excel file
excel_label = tk.Label(root, text="Excel File:")
excel_entry = tk.Entry(root, width=50)
excel_entry.insert(0, "D:/Temp/PythonExcel/DOORS_API/new_misra_report.xlsx")

# Create buttons for selecting files and processing files
select_c_button = tk.Button(root, text="Select C File", command=lambda: select_file(c_entry, 'c'))
select_function_button = tk.Button(root, text="Select Function File", command=lambda: select_file(function_entry, 'txt'))
select_excel_button = tk.Button(root, text="Select Excel File", command=lambda: select_file(excel_entry, 'xlsx'))
process_button = tk.Button(root, text="Process Files", command=process_files)
open_output_button = tk.Button(root, text="Open Output File", command=lambda: open_output_file(output_entry.get()))

# Arrange widgets using grid layout
c_label.grid(row=0, column=0, sticky="w")
c_entry.grid(row=0, column=1)
select_c_button.grid(row=0, column=2)

function_label.grid(row=1, column=0, sticky="w")
function_entry.grid(row=1, column=1)
select_function_button.grid(row=1, column=2)

output_label.grid(row=2, column=0, sticky="w")
output_entry.grid(row=2, column=1)
open_output_button.grid(row=2, column=2)

# New grid arrangement for the Excel file
excel_label.grid(row=3, column=0, sticky="w")
excel_entry.grid(row=3, column=1)
select_excel_button.grid(row=3, column=2)

# New widget for opening the output Excel file
open_excel_button = tk.Button(root, text="Open Excel Output File", command=lambda: open_output_file(os.path.join(os.path.dirname(excel_entry.get()), "filtered_new_misra_report.xlsx")))
# Add the new button to the grid
open_excel_button.grid(row=4, column=2)

process_button.grid(row=4, column=1)  # Add the process button

# Create a top-level menu
menubar = tk.Menu(root)

# Create a Help menu
helpmenu = tk.Menu(menubar, tearoff=0)
# Add items to the Help menu
helpmenu.add_command(label="How to Use", command=lambda: tk.messagebox.showinfo("How to Use", "1. Select the C file.\n2. Select the list of Function file separated by new line.\n3. Click 'Process Files' to find function lines.\n4. Click 'Open Output File' to view the results."))
# Add the Help menu to the menu bar
menubar.add_cascade(label="Help", menu=helpmenu)

# Create a Code menu
codemenu = tk.Menu(menubar, tearoff=0)
# Add items to the Code menu
codemenu.add_command(label="Show Source Code", command=display_code)
# Add the Code menu to the menu bar
menubar.add_cascade(label="Code", menu=codemenu)


# Attach the menu bar to the root window
root.config(menu=menubar)

# Start the Tkinter event loop
root.mainloop()
