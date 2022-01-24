
# SOURCES :
# https[:]//github.com/techwithtim/ColoredTextInPython
# https[:]//pypi.org/project/colorama/

# Colorama Ledger: 
# Fore = Foreground Color
# Back = Background Color (Highlight for the text)
# Style = Just the style
# - - - -
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


# How To Print Colored Text in Python

# Required Py Libraries - [ Requirements.txt ]
# pip install colorama

import colorama

from colorama import Fore, Back, Style
colorama.init() # This step is required to initialize all the added classes above (Fore,Back,Style)

x = ' '
print(x*2)
print('\033[31m' + 'By: Kalistamp') # By inputting:  "\033[31m" it will change the text to Red
# Regardless if the next print is not on the same string it will still be Red until you input the code to change it back 
print('This text is also going to be RED ... ')
print('\033[31m') # By changing the "31m" to "I'm" you have changed the text back to original color 

#
# AN EASIER STYLE OF PRINTING THE STRING IN COLOR WOULD BE TO USE FORE INSTEAD OF THE EXACT COLORAMA CODE EACH TIME
#
# EXAMPLE BELOW:
# 
# Another option instead of autoreset every time: "print(Fore.RESET)"
colorama.init(autoreset=True) # By adding "autoreset=True" inside the init -
# It will automatically reset the text color every time we print a new line of text 
#
#
print(Fore.RED + 'By: Kalistamp')

print('Now This text should not be RED Anymore')
print(x*3)
print(x*3)
print(x*3)

print() # Below Each letter has been changed too a different color ...
print(f"{Fore.RED}C{Fore.GREEN}O{Fore.YELLOW}L{Fore.BLUE}O{Fore.MAGENTA}R{Fore.CYAN}S{Fore.WHITE}!")
print(f"{Fore.RED}Red Text")
print(f"{Fore.GREEN}Green Text")
print(f"{Fore.YELLOW}Yellow Text")
print(f"{Fore.BLUE}Blue Text")
print(f"{Fore.MAGENTA}Magenta Text")
print(f"{Fore.CYAN}Cyan Text")
print(f"{Fore.WHITE}White Text")
print()
print(f"{Back.RED}B{Back.GREEN}A{Back.YELLOW}C{Back.BLUE}K{Back.MAGENTA}G{Back.CYAN}R{Back.WHITE}O{Back.RED}U{Back.GREEN}N{Back.YELLOW}D{Back.BLUE}!")
print(f"{Back.RED}Red Background")
print(f"{Back.GREEN}Green Background")
print(f"{Back.YELLOW}Yellow Background")
print(f"{Back.BLUE}Blue Background")
print(f"{Back.MAGENTA}Magenta Background")
print(f"{Back.CYAN}Cyan Background")
print(f"{Back.WHITE}White Background")
print()
print(f"{Style.DIM}S{Style.NORMAL}T{Style.BRIGHT}Y{Style.DIM}L{Style.NORMAL}E{Style.BRIGHT}!")
print(f"{Style.DIM}Dim Text")
print(f"{Style.NORMAL}Normal Text")
print(f"{Style.BRIGHT}Bright Text")
print()
print(f"{Fore.YELLOW}{Back.RED}C{Back.GREEN}{Fore.RED}O{Back.YELLOW}{Fore.BLUE}M{Back.BLUE}{Fore.BLACK}B{Back.MAGENTA}{Fore.CYAN}I{Back.CYAN}{Fore.GREEN}N{Back.WHITE}A{Back.RED}T{Back.GREEN}I{Back.YELLOW}O{Back.BLUE}N")
print(f"{Fore.GREEN}{Back.YELLOW}{Style.BRIGHT}Green Text - Yellow Background - Bright")
print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}Cyan Text - White Background - Dim")
