# Chrome Extensions for new OS Setup
# By: Kалистамп

import webbrowser
x = ' '

print(x*2)
print('TABLE OF CONTENTS:')
print(x)
print('All (a): Open all the Extensions ')
print('Basics (b): Just the basic Extensions ')
print('Print (p): Just print out Extension List ')
print(x*2)

sources = [
    'https://therecap.org/chrome-ex/',
        'https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en',
        'https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci',
        'https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en',
        'https://chrome.google.com/webstore/detail/url-render/flhclpkhoiajoikkabbfbinnjapaflog?hl=en',
        'https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en',
        'https://chrome.google.com/webstore/detail/youtube-actual-top-commen/hbdmelobmfcompinikjdaiphhonbgfpn/related',
        'https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanb?hl=en-US',
        'https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe?hl=en',
        'https://chrome.google.com/webstore/detail/stethoscope/gdkkpjagibimlpgmcbaajccgahfbojec',
        'https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en'
]

def Chrome():
    choice = input(f'What Section of would you like to open? \n [Enter the Letter]: ')
    if choice == 'a':
        webbrowser.open_new_tab('https://therecap.org/chrome-ex/')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/url-render/flhclpkhoiajoikkabbfbinnjapaflog?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/youtube-actual-top-commen/hbdmelobmfcompinikjdaiphhonbgfpn/related')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanb?hl=en-US')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/ublacklist/pncfbmialoiaghdehhbnbhkkgmjanfhe?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/stethoscope/gdkkpjagibimlpgmcbaajccgahfbojec')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en')
    elif choice == 'b':
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanb?hl=en-US')
        webbrowser.open_new_tab('')
        webbrowser.open_new_tab('https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en')
    elif choice == 'p':
        for number, links in enumerate(sources):
            print(number, links)
    else:
        print('It seems you made a typo, that option does not exist')

Chrome()
