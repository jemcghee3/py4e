import pprint

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
    print('Invalid file name')
    quit()

domains = dict()

for line in fhand:
    if len(line) < 2 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    email = words[1]
    each_domain = email.split('@')
    domains[each_domain[1]] = domains.get(each_domain[1], 0) + 1

pprint.pprint(domains)
