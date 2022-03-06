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

x = ' '

# [ COLOR LEGEND : ]

colorama.init(autoreset=True)
RED = Fore.RED
BLUE = Fore.CYAN
MAG = Fore.MAGENTA
RESET = colorama.Fore.RESET
LIT = Style.BRIGHT

def GHF_logo():
    GHF = f''' {BLUE}{LIT}
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     | F |--.
|--|===|  |'\     .---!~|  .--| I |--|
|  | G |  |.'\    |===| |--|--| N |  |
|  | I |  |\.'\   | H | |__|  | D |  |
|  | T |  | \  \  | U | |==|  | E |  |
|  |   |__|  \.'\ | B |_|__|  | R |__|
|--|===|--|   \.'\|===|~|--|--|~~~|--|
'--'---'--'    `-'`---'-'--'--'---'--' GHF
    '''
    print(GHF)

GHF_logo()
print(x)
print(f'{BLUE}{LIT} By: Kalistamp')
print(x*2)

parser = argparse.ArgumentParser(f'{RED}{LIT} DESCRIPTION: Enter Github Username [   ]  {RESET}')
# Positional arguments ....

parser.add_argument('-g', '--github', help='Enter the USERNAME of Git Account after the \"-g\" switch')

args = parser.parse_args()

if args.github:
    try:        
        username = args.github
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        if response.status_code == 200 and requests.codes.ok:
            data = response.json()
            print(f'{RED}{LIT}Result =  {response}')
            print(x*2)
            print(f"[+] Name : {data['name']}")
            print(f"[+] Id : {data['id']}")
            print(f"[+] Node Id : {data['node_id']}")
            print(f"[+] Gravatar Id : {data['gravatar_id']}")
            print(f"[+] Bio : {data['bio']}")
            print(f"[+] Location : {data['location']}")
            print(f"[+] Email : {data['email']}")
            print(f"[+] Twitter Username : {data['twitter_username']}")
            print(f"[+] Company : {data['company']}")
            print(f"[+] Type : {data['type']}")
            print(f"[+] Blog : {data['blog']}")
            print(f"[+] Followers : {data['followers']}")
            print(f"[+] Following : {data['following']}")
            print(f"[+] Public Gists : {data['public_gists']}")
            print(f"[+] Public Repos : {data['public_repos']}")
            print(f"[+] Created At : {data['created_at']}")
            print(f"[+] Updated At : {data['updated_at']}")
            print(f"[+] Organizations : {data['organizations_url']}")
            print(f"[+] Url : {data['url']}")
            print(f"[+] Html Url : {data['html_url']}")
            print(f"[+] Avatar Url : {data['avatar_url']}")
            print(f"[+] Followers Url : {data['followers_url']}")
            print(f"[+] Following Url : {data['following_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/following")
            print(f"[+] Events Url : {data['events_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/events")
            print(f"[+] Received Events Url : {data['received_events_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/received_events")
            print(f"[+] Gists Url : {data['gists_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/gists")
            print(f"[+] Starred Url : {data['starred_url']} (You Must Copy Like This )--> https://api.github.com/users/{username}/starred")
            print(f"[+] Repos Url : {data['repos_url']}")
            print(f"[+] Subscriptions Url : {data['subscriptions_url']}")
        else:
            print(f'{RED}{LIT}Result =  {response}')
            print(x*2)
            print(f'{RED}{LIT}[!] Invalid USERNAME Given, Try Again...')
    except KeyboardInterrupt:
        print('exit boiii')
