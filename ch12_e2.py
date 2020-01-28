'''
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
'''


import socket

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
    counter = 0
    while True:
        data = mysock.recv(500)
        counter = counter + len(data)
        if counter >= 3000:
            break
        if len(data) <1:
            break
        print(data.decode(), end='')

    mysock.close
    print(counter)
except:
    failure()



