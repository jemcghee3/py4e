while True:
    hours = input('Enter Hours: ') 
    try:
        hours = float(hours)
        break
    except:
        print('Error, please enter numeric input')
while True:
    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
        break
    except:
        print('Error, please enter numeric input')


if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5
print('Pay: ' + str(pay))
