import tkinter as tk                 # import the tkinter library and rename it as tk
from tkinter import filedialog       # import the filedialog module from tkinter library
import xlsxwriter                   # import the xlsxwriter library
from xlsxwriter.utility import xl_rowcol_to_cell
def on_exit():                      # define a function on_exit
    root.destroy()                  # destroy the root window

def create_excel():                # define a function create_excel
    AB_text = AB_input.get()        # get the text entered in the AB_input field and store it in AB_text
    BH_text = BH_input.get()        # get the text entered in the BH_input field and store it in BH_text
    GH_text = GH_input.get()        # get the text entered in the GH_input field and store it in GH_text
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx') # open a filedialog to save the excel file, with default extension .xlsx
    workbook = xlsxwriter.Workbook(file_path)   # create a new workbook using the file path
    worksheet = workbook.add_worksheet()         # add a worksheet to the workbook
    worksheet.write('A1', 'AB')                  # write "AB" in cell A1
    worksheet.write('A2', AB_text)               # write the AB_text in cell A2
    worksheet.write('B1', 'BH')                  # write "BH" in cell B1
    worksheet.write('B2', BH_text)               # write the BH_text in cell B2
    worksheet.write('C1', 'GH')                  # write "GH" in cell C1
    worksheet.write('C2', GH_text)               # write the GH_text in cell C2
    workbook.close()                             # close the workbook
    tk.Label(root, text='Excel Created').pack()   # show a label in the root window that says "Excel Created"

root = tk.Tk()                                   # create a Tkinter window and assign it to root
root.geometry("700x200")
root.title("Inputs Window")                      # set the title of the root window as "Inputs Window"


AB_label = tk.Label(root, text="AB: ")           # create a label and put it in the root window
AB_label.place(x=20, y=20)
AB_input = tk.Entry(root)                        # create an entry field and put it in the root window
AB_input.place(x=50, y=20, width=600)

BH_label = tk.Label(root, text="BH: ")           # create a label and put it in the root window
BH_label.place(x=20, y=50)
BH_input = tk.Entry(root)                        # create an entry field and put it in the root window
BH_input.place(x=50, y=50, width=600)

GH_label = tk.Label(root, text="GH: ")           # create a label and put it in the root window
GH_label.place(x=20, y=80)
GH_input = tk.Entry(root)                        # create an entry field and put it in the root window
GH_input.place(x=50, y=80, width=600)


exit_button = tk.Button(root, text="Exit", command=on_exit)  # create a button named "Exit" and associate on_exit function to it
exit_button.place(x=20, y=160)

excel_button = tk.Button(root, text="Create Excel", command=create_excel) # create a button named "Create Excel" and associate create_excel function to it
excel_button.place(x=60, y=160)


root.mainloop()                                  # start the main event loop to display the window
