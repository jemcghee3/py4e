def chop(user_list):
    del user_list[0]
    del user_list[-1]

def middle(user_list):
    middle_list = user_list[1:-1]
    return middle_list

things = [1, 5, 'money', 'power']
chop(things)
print(things)


more_things = [8, 'stuff', things, 'spam']
inside_list = middle(more_things)
print('more_things: ' + str(more_things))
print('inside_list: ' + str(inside_list))
