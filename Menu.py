# MENU
# MENU
# [ www python[.]plainenglish.io/build-a-fast-food-order-taker-in-python-87188efcbbdd ]


# START MENU PY

# Notice the menu we are making uses curley brackets instead of the original brackets ,

# This is because we are making a "Set" instead of a "List"

spam = 'by: kalistamp'
x = ' '

print('Menu . Py')
print(x)
print(spam.title())
print(x*2)


menu = {'ipa', 'pilsner', 'bud', 'coors', 'redbull', 'water'}


# Next we are making a "While Loop", that asks the customer what they would like to order

def ask_order():
    current_order = []
    while True:
        print('Hey hows it goin! ')
        print(' The menu today is: \n' + ', \n' .join(menu))
        print('\n')
        print('What can i get for you?')
        order = input()
        if order in menu:
            current_order.append(order)
        else:
            print('I\'m sorry that item is not on menu list.')
        if order_done():
            return current_order


# After this while True loop is ran the program is checking the input (order) of the customers choice to see if it is
# in the menu we made, If the drink is, the script appends the order to the current_order, but if we order something
# like tea which is not on the menu, the Else script then runs the print saying sorry item is not on menu Adding the
# order to the current_order, else printing the sorry string
#
#
#
# We must now put in a way for us to escape the "while loop" or we will contninue to run the same question over and
# over,

# We have 3 options when coding a way to escape a "While Loop" . . . . :
#
#
# " In order to escape a while loop, we have 3 options: return which takes us out of the function, set the condition
# to False (not possible here since it’s True), or use a new command called break. There are two new commands in
# loops that we haven’t discussed: continue and break. continue is self explanatory: stop where we are and go back to
# the top of the loop. break cuts us out of the loop and allows us to move on in the function, past the while loop.
# In this project, we are going to make sure we are finished with the order, and return with our current_order
# variable. Take a look: "

def order_done():
    print('Anything else? [yes or no]')
    choice = input()
    if choice == 'no':
        return True
    elif choice == 'yes':
        return False
    else:
        print('Im sorry was that a yes or a no?')


def output_order(order_list):
    print('Okay, so you want :')
    for order in order_list:
        print(order)



def main():
    order = ask_order()
    output_order(order)
    print()
    print('Here you go ...')
    print()
    print('Thank\'s for coming today')


if __name__ == "__main__":
    main()
