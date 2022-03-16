

# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY INVESTIGATION 


import os

main = 'Target'
sub_one = 5

output = input(f'enter the output Path:  ')

chdir = os.path.realpath('%', output)

chdir(output)

print(os.mkdir(str(main)))

print(os.mkdir(str(sub)))

#
# THE ABOVE CODE WILL NOT WORK, WAS ORIGONALLY GETTING THE ERROR "TypeError: 'str' object is not callable" ...
#
# WAS TOLD TO ADD A "%" IN THE STRING TRYING TO BE PRINTED ... SO I CHANGED THE "chdir" VARIABLE TOO "os.path.realpath('%', output)" SO THAT THERE IS A PERCENTAGE ADDED TO THE "output"
#
# NOW IM JUST RECEIVING THE ERROR "TypeError: realpath() takes 1 positional argument but 2 were given" .... 
#
# FIX AND FINISH THIS ABOVE CODE SO THAT WHEN IT PRINTS THE DESIRED FOLDERS I WANT THAT THERE ARE ALL CREATED IN WHATEVER OUTPUT DIRECTORY THE USER WANTS THEM CREATED IN ....
#
# AFTER THAT ... FIGURE OUT HOW TO CREATE CUSTOM NAMED TXT FILES INSIDE THOSE FOLDERS THAT WERE JUST CREATED
#
# GONNA TAKE SOME WORK 
#

import os

main = 'Target'
sub_one = 'Home'
sub_two = 'Socials'
sub_tree = 'Connections'
sub_four = 'Work'
sub_five = 'Extras'

print(os.mkdir(str(main)))
print(os.mkdir(str(sub_one)))
print(os.mkdir(str(sub_two)))
print(os.mkdir(str(sub_tree)))
print(os.mkdir(str(sub_four)))
print(os.mkdir(str(sub_five)))

#
# NOT3:
# WHY DO THE FOLDERS GET CREATED LOCKED WITHOUT SUDO PERMISSIONS?
# 
