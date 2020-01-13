# This program prompts for a list of numbers and prints out the highest and lowest number.

def highest(user_set):
    highest_so_far = None
    for item in user_set:
        if highest_so_far is None or highest_so_far < item:
            highest_so_far = item
    return highest_so_far

def lowest(user_set):
    lowest_so_far = None
    for item in user_set:
        if lowest_so_far is None or lowest_so_far > item:
            lowest_so_far = item
    return lowest_so_far

data_set = []
while True:
    new_data = input('Enter a number: ')
    if new_data == 'done':
        break
    else:
        try:
            new_data = int(new_data)
            data_set.append(new_data)
        except:
            print('Invalid input')
        
high_number = highest(data_set)
low_number = lowest(data_set)
print(str(high_number) + ' ' + str(low_number))
