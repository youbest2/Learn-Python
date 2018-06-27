#### Pyinstaller can be used to generate a single executable file from a python project.   
STEP 1 :   
Install Pyinstaller   
https://www.pyinstaller.org/downloads.html   
https://github.com/pyinstaller/pyinstaller/zipball/develop   

STEP 2 :   
Extract the file in python installed directory (C:\Python27\)   
Remane the extracted folder to : pyinstaller   
STEP 3 :   
Now open command prompt in Python directory and    
use command : cd pyinstaller   
(To create exe)   
use command : python pyinstaller.py your_python_file.py   
(To create single exe)   
use command : python pyinstaller.py --onefile --windowed your_python_file.py   
(your_python_file.py : it should be placed in C:\Python27\pyinstaller\ )   

Output Folde : C:\Python27\pyinstaller\main\dist   
