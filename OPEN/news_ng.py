# Requirements
# pip install colorama
# By: калиштамп

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

x = ' '

def open_news():
    choice = input(f'What Section of news would you like to read? \n [Enter the Letter]: ')
    print(x)
    if choice == 'c':
        websites = [        'https://therecap.org/',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',]
        for url in websites:
            webbrowser.open_new_tab(url)
    elif choice == 't':
        websites = [       'https://krebsonsecurity.com/',
        'https://dumpoir.com/v/llllap3xllll',
        'https://unredactedmagazine.com/',
        'https://www.producthunt.com/',
        'https://securityaffairs.co/wordpress/',
        'https://cybersecurity-magazine.com/',
        'https://www.hackerone.com/,vulnerability-and-security-testing-blog',
        'https://telegra.ph/Razvedka-dlya-podgotovki-DDoS-atak-03-05',
        'https://telegra.ph/KORISN%D0%86-POSILANNYA-DLYA-DOPOMOGI-U-DDOS-ATAC%D0%86-02-27',
        'https://www.secjuice.com/tag/osint/',
        'https://www.wonderhowto.com/',
        'https://hakin9.org/blog-2/',
        'https://www.hackingarticles.in']
        for url in websites:
            webbrowser.open_new_tab(url)
    elif choice == 'x':
        websites = [       'http://unlimitedhangout.com/',
        'https://www.thelastamericanvagabond.com/',
        'https://www.investmentwatchblog.com/author/maizipeng/',
        'https://thegradient.pub/',
        'https://www.sciencedaily.com/',
        'https://www.propublica.org/',
        'https://viewdns.info/iphistory/?domain=therecap.org',]
        for url in websites:
            webbrowser.open_new_tab(url)
    else:
        print(' [!] It seems you made a typo, that section does not exist')

def print_news():
    choice = input(f'What Section of news would you like to read? \n [Enter the Letter]: ')
    print(x)
    if choice == 'c':
        websites = [        'https://therecap.org/',
        'https://www.trickster.dev/',
        'https://news.ycombinator.com/',
        'https://www.reddit.com/r/privacy/',
        'https://www.reddit.com/r/Piracy/',
        'https://www.hackingarticles.in',
        'https://www.ibtimes.com',
        'https://www.theepochtimes.com/',
        'https://www.mintpressnews.com/',
        'https://therecord.media/',]
        for number, links in enumerate(websites):
            print(number, links)
    elif choice == 't':
        websites = [       'https://krebsonsecurity.com/',
        'https://dumpoir.com/v/llllap3xllll',
        'https://unredactedmagazine.com/',
        'https://www.producthunt.com/',
        'https://securityaffairs.co/wordpress/',
        'https://cybersecurity-magazine.com/',
        'https://www.hackerone.com/,vulnerability-and-security-testing-blog',
        'https://telegra.ph/Razvedka-dlya-podgotovki-DDoS-atak-03-05',
        'https://telegra.ph/KORISN%D0%86-POSILANNYA-DLYA-DOPOMOGI-U-DDOS-ATAC%D0%86-02-27',
        'https://www.secjuice.com/tag/osint/',
        'https://www.wonderhowto.com/',
        'https://hakin9.org/blog-2/',
        'https://www.hackingarticles.in']
        for number, links in enumerate(websites):
            print(number, links)
    elif choice == 'x':
        websites = [       'http://unlimitedhangout.com/',
        'https://www.thelastamericanvagabond.com/',
        'https://www.investmentwatchblog.com/author/maizipeng/',
        'https://thegradient.pub/',
        'https://www.sciencedaily.com/',
        'https://www.propublica.org/',
        'https://viewdns.info/iphistory/?domain=therecap.org',]
        for number, links in enumerate(websites):
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
