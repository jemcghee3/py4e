import urllib.request

user_url = input('Please enter your desired URL. ')
try:
    fhand = urllib.request.urlopen(user_url)
except:
    print('Invalid URL.')
    quit()

count = 0
for line in fhand:
    line = line.decode()
    for character in line:
        if count < 3000:
            print(character, end='')
            count += 1
print('')
print(count)

