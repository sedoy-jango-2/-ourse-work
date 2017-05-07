def cycleFor(line, k):
    counter = line[k + 4:line.find('=')]
    source = line[:k]
    line = line[line.find('for ') + 4:]
    counterFrom = line[line.find('=') + 1:line.find(' ')]
    if line.find('downto') != -1:
        line = line[line.find('downto ') + 7:]
        counterTo = line[:line.find(' do')]
        line = (
        'for (' + counter + '=' + counterFrom + ';' + counter + '>' + counterTo + ';' + counter + '--' + ')' + '\n')
    else:
        counterTo = line[line.find('to ') + 3:line.find(' do')]
        line = (
        'for (' + counter + '=' + counterFrom + ';' + counter + '<' + counterTo + ';' + counter + '++' + ')' + '\n')
    return source + line


def cycleWhile(line, k):
    source = line[:k]
    line = 'while(' + line[line.find('while') + 5:line.find('do')] + ')\n'
    return source + line


def cycleIf(line, k):
    source = line[:k]
    line = 'if (' + line[line.find('if') + 2:line.find('then')] + ')\n'
    return source + line
