# A simple program to simulate the operation of the grep command.
# Ask the user to enter a regular epression and counnt the number of lines that matched the regular expression.

import re

ffile = input('Enter a file name: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

expression = input('Enter a regular expression: ')
counter = 0
for line in fhandle:
    line = line.rstrip()
    mo = re.findall(expression, line)
    if len(mo) == 0:
        continue
    counter += 1

print(str(ffile) + ' had ' + str(counter) + ' lines that matched ' + expression)
