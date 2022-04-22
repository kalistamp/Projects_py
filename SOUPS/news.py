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
print(f'{RED}{LIT}cstop:{RESET} The Basics ')
print(f'{RED}{LIT}tech:{RESET} Tech related News ')
print(f'{RED}{LIT}Xtras(x):{RESET} All the Extras ')

def Cstop_news():
    choice = input(f'What Section of news would you like to read? \n [Enter Acronym]:     ')
    if choice == 'cstop':
        webbrowser.open_new_tab('https://therecap.org/')
        webbrowser.open_new_tab('https://news.ycombinator.com/')
        webbrowser.open_new_tab('https://www.hackingarticles.in')
        webbrowser.open_new_tab('https://www.ibtimes.com')
        webbrowser.open_new_tab('https://www.theepochtimes.com/')
        webbrowser.open_new_tab('https://www.mintpressnews.com/')
        webbrowser.open_new_tab('https://therecord.media/')
        webbrowser.open_new_tab(' ')
    elif choice == 'tech':
        webbrowser.open_new_tab('https://krebsonsecurity.com/')
        webbrowser.open_new_tab('https://dumpoir.com/v/llllap3xllll')  # He Posts Awesome Repos :)
        webbrowser.open_new_tab('https://securityaffairs.co/wordpress/')
        webbrowser.open_new_tab('https://cybersecurity-magazine.com/')
        webbrowser.open_new_tab('https://www.hackerone.com/vulnerability-and-security-testing-blog')
        webbrowser.open_new_tab('https://telegra.ph/Razvedka-dlya-podgotovki-DDoS-atak-03-05')
        webbrowser.open_new_tab('https://telegra.ph/KORISN%D0%86-POSILANNYA-DLYA-DOPOMOGI-U-DDOS-ATAC%D0%86-02-27')
        webbrowser.open_new_tab('https://www.secjuice.com/tag/osint/')
        webbrowser.open_new_tab('https://www.wonderhowto.com/')
        webbrowser.open_new_tab('https://hakin9.org/blog-2/')
        webbrowser.open_new_tab('https://www.hackingarticles.in')
    elif choice == 'x':
        webbrowser.open_new_tab('http://unlimitedhangout.com/')
        webbrowser.open_new_tab('https://www.thelastamericanvagabond.com/')
        webbrowser.open_new_tab('https://www.investmentwatchblog.com/author/maizipeng/')
        webbrowser.open_new_tab('https://thegradient.pub/')
        webbrowser.open_new_tab('https://www.sciencedaily.com/')
        webbrowser.open_new_tab('https://www.propublica.org/')
        webbrowser.open_new_tab('https://viewdns.info/iphistory/?domain=therecap.org')
    else:
        print('It seems you made a typo, that secrtion does not exist')

Cstop_news()
