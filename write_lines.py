

with open('E.c', 'r') as searchfile:
    for line in searchfile:
        if 'COU_SET(' in line:
            print line

with open('E.c','r+') as myFile:
    for num, line in enumerate(myFile, 1):
        if 'COU_SET(' in line:
            print 'found at line:', num
            print line
            s = line
            a, b = s.split('(', 1)
            c, d = b.split(',', 1)
            e, f = d.split(',', 1)
            result = 'Set ' + c + ' equal to' + e;
            nline = '\n'
            qw = myFile.writelines(nline)
            data = myFile.writelines(result)



# with open('E.c', 'w') as file:
#         # read a list of lines into data
#         data = file.writelines(result)


# # and write everything back
# with open('E.c', 'w') as file:
#     file.writelines(data)
