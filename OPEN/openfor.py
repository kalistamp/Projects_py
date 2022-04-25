print(f'{RED}{LIT}TABLE OF CONTENTS:')

def Cstop_news():
    choice = input(f'What Section would you like to access ? \n [Enter the Letter]: ')
    if choice == 'c':
        webbrowser.open_new_tab('https://therecap.org/')
