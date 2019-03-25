print "This will print the line containing the string/word searched in the  file"
print "Below code print the line containing the string/word searched in the  file"

with open('test.c', 'r') as searchfile:
    for line in searchfile:
        if '@ingroup' in line:
            print line

print "End of part 1 -------------------------------------------------------------------"
print "End of part 1 -------------------------------------------------------------------"
#########################################################################################################################################################

print "This will print the line number in which the string/word searched in the  file is found"
print "Below code will print the line number in which the string/word searched in the  file is found"

with open('test.c','r+') as myFile:
    for num, line in enumerate(myFile, 1):
        if '@ingroup' in line:
            print 'found at line:', num
            print line

print "End of part 2 -------------------------------------------------------------------"
print "End of part 2 -------------------------------------------------------------------"
#########################################################################################################################################################

print "This will print the number of lines in the text file"
print "Below code will print the number of lines in the text file"

num_lines = 0
with open('test.c', 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)

print "End of part 3 -------------------------------------------------------------------"
print "End of part 3 -------------------------------------------------------------------"
#########################################################################################################################################################

print "Below code will print the specific line number contents of the text file"
print "Below code will print the specific line number contents of the text file"
with open('test.c','r') as f:
    lines = f.readlines()
    print lines[1]
    print lines[2]
    print lines[3]
print "End of part 4 -------------------------------------------------------------------"
print "End of part 4 -------------------------------------------------------------------"
#########################################################################################################################################################

