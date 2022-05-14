# Chrome Extensions for new OS Setup
# author = Автор: калистамп 

import webbrowser
import time
x = ' '

print(x*2)
print('TABLE OF CONTENTS:')
print(x)
print('All (a): Open all the Extensions ')
print('Basics (b): Just the basic Extensions ')
print('Print (p): Print out Extension List & Guides ')
print(x*2)

extension = [
    'https://therecap.org/chrome-ex/',
    'https://www.qbittorrent.org/download.php',
        'https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en',
        'https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=en',
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

basic = ['https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb?hl=en', 'https://chrome.google.com/webstore/detail/github-repository-size/apnjnioapinblneaedefcnopcjepgkci', 'https://chrome.google.com/webstore/detail/onetab/chphlpgkkbolifaimnlloiipkdnihall?hl=en', 'https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle?hl=en', 'https://chrome.google.com/webstore/detail/quick-source-viewer/cfmcghennfbpmhemnnfjhkdmnbidpanb?hl=en-US', 'https://chrome.google.com/webstore/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=en', 'https://chrome.google.com/webstore/detail/momentum/laookkfknpbbblfpciffpaejjkokdgca?hl=en']


sources = [
    'https://github.com/kalistamp',
    'https://www.google.com/chrome/',
    'https://twitter.com/1800otrack',
    'https://wallpaperbat.com/img/430531-usa-lake-mountains-stones-scenery-lake-tahoe-nevada-nature-407420.jpg',
]

methods = """

                        OHMYZSHELL (2 Methods) :

apt install zsh

apt install git

curl -

sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

wget -

sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"



                        Browser Uninstall Guides:

Microsoft edge windows 10 (Settings | Apps | Edge Version) -

cd %PROGRAMFILES(X86)%\Microsoft\Edge\Application\<EDGE_Version_#>\Installer 

setup.exe --uninstall --system-level --verbose-logging --force-uninstall

"""


vscode = """

                        VS_CODE Extensions :

cobalt2 theme
codestackr theme
fluent icons
tabnine
vscode-icons
python

"""

def Chrome():
    choice = input(f'What Section of would you like to open? \n [Enter the Letter]: ')
    print(x*2)
    if choice == 'a':
        for url in extension:
            time.sleep(3)
            webbrowser.open_new_tab(url)
    elif choice == 'b':
        for url in basic:
            time.sleep(3)
            webbrowser.open_new_tab(url)
    elif choice == 'p':
        for number, links in enumerate(extension):
            print(number, links)
        print(x*2)
        for number, links in enumerate(sources):
            print(number, links)
        print(x*2)       
        print(methods)
        print(vscode)
    else:
        print(' [!] It seems you made a typo, that option does not exist')

Chrome()
