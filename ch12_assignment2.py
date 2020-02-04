# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
'''
 In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

def loadpage(user_url):
    html = urllib.request.urlopen(user_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def geturl(user_soup):
# Retrieve all of the anchor tags
    global url
    tags = user_soup('a')
    url = tags[position - 1].get('href', None)

for i in range(count):
    soup = loadpage(url)
    geturl(soup)
    print(url)
'''
for tag in tags:
    print(tag.get('href', None))
'''
