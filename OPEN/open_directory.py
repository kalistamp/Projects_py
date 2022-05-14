#!/user/bin python3 Kalistamp Lists

# Disclaimer: This script is for educational purposes only.  

# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY RECONNAISSANCE
# Note: If ran in sudo Permissions will default to "Locked" 

import os

date = input(f'Enter_Todays_Date: ')
main = 'open_dir'

os.mkdir(main, mode=0o777) 

file = open(f"{main}/List.txt", "w") 
file.write("""

https://www.reddit.com/r/opendirectories/

https://www.reddit.com/user/ODScanner/

https://ewasion.github.io/opendirectory-finder/


                open-directories:

https://ewasion.github.io/opendirectory-finder/
https://github.com/fangfufu/httpdirfs
https://www.reddit.com/r/opendirectories/comments/933pzm/all_resources_i_know_related_to_open_directories/
https://the-eye.eu/public/
https://www.reddit.com/r/opendirectories/comments/75ya8g/the_holy_grail_of_indexes/
https://www.reddit.com/r/opendirectories/comments/902j1i/36_gb_of_flash_games_19k_files/
https://github.com/HerbL27/FileMasta
https://www.reddit.com/r/opendirectories
https://github.com/simon987/opendirectories-bot
http://panelshow.club/
https://www.reddit.com/r/panelshow
https://github.com/nektro/andesite
https://github.com/KoalaBear84/OpenDirectoryDownloader


""")
file.close()

file = open(f"{main}/Nts.txt", "w") 
file.write(f"""

                                Todays Date:   {date}
                                
                                Source: 

COMMENTS:



****************************************************************

- 

""")
file.close()
