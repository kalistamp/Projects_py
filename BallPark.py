# [9/24/21]

# Automated Bartender serving people Beer at Ball Game

# IMPORTANT NOTE: Because i could not get a proper If / Else Statement to work for me and i am currently at
# ClubMallard with no Internet I decided to reference from my Coursea Notes (1/26/21) to program the code to count the
# length of the user input to determine the size to give the correct response Rather than the correct way,
# which i assume is defining each Size and the proper response that goes with it ..


spam = 'by: kalistamp'
x = ' '
print(x)
print('BALLPARK BARTENDER PY')
print(x)
print(spam.title())
print(x * 2)

# start

print('Hello hows it going \n Hope your enjoying the game today !')
print(x)
print('We have Fresh Fieldwork beer on tap \n Were are offering the hazy TigerEye IPA')
print(x)
print('Can i get you a "short" or a "tall" pour today ? ')

size = input()

print(x * 2)

print('Sounds Good ! ' + size + ' it is then, coming right up...')
print(x)
print('"Returns with drink - "')
print(x)


def total_price(size):
    if len(size) > 4:
        print('That\'s gonna be ' + str(6) + ' dollars please, will you be paying in "cash" or "credit" ')
    else:
        print('That\'s gonna be ' + str(12) + ' dollars please, will you be paying in "cash" or "credit" ')


total_price(size)
print(x)

payment = input()


def total_price(payment):
    if len(payment) > 4:
        print(' Sounds good! \n Let me run your card real quick ...')
    else:
        print(' Sounds Good! \n Let me grab your change for you ...')


total_price(payment)
print(x)

print('"Returns with receipt - "')
print(x * 2)
print('Thank you for coming to the Game ! \n Have a great day')
