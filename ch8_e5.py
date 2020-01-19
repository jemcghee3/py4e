ffile = input('Enter a file name: ')
fhand = open(ffile)

count = 0
for line in fhand:
    if not line.startswith('From') or len(line) < 2 or line.startswith('From:'):
        continue
    count += 1
    words = line.split()
    print(words[1])
print('There were ' + str(count) + ' lines in the file with From as the first word.')
