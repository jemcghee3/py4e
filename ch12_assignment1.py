# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
'''
 Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:', tag.get('class', None))
#    print('Contents:', tag.contents)
#    print('Attrs:', tag.attrs)
    total += int(tag.contents[0])
    count += 1

print('Count %s' % count)
print('Sum %s' % total)
