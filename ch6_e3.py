def count(given_string, desired_letter):
    counter = 0
    for each_letter in given_string:
        if each_letter == desired_letter:
            counter = counter + 1
    return counter

print('I search any string and count the times a certain letter appears in the string.')
user_string = input('What string should I search?: ')
user_letter = input('What letter should I search? ')

user_count = count(user_string, user_letter)

print('I found the letter \'' + user_letter + '\' ' + str(user_count) + ' times.')

