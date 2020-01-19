ffile = input('Enter file: ')
try:
    fhand = open(ffile)
except:
    print('Bad file name.')

word_list = []
for line in fhand:
    words = line.split()
    for each_word in words:
        if each_word in word_list:
            continue
        word_list.append(each_word)
word_list.sort()
print(word_list)

