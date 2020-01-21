import pprint

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
    print('Invalid file name.')
    quit()

days = dict()

for line in fhand:
    if len(line) < 3 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    dow = words[2]
    days[dow] = days.get(dow, 0) + 1

pprint.pprint(days)
