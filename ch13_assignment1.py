'''
 In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file. 
 '''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    data = data.decode()
    tree = ET.fromstring(data)


    lst_user = tree.findall('comments/comment')
    print('User count:', len(lst_user))
    
    total = 0
    for item in lst_user:
        each_count = item.find('count').text
        print('Count', each_count)
        total = total + int(each_count)

    print(total)
