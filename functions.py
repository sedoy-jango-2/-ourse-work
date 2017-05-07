def types_change(variables):
    for j in range(variables.count(';') + 1):
        if j == 0:
            global_variables_string = variables[variables.find('(') + 1:variables.find(':')]
            global_variables_type = variables[variables.find(':') + 1:variables.find(';')]
            global_variables_mass = []
            if global_variables_string.find(',') == -1:
                global_variables_mass.append(global_variables_string)
            else:
                for t in range(global_variables_string.count(',') + 1):
                    if t < global_variables_string.count(','):
                        global_variables_mass.append(global_variables_string[:global_variables_string.find(',')])
                    else:
                        global_variables_mass.append(global_variables_string[global_variables_string.find(',') + 1:])
            variables_new = ''
            for t in range(len(global_variables_mass)):
                variables_new += global_variables_type + ' ' + global_variables_mass[t] + ','
        else:
            variables = variables[variables.find(';') + 2:]
            global_variables_string = variables[:variables.find(';')]
            global_variables_type = global_variables_string[global_variables_string.find(':') + 1:]
            global_variables_mass = []
            if global_variables_string.find(',') == -1:
                global_variables_mass.append(global_variables_string[:global_variables_string.find(':')])
            else:
                for t in range(global_variables_string.count(',') + 1):
                    if t < global_variables_string.count(','):
                        global_variables_mass.append(global_variables_string[:global_variables_string.find(',')])
                    else:
                        global_variables_mass.append(global_variables_string[global_variables_string.find(',') + 1:])
            for t in range(len(global_variables_mass)):
                variables_new += global_variables_type + ' ' + global_variables_mass[t] + ','
    return variables_new