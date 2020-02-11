'''
 Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
'''

import json
import urllib.request, urllib.parse, urllib.error

user_url = input('Enter a URL: ')
fhand = urllib.request.urlopen(user_url)

data = fhand.read().decode()

info = json.loads(data)

print('User count: ', len(info['comments']))

count_total = 0
for user in info['comments']:
    count_total = count_total + user['count']

print('Sum: ', count_total) 
