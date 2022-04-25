#! /usr/bin/python3

# Disclaimer: This script is for educational purposes only. None of the authors, contributors, administrators, vandals, or anyone else connected with sources, in any way whatsoever, can be responsible for your use of the information contained in or linked from these web pages. 


print(f'{RED}{LIT}TABLE OF FORUM CONTENTS:')
print(f'{RED}{LIT}cstop(c):{RESET} Open Clearnets ')
print(f'{RED}{LIT}tech(o):{RESET} Print Onion Lnks ')
print(f'{RED}{LIT}Xtras(r):{RESET} Print Ran Lnks')

def Forums():
    choice = input(f'What Section would you like to access? \n [Enter the Letter]: ')
    if choice == 'c':
        webbrowser.open_new_tab('https://exploit.in/')
        webbrowser.open_new_tab('https://cracked.io/')
        webbrowser.open_new_tab('https://cracked.io/')
        webbrowser.open_new_tab('https://sinister.ly/')
        webbrowser.open_new_tab(' ')
        webbrowser.open_new_tab(' ')


    elif choice == 't':
        file = open(f"ONI", "w") 
        file.write("""

Sources - https://tor.taxi/ | https://oniontree.org/

CryptBB - 

    """)
        file.close()
    elif choice == 'x':
        file = open(f"RAN", "w") 
        file.write("""

Directories: 

    """)
        file.close()
    else:
        print('It seems you made a typo, that section does not exist')

Forums()
