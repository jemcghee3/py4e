ffile = input('Enter file name: ' )
try:
    fhand = open(ffile)
except:
    print('Invalid file name.')
    quit()

words = dict()
for line in fhand:
    word_list = line.split()
    for k in word_list:
        words[k] = 0

print(words)
