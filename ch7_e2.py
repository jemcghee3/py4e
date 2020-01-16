""" Write a program to prompt for a file name, and then read through the file name and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with 'X-DSPAM-Confidnece:' pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
"""

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
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
