#intro

import os

def intro(startup):
    os.system('clear')
    name = ""
    while name == "":
        name = raw_input("Welcome, please enter your name: ")
        if name.isalpha():
            print ("Hello {0} and thank you for playing. Here's 10 gold to start.").format(name)
        else:
            print ("Names can only contain characters. Try again.")
            name = ""
    return name
