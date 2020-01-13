def computepay(hours_worked, hourly_rate):
    if hours_worked <= 40:
        pay = hours_worked * hourly_rate
    else:
        pay = ((hours_worked - 40) * hourly_rate * 1.5) + (40 * hourly_rate)
    return pay

while True:
    hours = input('Enter Hours: ')
    try:
        hours = float(hours)
        break
    except:
        print('Please enter a number.')

while True:
    rate = input('Enter Rate: ')
    try:
        rate = float(rate)
        break
    except:
        print('Please enter a number')

pay = computepay(hours, rate)
print('Pay: ' + str(pay))
