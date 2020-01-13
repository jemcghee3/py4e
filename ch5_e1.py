def total(input_set):
    running_total = 0
    for member in input_set:
        running_total = running_total + member
    return running_total

def count(input_set):
    count = 0
    for i in input_set:
        count = count + 1
    return count

def average(input_set):
    mean = total(input_set) / count(input_set)
    return mean

user_set = []
while True:
    print('Enter \"done\" to finish')
    new_data = input('Enter a number: ')
    if new_data == 'done':
        break
    try:
        new_data = int(new_data)
        user_set.append(new_data)
    except:
        print('Invalid input')
        continue

s = total(user_set)
c = count(user_set)
a = average(user_set)

print(str(s) + ' ' + str(c) + ' ' + str(a))
