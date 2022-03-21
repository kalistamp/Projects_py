

# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY RECONNAISSANCE


import os

main = 'Target'
sub_one = 'Home'
sub_two = 'Socials'
sub_tree = 'Connections'
sub_four = 'Work'
sub_five = 'Extras'

os.mkdir(main, mode=0o777)
# "0o777" is Defauly Mode to unlock all permissions ...
os.mkdir(sub_one, mode=0o777)
os.mkdir(sub_two, mode=0o777)
os.mkdir(sub_tree, mode=0o777)
os.mkdir(sub_four, mode=0o777)
os.mkdir(sub_five, mode=0o777)

file = open("test.txt", "w") 
file.write("Your text goes here") 
file.close()

# [ "os.chmod" can change the permissions of anyy Directory or File created by "os", or any other arugment you use such as "open/write" ]
