ffile = input('Enter a file name: ')
try:
    fhandle = open(ffile)
except:
    print('Invalid file name.')
    quit()

time_of_day = dict()

for line in fhandle:
    if len(line) < 2 or not line.startswith('From') or line.startswith('From:'):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')
    hour = hour[0]
    time_of_day[hour] = time_of_day.get(hour, 0) + 1
# above code splits the line to get the hour, then adds the hour to a dictionary as the key with count as value

results = list(time_of_day.items())
results.sort()
for each_tuple in results:
    print(each_tuple[0], each_tuple[1])
