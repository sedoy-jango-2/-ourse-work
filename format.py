def inputName(line, k):
    space = line[:k]
    line = line[k:]
    line = line.replace('\u0027', "\u0022")
    line = line.replace(',', '<<')
    if line.find('write(') != -1:
        line = 'cout << ' + line[line.find('write(')+6:line.find(')')] + ' << endl;\n'
    elif line.find('writeln(') != -1:
        line = 'cout << ' + line[line.find('writeln(')+8:line.find(')')] + ' << endl;\n'
    elif line.find('writeln;') != -1:
        line = 'cout <<' + '''\n''' + ';'
    return space + line


def outputName(line, k):
    space = line[:k]
    line = line[k:]
    line = line.replace(',', '>>')
    if line.find('readln(') != -1:
        line = 'cin >> ' + line[line.find('readln(')+6:line.find(')')] + ';\n'
    elif line.find('read(') != -1:
        line = 'cin >> ' + line[line.find('read(')+4:line.find(')')] + ';\n'
    elif line.find('readln;') != -1:
        line = 'cout <<' + '\u0022 \u005C' + '\u006E \u0022' + ';\n'
    return space + line
