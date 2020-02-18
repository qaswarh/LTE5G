file_txt = open('ShUDA.txt', 'r')
table = []
for line in file_txt:
    if ':' in line:
        if re.search(str_input, line, re.IGNORECASE):
            key, value = line.split(':', 1)
            tr = [key, value]
            table.append(tr)
    elif '<' in line:
        if re.search(str_input, line, re.IGNORECASE):
            key, value = line, next(file_txt)
            tr = [key, value]
            table.append(tr)

print(tabulate.tabulate(table, tablefmt="fancy_grid")))





