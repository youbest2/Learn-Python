input_file = open('E.c', 'r')
myFile = open('Z.c', 'w')

for lines in range(5000):
    line = input_file.readline()
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
        # qw = myFile.writelines(nline)
        data = myFile.writelines(v1+'\n')
        # qw = myFile.writelines(nline)
    elif 'COU_CALL(EGAP' in line:
        # print 'found at line:', num
        # print line
        result2 = line
        nline2 = '\n'
        data = myFile.writelines('/* run */')
        qw = myFile.writelines(nline2)
        data = myFile.writelines(result2)
        data = myFile.writelines('/* result */'+'\n')
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
        data = myFile.writelines(v11 + '\n')
    elif 'COU_ASSERT_NOT_EQUAL(' in line:
        s11 = line
        z11 = line
        a11, b11 = s11.split('(', 1)
        c11, d11 = b11.split(',', 1)
        e11, f11 = d11.split(',', 1)
        p11, q11 = z11.split('"', 1)
        # print p
        result11 = 'Check whether ' + c11 + ' is equal not to' + e11;
        v111 = p11 + ' "' + result11 + '");'
        # print v1
        nline11 = '\n'
        qw = myFile.writelines(nline11)
        data = myFile.writelines(v111)
    elif '//' in line:
        comments = line
        nline3 = '\n'
        qw = myFile.writelines(nline3)
        data = myFile.writelines('\n' + '\n' + comments)
        data = myFile.writelines('/* precondition */')
        qw = myFile.writelines(nline3)
    # elif '/* run */' or '/* result */' or '/* precondition */' in line:
    #     qw = myFile.writelines('')
    elif not line.strip():
        continue
    else:
        return_extra_lines = line
        data = myFile.writelines(return_extra_lines)
