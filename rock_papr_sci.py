#
# ROCK | PAPER | SCISSORS
# (Real Python Podcast ep.91)
#
# A Simple Command Line Game
spam = 'a simple command line game\n by: kalistamp'
print(spam.title())
print('\n'*2)
#
#
import random

three_choices = ['rock', 'paper', 'scissors']
# ALTERNATIVE - (This is how the tutorial showed it,, i wrote it above my own way)

print('Throw down your choice! \n [ type rock, paper, or scissors: ]')
user_pick = input()

if user_pick in three_choices:
	computer_pick = random.choice(three_choices)
	print(
		f' You threw ' + user_pick + ' \n The computer threw ' + computer_pick )
else:
	print(' You typed "' + user_pick + '" which isn\'t a valid throw... \n Get it Together and Try Again')


#
# This is what the course showed as the correct example to use:
#
#if user_pick in choices:
#	computer_pick = random.choice(three_choices)
#	print(
#		f' You threw '{user_pick}' \n the computer threw '{computer_pick}'')
#else:
#	print(' You typed '{user_pick}' which isn\'t a valid throw... \n Get it Together and Try Again')

# After trying to run the script, i am told :  " SyntaxError: invalid syntax " pointing at the " { } "" Brackets as the invalid syntax

print('\n'*2)
print(' Run script to play again ')
