ffile = input('Enter a file name: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

commits = dict()
emails = list()
for line in fhandle:
    if len(line) < 2 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    user = words[1]
    commits[user] = commits.get(user, 0) + 1

for key, val in commits.items():
    emails.append((val, key))

emails.sort(reverse = True)

print(emails[0][1], emails[0][0])
