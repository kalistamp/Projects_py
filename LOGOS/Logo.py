


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
spam = 'by:kalistamp '
print(spam.title())
print(x*2)



def banner():
    version = "1.0"
    ascii_banner = f"""{BLUE}{LIT}
                                                                                                                                                        
  /$$       /$$$$$$ /$$   /$$ /$$   /$$       /$$$$$$$$  /$$   /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$       
| $$      |_  $$_/| $$$ | $$| $$  /$$/      | $$_____//$$$$  | $$$ | $$| $$__  $$ /$$__  $$| $$__  $$      
| $$        | $$  | $$$$| $$| $$ /$$/       | $$     |_  $$  | $$$$| $$| $$  \ $$|__/  \ $$| $$  \ $$      
| $$        | $$  | $$ $$ $$| $$$$$/        | $$$$$    | $$  | $$ $$ $$| $$  | $$   /$$$$$/| $$$$$$$/      
| $$        | $$  | $$  $$$$| $$  $$        | $$__/    | $$  | $$  $$$$| $$  | $$  |___  $$| $$__  $$      
| $$        | $$  | $$\  $$$| $$\  $$       | $$       | $$  | $$\  $$$| $$  | $$ /$$  \ $$| $$  \ $$      
| $$$$$$$$ /$$$$$$| $$ \  $$| $$ \  $$      | $$      /$$$$$$| $$ \  $$| $$$$$$$/|  $$$$$$/| $$  | $$      
|________/|______/|__/  \__/|__/  \__/      |__/     |______/|__/  \__/|_______/  \______/ |__/  |__/      
                                                                                                           
                                                                                                           
    """
    print(ascii_banner)

banner()


print('*******************************************************************')
ppint(x*2)


def HTP_logo():
    HTP = f''' {BLUE}{LIT}
       .--.                   .---.
   .---|__|           .-.     |~~~|
.--|===|--|_          |_|     |~P~|--.
|  |===|  |'\     .---!~|  .--| L |--|
|%%| H |  |.'\    |===| |--|%%| A |  |
|%%| A |  |\.'\   | T | |__|  | N |  |
|  | C |  | \  \  |=H=| |==|  | E |  |
|  | K |__|  \.'\ | E |_|__|  |~T~|__|
|  |===|--|   \.'\|===|~|--|%%|~~~|--|
^--^---'--^    `-'`---^-^--^--^---'--' hjw
    '''
    print(HTP)

HTP_logo()


print('*******************************************************************')
ppint(x*2)




