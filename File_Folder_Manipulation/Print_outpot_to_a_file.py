import os
import sys

# This will print output to a text file
sys.stdout = open("test.txt", "w")

# Running the aforementioned command and saving its output
output = os.popen('wmic process get description, processid').read()

# Displaying the output
print(output)

sys.stdout.close()
