
# Happy coding! :-)

spam = 'by kalistamp'
print(spam.title())


print('MAGIC' + str(8) + 'BALL PY')
print()
print()

# DESCRIPTION -

# the following program defines a function that returns a different string depending on what number it is passed as an argument.

print()

#start

# geta = Get Answer 

import random

def geta(fortune):
  if fortune == 1:
    return 'Someones working harder'
  elif fortune == 2:
    return 'Hard work pays off'
  elif fortune == 3:
    return 'YES'
  elif fortune == 4:
    return 'NO'
  elif fortune == 5:
    return 'Keep on grinding'
  elif fortune == 6:
    return 'Dont deviate from the plan'
  elif fortune == 7: 
    return 'Tough times dont last , Tough people do'
  elif fortune == 8:
    return 'No ones likes a quitter'
  elif fortune == 9:
    return 'Nothing worth having comes easy'


# 3 Lines that are reffered too below

    
r = random.randint(1,9)

passage = geta(r)

print(passage)

print()
print()

# Note that since you can pass return values as an argument to another function call, you could shorten these three lines:


print(geta(random.randint (1,9)))


