import cycle
import operators
import os
import format
import functions


def operators_change(string):
    for j in range(len(typesMassPas)):
        if string.find(typesMassPas[j]) != -1:
            string = string.replace(typesMassPas[j], typesMassCpp[j])
            return string


def variables_change(line):
    for mass_element in range(len(typesMassPas)):
        if line.find(typesMassPas[mass_element]) != -1 and \
                        line.find('procedure') == -1 and \
                        line.find('function') == -1:
            line = line.replace(typesMassPas[mass_element], typesMassCpp[mass_element])
            line = line[3:]
            line = line[line.find(typesMassCpp[mass_element]):line.find(';')] + line[:line.find(typesMassCpp[mass_element]) - 1] + ';\n'
    return line


try:
    file_pascal = open('pascalFrom.pas', encoding='utf-8')
    file_cpp = open('cppTo.cpp', 'w', encoding='utf-8')
    if os.stat('pascalFrom.pas').st_size == 0:
        print('Файл пуст')
        exit()
except ValueError:
    exit()
else:
    with file_pascal:
        file_pascal.seek(0)
        file_pas = file_pascal.readlines()
        operatorsPas = ['<>', ' or ', ' and ', ' not', 'mod', 'div']
        operatorsCpp = ['!=', ' || ', ' && ', ' !', '%', '/']
        typesMassPas = ['real', 'integer', 'boolean', 'char', 'string', 'byte']
        typesMassCpp = ['float', 'int', 'bool', 'chr', 'string', 'byte']
        alfarus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
        libDict = {
            '<math.h>': {
                'c++': ['atan',
                        'atof',
                        'ceil',
                        'cos',
                        'exp',
                        'fabs',
                        'floor',
                        'fmod',
                        'sin',
                        'sqrt',
                        'tan'],
                'pascal': ['arctan',
                            'val',
                            'round',
                            'cos',
                            'exp',
                            'abs',
                            'trunc',
                            'frac',
                            'sin',
                            'sqrt',
                            'tan']
            },
            '<limits.h>': {
                'c++': ['MAX_INT',
                        'MIN_INT'
                        ],
                'pascal': ['maxinteger',
                           'mininteger'
                           ]
            }

        }
        t = i = 0
        number = 0
        functionsDict = []
        functionsDict.append('#include <stdio.h>;\n')
        functionsDict.append('#include <stdlib.h>;\n')
        functionsDict.append('#include <iostream>;\n')
        mainDict = []
        flag1 = False
        flag2 = False
        flag3 = False
        while i < len(file_pas):
            file_pas[i] = file_pas[i].lower()
            for key in range(len(libDict['<math.h>']['pascal'])):
                if file_pas[i].find(libDict['<math.h>']['pascal'][key]) != -1:
                    file_pas[i] = file_pas[i].replace(libDict['<math.h>']['pascal'][key], libDict['<math.h>']['c++'][key])
                    flag1 = True
            if file_pas[i].find('string') != -1 or file_pas[i].find('char') != -1:
                flag2 = True
            if file_pas[i].find('write') != -1 or file_pas[i].find('read') != -1:
                for letter in range(len(alfarus)):
                    if file_pas[i].find(alfarus[letter]) != -1:
                        flag3 = True
            if not file_pas[i].find('program') == -1:
                for j in range(i+1, len(file_pas)):
                    file_pas[j] = file_pas[j].lower()
                    if file_pas[j].find('var') != -1:
                        break
                    else:
                        functionsDict.append(file_pas[j])
                    i += 1
            elif not file_pas[i].find('procedure') == -1 or\
                    not file_pas[i].find('function') == -1:
                for j in range(i, len(file_pas)):
                    file_pas[j] = file_pas[j].lower()
                    if file_pas[j] == 'end;\n':
                        functionsDict.append(file_pas[j])
                        break
                    else:
                        if file_pas[j] == 'begin\n':
                            file_pas[j].replace('begin', ' \n')
                        functionsDict.append(file_pas[j])
                    i += 1
            else:
                mainDict.append(file_pas[i])
            i += 1
        if flag1:
            functionsDict.insert(0, '#include <math.h>;\n')
        if flag2:
            functionsDict.insert(0, '#include <string.h>;\n')
        flag = False
        file_pascal.close()
        file_pascal = open('beetween.txt', 'w', encoding='utf-8')
        functionsDict.append('int main()\n')
        functionsDict.append('{\n')
        if flag3:
            functionsDict.append('setlocale(LC_ALL, ".1251");\n')
            functionsDict.append('SetConsoleCP(1251);\n')
        mainDict.remove('begin\n')
        mainDict.remove('end.\n')
        for i in range(len(mainDict)):
            functionsDict.append(mainDict[i])
        functionsDict.append('return 0;\n')
        functionsDict.append('}\n')
        for i in range(len(functionsDict)):
            file_pascal.write(functionsDict[i])
        file_pascal.close()
        file_pascal = open('beetween.txt', encoding='utf-8')
        file_pas = file_pascal.readlines()
        while t < len(file_pas):
            line = file_pas[t].lower()
            if line.find('var') != -1and \
                        line.find('procedure') == -1 and \
                        line.find('function') == -1:
                line = variables_change(line)
                line = line.replace('var', '{\n')
            if line.find('type') != -1:
                line = line[line.find('type') + 4:]
                if line.find('array') != -1:
                    typeOfType = line[line.find('of') + 3:line.find(';')]
                    for j in range(len(typesMassPas)):
                        if typeOfType.find(typesMassPas[j]) != -1:
                            typeOfType = typeOfType.replace(typesMassPas[j], typesMassCpp[j])
                    line = line[:line.find('=array')] + line[line.find('=array') + 6:line.find('of')]
                    typesMassPas.append(line[:line.find('[')].lstrip())
                    typesMassCpp.append(line[:line.find('[')].lstrip())
                    line = 'typedef ' + typeOfType + line + ';\n'
            if line.find('array') != -1:
                line = line[:line.find(':array')] + line[line.find(':array') + 6:line.find('of')] + line[line.find(
                    'of') + 2:]
            for j in range(len(typesMassPas)):
                if line.find(typesMassPas[j]) != -1 and \
                                line.find('procedure') == -1 and \
                                line.find('function') == -1 and \
                                line.find('typedef') == -1:
                    line = line.replace(typesMassPas[j], typesMassCpp[j])
                    line = line[line.find(typesMassCpp[j]):line.find(';')] + line[:line.find(typesMassCpp[j])-1] + ';\n'

            if line.find('=') != -1:
                k = line.find('=')
                if line[k-1] == ':':
                    line = line.replace(':=', '=')
                elif line[k-1] != '>' and line[k-1] != '<':
                    line = line.replace('=', ' == ')
            if line.find('const') != -1:
                line = line[line.find('const ') + 6:]
                line = '#define ' + line[:line.find(' ==')] + ' ' + line[line.find(' ==') + 3:]
            if line.find('for') != -1:
                k = line.find('for')
                line = cycle.cycleFor(line, k)
            if line.find('if') != -1:
                k = line.find('if')
                line = cycle.cycleIf(line, k)
            if line.find('while') != -1:
                k = line.find('while')
                line = cycle.cycleWhile(line, k)
            if line.find('repeat') != -1:
                line = line.replace('repeat', 'do')
            if line.find('until') != -1:
                k = line.find('until')
                line = cycle.cycleUntil(line, k)
            if line.find('begin') != -1:
                k = line.find('begin')
                line = operators.begin(line, k)
            if line.find('end') != -1:
                k = line.find('end')
                line = operators.end(line, k)
            if line.find('write') != -1:
                k = line.find('write')
                line = format.inputName(line, k)
            if line.find('read') != -1:
                k = line.find('read')
                line = format.outputName(line, k)
            if not line.find('procedure') == -1:
                name_of_function = line[line.find('procedure') + 10:line.find('(')]
                variables = line[line.find('('):line.find(')') + 1]
                variables_new = functions.types_change(variables)
                variables_new = operators_change(variables_new)
                variables_new = variables_new.replace(';', ',')
                variables_new = variables_new[:variables_new.rfind(',')]
                line = 'void ' + name_of_function + '(' + variables_new + ')' + '\n' + '{\n'
            if not line.find('function') == -1:
                name_of_function = line[line.find('function') + 9:line.find('(')]
                type_of_function = line[line.rfind(':') + 2:line.rfind(';')]
                type_of_function = operators_change(type_of_function)
                variables = line[line.find('('):line.find(')') + 1]
                variables_new = functions.types_change(variables)
                variables_new = operators_change(variables_new)
                variables_new = variables_new.replace(';', ',')
                variables_new = variables_new[:variables_new.rfind(',')]
                line = type_of_function + ' ' + name_of_function + '(' + variables_new + ')' + '\n' + '{\n'
            for j in range(len(operatorsPas)):
                if line.find(operatorsPas[j]) != -1:
                    line = line.replace(operatorsPas[j], operatorsCpp[j])
            t += 1
            file_cpp.write(line)
        file_cpp.close()
