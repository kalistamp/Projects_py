
# Automated Bus Driver at SFO/SIA


logo = 'by: kalistamp'
x = ' '
print(x*2)
print(logo.title())
print(x*2)

# start

print('Hello, World!')
print()
print('Hello, Welcome to the SFO/SIA transportation services \n What is your final stop today')
print()
des = input()
print('Sounds Good! ' + des + ' it is then ')
print()
print('The estimated time of arrival for stop ' + des + ' is about ' + str(15) + ' mins give or take')
print()
print('Hope you came early enough to clock in on time')
print('goodbye')
#
# END OF SCRIPT


#
#
#
#
#
#

# I ADDED AN SERIES OF DIFFERENT GREEETINGS FOR THE BUS DRIVER TOO SAY....

# THEN USED THE IMPORT-RANDOM MODULE
# Along with the random.choice, which is used for lists [aside from random.randint which is used on integers]
# TO SPIT OUT ONE OF THE MANY RESPONSES EACH TIME AT RANDOM


#Automated Bus Driver at SFO/SIA

import random

print(x*2)
logo = 'by: kalistamp'
print(logo.title())
print(x*2)

#start

GREET = ['Hello hows it going today, get in',
'Hey! its nice to meet you hop on in', 'Hello, Welcome to the SFO/SIA transportation services',
'Hows it hanging buddy, ready for work', 'Okay piss off or get in the bus', 'Im not having a good day... get the fuck in',
'Fuck off or get in']

def randgreet():
  greeting = random.choice(GREET)
  print(greeting)

randgreet()

print('What stop is your final destination today?')

des = input()

print('Sounds Good! ' + des + ' it is then ')
print(x)
print('The estimated time of arrival for stop ' + des + ' is about ' + str(15) + ' mins give or take \n Hope you came early enough to clock in on time')
print(x*2)
print('"After a long quiet 15 min ride you approach your stop and get off the bus for work ..." ')
print(x*2)
print('goodbye')

#end of script
