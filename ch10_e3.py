import pprint

ffile = input('Enter a file name: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

letters = dict()

for line in fhandle:
    for word in line:
        for letter in word:
            if letter.isalpha():
                letter = letter.lower()
                letters[letter] = letters.get(letter, 0) + 1

letter_list = list()

for key, value in letters.items():
    letter_list.append((value, key))

letter_list.sort(reverse=True)
pprint.pprint(letter_list)
