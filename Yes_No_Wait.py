# Happy coding! :-)
import random

logo = 'by: kalistamp'

print('Take This advice . . .')
print(logo)

# This is a spin off of the 8ball script i worked with ... telling me yes / no / or wait an hour

# you will be importing random

# and using def function to define my 3 options of what i should decide to do

def tellme(num):
    if num == 1:
        return 'Wait an Hour Give it some time'
    elif num == 2:
        return 'NO'
    elif num == 3:
        return 'YES'

# below 3 lines

fait = random.randint(1, 3)

ballshake = tellme(fait)

print(ballshake)
print()
print('.')
print('.')
print('.')
# Condensed version of the above 3 lines

# ~ ~ ~ CODE SNIPPET: print(tellme(random.randint(1,3)))

print('GOODBYE !!')
print('\n'*2)
print('Shortened code by creating list and using "choice" command instead of "randint" . . .')
print('\n'*2)

results = ["yes", "no", "fuck off"]

def main():
  theball = random.choice(results)
  print(theball)

main()

print('.')
print('.')
print('.')
#
#
#
#
# THE COMPUTER WILL DISPLAY TWO DIFFERENT FORTUNES BECAUSE THE CODE IN THIS SCRIPT IS WRITTEN TWICE;
# THE SECOND CHUNK OF CODE IS A MORE SIMPLISTIC CONDENSED VERSION OF HOW IT IS WRITTEN ABOVE ...
# CREATED A LIST AND USED THE RANDOM MODULE TO PICK A random "CHOICE" INSTEAD OF DEFINING AN IF/ELSE STATEMENT WITH NUMBERS (randint) ASSIGNED TO EACH FORTUNE 

