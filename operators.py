def begin(line, k):
    line = line[:k] + '{\n'
    return line

def end(line, k):
    line = line[:k] + '}\n'
    return line