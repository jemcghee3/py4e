# This program contains an easter egg.

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
    if ffile == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punk\'d!') # sigh
    else:
        print('Bad file name.')
    quit()

spam = []
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        prefix_length = len('X-DSPAM-Confidence:')
        mo = line[prefix_length:]
        mo = mo.strip()
        mo = float(mo)
        spam.append(mo)

total = 0
count = 0
average = None
for item in spam:
    total = total + item
    count = count + 1
average = total / count

print(average)
