import pprint

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
    print('Invalid file name.')
    quit()

senders = dict()

for line in fhand:
    if len(line) < 2 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    email = words[1]
    senders[email] = senders.get(email, 0) + 1

pprint.pprint(senders)
