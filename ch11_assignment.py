''' Finding Numbers in a Haystack
This assignment reads through and parses a file with text and numbers.
All the numbers are extracted and the sum is computed.

The data file contains a text with random numbers inserted.

The basic outline of this program is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the xtracted strings to integers and summing up the integers.'''

import re

ffile = input ('Enter file: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

data_set = list()

for line in fhandle:
    line.rstrip()
    mo = re.findall('[0-9]+', line)
    if len(mo) == 0:
        continue
    data_set += mo

for n in range(len(data_set)):
    data_set[n] = int(data_set[n])

print(sum(data_set))
print(len(data_set))
