
name = 'by: kalistamp'
x = ' '
print(x)
print(name.title())
print(x*2)

# Required Py Libraries - [ Requirements.txt ]
# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup

URL = input(f'Enter Link to be parsed for all embedded Links:')

# Add an if/else statement to include "https" befpre the url if it is not already included

if ('https' or 'http') in URL:
    page_data = requests.get(URL)
    print(page_data)
else:
    page_data = requests.get('https://' + URL)
    print(page_data)

# By adding "print(page_data)" the output will show a "Response [403]" if the request was successful 

soup_parser = BeautifulSoup(page_data.text, 'html.parser')

links_grabbed = []

# Don't forget the 'href' .... [ "Get all the links from <a> tags with attribute href, and store it in lists variable." ]

for link in soup_parser.find_all('a'):
    links_grabbed.append(link.get('href') + '\n')

with open('kaliscrape.txt', 'a') as done:
    print(*links_grabbed, sep = '\n', file = done )

# When finally printing and saving "done" file, add: sep='\n' to print out everything extracted in clean format

# README.md :
# Steps -
# 1. Save this Python File in a Directory
# 2. Take the URL as an input
# 3. Validate the URL for 'http' and 'https'
# 4. Define an empty array - - ? (WTF Does that mean ..)
# 5. Append the data in that array and save the data in the kaliscrape.txt file



