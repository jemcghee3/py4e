import pprint

ffile = input('Enter a file name: ')
try:
    fhand = open(ffile)
except:
    print('Invalid file name.')
    quit()

all_senders = dict()
most_messenger = None
most_messages = None

for line in fhand:
    if len(line) < 2 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    emailer = words[1]
    all_senders[emailer] = all_senders.get(emailer, 0) + 1

for key in all_senders:
    if most_messages is None or all_senders[key] > most_messages:
        most_messages = all_senders[key]
        most_messenger = key

print(most_messenger, most_messages)
