# Requirements
# pip install colorama
# By: Kalistamp

import webbrowser
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

print(f'{RED}{LIT}Table of Contents:')
print(f'{RED}cstop:{RESET} The Basics ')

def Cstop_news():
    choice = input(f'What Section of news would you like to read today? \n [Enter Acronym]:     ')
    if choice == 'cstop':
        webbrowser.open_new_tab('https://therecap.org/')
        webbrowser.open_new_tab('https://news.ycombinator.com/')
        webbrowser.open_new_tab('https://www.hackingarticles.in')
        webbrowser.open_new_tab('https://www.ibtimes.com')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
    elif choice == 'Tech':
        webbrowser.open_new_tab('https://krebsonsecurity.com/')
        webbrowser.open_new_tab('https://dumpoir.com/v/llllap3xllll')  # He Posts Awesome Repos :)
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab('https://hakin9.org/blog-2/')
        webbrowser.open_new_tab('https://www.hackingarticles.in')
        webbrowser.open_new_tab('https://www.ibtimes.com')
    elif choice == 'Xtras':
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')
    else:
        print('It seems you made a typo, that secrtion does not exist')

Cstop_news()
