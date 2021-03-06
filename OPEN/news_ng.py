# Requirements
# pip install colorama
# By: калиштамп

import webbrowser
import time
import colorama
from colorama import Fore
from colorama import Style

# [ COLOR LEGEND : ]

colorama.init(autoreset=True)
RED = Fore.RED
BLUE = Fore.CYAN
MAG = Fore.MAGENTA
RESET = colorama.Fore.RESET
LIT = Style.BRIGHT

x = ' '
print(x*2)

cstop = [        'https://therecap.org/',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',]

tech = [       'https://krebsonsecurity.com/',
        'https://dumpoir.com/v/llllap3xllll',
        'https://www.producthunt.com/',
        'https://securityaffairs.co/wordpress/',
        'https://cybersecurity-magazine.com/',
        'https://www.hackerone.com/,vulnerability-and-security-testing-blog',
        'https://telegra.ph/Razvedka-dlya-podgotovki-DDoS-atak-03-05',
        'https://telegra.ph/KORISN%D0%86-POSILANNYA-DLYA-DOPO[        ',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',
        'https://hakin9.org/blog-2/',
        'https://www.hackingarticles.in' ]

xtras = [       'http://unlimitedhangout.com/',
        'https://www.thelastamericanvagabond.com/',
         'https://heystacks.com/hall-of-fame', 
        'https://www.investmentwatchblog.com/author/maizipeng/',
        'https://thegradient.pub/',
        'https://www.sciencedaily.com/',
        'https://www.propublica.org/',
        'https://viewdns.info/iphistory/?domain=therecap.org',]

KITCHEN_TABLE = cstop + tech + xtras 

def open_news():
    choice = input(f'What Section of news would you like to read? \n [Enter the Letter]: ')
    print(x)
    if choice == 'c':
        for url in cstop:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 't':
        for url in tech:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    elif choice == 'x':
        for url in xtras:
            time.sleep(2)
            webbrowser.open_new_tab(url)
    else:
        print(' [!] It seems you made a typo, that section does not exist')

def print_news():
    choice = input(f'What Section of news would you like to read? \n [Enter the Letter or type "all" for everything ...]: ')
    print(x)
    if choice == 'c':
        for number, links in enumerate(cstop):
            print(number, links)
    elif choice == 't':
        for number, links in enumerate(tech):
            print(number, links)
    elif choice == 'x':
        for number, links in enumerate(xtras):
            print(number, links)
    elif choice == 'all':
        for number, links in enumerate(KITCHEN_TABLE):
            print(number, links)
    else:
        print(' [!] It seems you made a typo, that section does not exist')



which = input(f'Would you like to \"open\" or \"view\" News Sections? :    ')

print(x*2)
print(f'{RED}{LIT}TABLE OF CONTENTS:')
print(f'{RED}{LIT}cstop(c):{RESET} The Basics ')
print(f'{RED}{LIT}tech(t):{RESET} Tech related News ')
print(f'{RED}{LIT}Xtras(x):{RESET} All the Extras ')

if which == 'open':
    open_news()
elif which == 'view':
    print_news()
else:
    print(f' {RED}{LIT} [!] It seems you made a typo - that option does not exist')
