# Write a program to use regular expressions to look for lines of the form:
# New Revision: 39772
# Extract the number from each of the lines, compute the average, and output as integer

import re

ffile = input('Enter file: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

data_set = list()

for line in fhandle:
    line = line.rstrip()
    mo = re.findall('^New Revision: (\d+)', line)
    if len(mo) == 0:
        continue
    mo = float(mo[0])
    data_set.append(mo)

print(int(sum(data_set) / len(data_set)))
