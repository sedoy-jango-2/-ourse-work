def inputName(line, k):
    space = line[:k]
    line = line[k:]
    line = line.replace('\u0027', "\u0022")
    if line.find('wrileln') != 1:
        line = 'printf' + line[line.find('writeln')+7:]
    elif line.find('write') != 1:
        line = 'printf' + line[line.find('write')+5:]
    return space + line


def outputName(line, k):
    space = line[:k]
    line = line[k:]
    if line.find('readln') != 1:
        line = 'scanf' + line[line.find('readln')+6:]
    elif line.find('read') != 1:
        line = 'scanf' + line[line.find('read')+4:]
    return space + line