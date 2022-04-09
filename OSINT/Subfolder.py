


# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY RECONNAISSANCE

# Note: If ran in sudo Permissions will default to "Locked" 


import os

main = 'AP'
sub_one = 'SharkCaps'
sub_two = 'WordLi'
sub_tree = 'Hashcat'
sub_four = 'Xtras'
# sub_five = 'Xtras_2'

os.mkdir(main, mode=0o777)
# "0o777" is Defauly Mode to unlock all permissions ...
os.mkdir(sub_one, mode=0o777)
os.mkdir(sub_two, mode=0o777)
os.mkdir(sub_tree, mode=0o777)
os.mkdir(sub_four, mode=0o777)
# os.mkdir(sub_five, mode=0o777)

# [ "os.chmod" can change the permissions of anyy Directory or File created by "os", or any other arugment you use such as "open/write" ]


file = open("Txt", "w") 
file.write("Text Input")
file.close()

file = open("Man", "w") 
file.write("""

--help CAN GO HERE ...


    """) 
file.close()
