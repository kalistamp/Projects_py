# Requirements
# By: калиштамп

import os

sources = [       'https://github.com/kalistamp',
'https://www.virustotal.com/gui/home/upload',
'https://vms.drweb.com/online/?lng=en',
'https://virusshare.com/',
'https://www.eset.com/us/home/online-scanner/',
'https://t.me/VirusTotalAV_bot',
'https://telegram.me/drwebbot'

 ]

# print(*sources, sep = '\n')
for number, links in enumerate(sources):
    print(number, links)

file = open("Anti_germs", "w") 
file.write("""

https://github.com/kalistamp
https://www.virustotal.com/gui/home/upload
https://vms.drweb.com/online/?lng=en
https://virusshare.com/
https://www.eset.com/us/home/online-scanner/
https://t.me/VirusTotalAV_bot
https://telegram.me/drwebbot

""")
file.close()

print(' [+] Recource list printed in current directory')
