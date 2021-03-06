'''
Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
'''

import socket, re

def failure():
    print('Doo doo doo! We\'re sorry. The url  you have entered is out of service or has been disconnected. Please check the url and try again. Doo doo doo!')
    quit()

user_url = input('Please enter the URL you wish to retrieve: ')
if not user_url.startswith('http://') and not user_url.startswith('https://'): # this handles urls without the http:// to properly format them
    url_fixer = ['http://']
    url_fixer.append(user_url)
    user_url = url_fixer[0] + url_fixer[1]
# Debug   print(user_url)
domain = user_url.split('/')
domain = domain[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((domain, 80))
except:
   failure()
try:
    cmd = 'GET ' + str(user_url) + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)
except:
    failure()

while True:
    data = mysock.recv(512)
    if len(data) <1:
        break
    data = data.decode()# decode the data first to play with it
    header = data.split(r'\n\n\n')
    print(header[0])

mysock.close
