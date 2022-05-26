
# TONS OF NEW CHANGES AND UPGRADES TO THIS SCRIPT, CHECK "soup_links_2.py" FOR REFRENCE TO SEE CHANGES

# Argparse: As the name suggests, it parses command line arguments used while launching a Python script or application.
#
# UPDATED THIS LINK FROM "soup_links_2" to accept command line arguments using the Module - "argparse"


spam = 'by: kalistamp'
x = ' '

# Required Py Libraries - [ Requirements.txt ]
# pip install requests
# pip install bs4
# pip install colorama

import requests
import colorama
import argparse
from bs4 import BeautifulSoup
from colorama import Fore
from colorama import Style

# [ COLOR LEGEND : ]

colorama.init(autoreset=True)
RED = Fore.RED
BLUE = Fore.CYAN
MAG = Fore.MAGENTA
RESET = colorama.Fore.RESET
LIT = Style.BRIGHT

# source - http[:]//patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

def banner():
    version = "1.0"
    ascii_banner = f"""{BLUE}{LIT}                                                                                                                                         
         

██╗   ██╗██████╗ ██╗         ███████╗ ██████╗ ██╗   ██╗██████╗ 
██║   ██║██╔══██╗██║         ██╔════╝██╔═══██╗██║   ██║██╔══██╗
██║   ██║██████╔╝██║         ███████╗██║   ██║██║   ██║██████╔╝
██║   ██║██╔══██╗██║         ╚════██║██║   ██║██║   ██║██╔═══╝ 
╚██████╔╝██║  ██║███████╗    ███████║╚██████╔╝╚██████╔╝██║     
 ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                                                          
                                                                                                  

    """
    print(ascii_banner)

banner()

print(RED + LIT + spam.title())     # TITLE PRINTED TWICE - -
print(f'{BLUE}{LIT}{spam.title()}')
print(x*2)

# MUST add format argument "f" before the string if you would like to include a defined variable inside the string, like a color {BLUE}-{RESET}"
# DESCRIPTION, of the Script Below :

parser = argparse.ArgumentParser(description= f"{RED}{LIT} DESCRIPTION: Enter URL to be parsed for all embedded Links [ ]  {RESET} ")

# Unless you add the two dashes before the switches ("-o", "--output") like you did below ...
# ... The arguments being made will be "positional arguments" (required) instead of "optional arguments",,, the arguments below have two switches, so they are going to be optional arguments

parser.add_argument("URL", help=f"{BLUE}{LIT}The URL to extract links from.{RESET}")
# First argument added is going to be a "Positional Argument" (required) 
parser.add_argument("-o", "--output", help= f" {BLUE}{LIT}If you decide to save the output in a file. - [Don't forget to add Directory Path] {RESET}")

# BELOW IS A REMOVED ARGUMENT THAT WAS NEVER USED...
# 
# parser.add_argument('-t', '--test-run', help= f' {BLUE}{LIT}Test a URL too see the return Response (Response[200]=Succcess ){RESET}') 

# "print(page_data)" - - Will show the the Response code for the URL your attempting to parse

args = parser.parse_args()
URL = args.URL

# Add an if/else statement to include "https" before the url if it is not already included in the link provided 

if ('https' or 'http') in URL:
    page_data = requests.get(URL)
    print(page_data)
else:
    page_data = requests.get('https://' + URL)
    print(page_data) # By adding "print(page_data)" the output will show a "Response [200]" if the request was successful

print(x*2)

soup_parser = BeautifulSoup(page_data.text, 'html.parser')

links_grabbed = []

# Don't forget the 'href' .... [ "Get all the links from <a> tags with attribute href, and store it in lists variable." ]

for link in soup_parser.find_all('a'):
    links_grabbed.append(link.get('href') + '\n')
    print(link.get('href')) # Adding "print(link.get('href'))" will display in terminal all links that were grabbed and saved


if args.output:
    with open(f'{URL}_links.txt', 'a') as done:
        print(*links_grabbed, sep = '\n', file = done ) # When finally printing and saving "done" file, add: sep='\n' to print out everything extracted in clean format
    print(x*2)
    print(f'{RED}{LIT}[+] Total Number of links Found: ', len(links_grabbed))
    # By adding "len(links_grabbed)" [Which is the list we set to store to hyperlinks grabbed] , we can display the number of links grabbed as an output
    print(f'{RED}{LIT}[+] Links stored in output TXT file.')

else:
    print(f'{RED}{LIT} NO OUTPUT WAS PRINTED . . . ')

# BELOW IS THE OLD CODE USED BEFORE I CHANGED IT INTO AN IF/ELSE "args" STATEMENT :
#with open(f'{URL}_links.txt', 'a') as done: . . . etc.

print(f'{RED}{LIT}[+] Total Number of links Found: ', len(links_grabbed))
print(x)
print(f'{BLUE}{LIT} Thank you for using Link F1nd3r !')
print(x*2)

# README.md :
# Steps -
# 1. Save this Python File in a Directory
# 2. Take the URL as an input ... or argument in this case 
# 3. Validate the URL for 'http' and 'https'
# 4. Define an empty array as a list (" links_grabbed = [] ")
# 5. Append the data in that array and save the data in the {url}_links.txt file
