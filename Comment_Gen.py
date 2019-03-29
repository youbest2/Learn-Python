with open('E.c', 'r') as searchfile:
    for line in searchfile:
        if 'COU_SET(' in line:
            print line

with open('E.c','r+') as myFile:
    for num, line in enumerate(myFile, 1):
        if 'COU_SET(' in line:
            # print 'found at line:', num
            # print num
            s = line
            z = line
            a, b = s.split('(', 1)
            c, d = b.split(',', 1)
            e, f = d.split(',', 1)
            p, q = z.split('"', 1)
            # print p
            result = 'Set ' + c + ' equal to' + e;
            v1 = p + ' "' + result + '");'
            # print v1
            nline = '\n'
            qw = myFile.writelines(nline)
            data = myFile.writelines(v1)
        elif  'COU_CALL(' in line:
            # print 'found at line:', num
            # print line
            result2 = line
            nline2 = '\n'
            qw = myFile.writelines(nline2)
            data = myFile.writelines(result2)
        elif 'COU_ASSERT_EQUAL(' in line:
            s1 = line
            z1 = line
            a1, b1 = s1.split('(', 1)
            c1, d1 = b1.split(',', 1)
            e1, f1 = d1.split(',', 1)
            p1, q1 = z1.split('"', 1)
            # print p
            result1 = 'Check whether ' + c1 + ' is equal to' + e1;
            v11 = p1 + ' "' + result1 + '");'
            # print v1
            nline1 = '\n'
            qw = myFile.writelines(nline1)
            data = myFile.writelines(v11)
        else:
            return_extra_lines = line
            data = myFile.writelines(return_extra_lines)
