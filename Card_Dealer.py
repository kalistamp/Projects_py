# This time using choice command with random instead of randint

# You are using choice command because you are working with lists (suits , ranks) instead of integers


print(' Card Dealer Script \n By: Kalistamp')
print('\n'*2)

import random

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def main():
    suite = random.choice(SUITS)
    rank = random.choice(RANKS)
    print(rank)
    print(suite)


# below is two different ways of printing the def function

# the two example are seperated by a blank print

# Execution:

main()

# ---------------------------
print()
print('. . . NEW LAYOUT . . .')
print()
# ---------------------------

# FIXING THE CODE ABOVE

# The card results prints out funny to the user , time to combine the suit and rank into one string

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def main():
    suite = random.choice(SUITS)
    rank = random.choice(RANKS)
    print(f'{rank} of {suite}')


main()

print()

# end

# NOTE BELOW --

# example of the f function before a printed string- makes it so you can add an input that the user has defined


print('Tell me that new layout doesnt look way better')
print('\n')

print('what size cup do you want?')
print('\n')
size = input()
print('\n')
print(f'sounds good {size} coming up')

# NOTE: If there is a format "f" at the beginning of the string, you can add the input created with these brackets " {} "


# end
