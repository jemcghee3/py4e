numbers = []
while True:
    new_data = input('Enter a number: ')
    if new_data == 'done':
        quit()
    elif not new_data.isdecimal():
        print('Error, please enter a digit or type \'done\' when done.')
        continue
    numbers.append(new_data)

print('Maximum: ' + str(max(numbers)))
print('Minimum: ' + str(min(numbers)))
