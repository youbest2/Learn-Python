with open('E.c', 'r+') as file :
    filedata = file.read()


with open('E.c','r+') as myFile:
    for num, line in enumerate(myFile, 1):
        if 'COU_SET(' in line:
            print 'found at line:', num
            print line
            s = line
            z = line
            a, b = s.split('(', 1)
            c, d = b.split(',', 1)
            e, f = d.split(',', 1)
            result = 'Set ' + c + ' equal to' + e;
            nline = '\n'
            qw = myFile.writelines(nline)
            data = myFile.writelines(result)


Tobo = result + '");'
# Replace the target string
filedata = filedata.replace('");', Tobo)

# Write the file out again
with open('E.c', 'w') as file:
    file.write(filedata)
