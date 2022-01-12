# SOURCE (MEDIUM): https[:]//faun.pub/check-all-the-links-of-a-given-website-using-python-4dd1c0015315
#
# PROJECT RECAP: This project is about fetching all the links to a given website
# Tip: Best to Practice inside a Virtual_Machine

spam = 'by: kalistamp'
x = ' '
print(x)
print(spam.title())
print(x * 2)

# Required Py Libraries - [ Requirements.txt ]
# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup

url = input(f' Enter Link:  ')
if ('https' or 'http') in url:
    data = requests.get(url)
else:
    data = requests.get('https://' + url)

# What is "href" ? [ Possible Conclusions ]:
# 1. An absolute URL; points to another web site (like href="http://www.example.com/theme.css")
# 2. A relative URL; points to a file within a web site (like href="/themes/theme.css")
#
# Source Labeled "soup_parser" as "soup" ...

soup_parser = BeautifulSoup(data.text, 'html.parser')
links = []
for link in soup_parser.find_all('a'):
    links.append(link.get('href'))

with open('KaliScrape.txt', 'a') as saved:
    print(links, file = saved)


# README.md :
# Steps -
# 1. Save this Python File in a Directory
# 2. Take the URL as an input
# 3. Validate the URL for 'http' and 'https'
# 4. Define an empty array - - ? (WTF Does that mean ..)
# 5. Append the data in that array and save the data in the kaliscrape.txt file
