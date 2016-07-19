#intro

import os
from commands import commands
import characters
import game
import json
from assets import *


instance = commands()

def startup():
    os.system('clear')
    player = characters.character(20, 10, [], "")

    while player.name == "":
        s = raw_input("What would you like to do? New/Load: ")
        choice = s.lower()
        if choice == "new":
            player.name = intro(player)
            print player.name
            the_engine = engine.engine(player)
            game.game(the_engine)
        elif choice == "load":
            instance.load(player)
            the_engine = engine.engine(player)
            game.game(the_engine)
        else:
            print "That is not a valid command."

def intro(newchar):
    os.system('clear')
    name = ""
    while name == "":
        name = raw_input("Welcome, please enter your name: ")
        if name.isalpha():
            print ("Hello {0} and thank you for playing. Here's 10 gold to start.").format(name)
            return name
        else:
            print ("Names can only contain letters. Try again.")
            name = ""
    return name
