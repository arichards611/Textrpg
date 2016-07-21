#intro

import os
import characters
import game
from assets import *

def startup():
    os.system('clear')
    player = characters.player(20, 10, [], "")

    while player.name == "":
        s = raw_input("What would you like to do? New/Load: ")
        choice = s.lower()
        if choice == "new":
            player.name = intro(player)
            print player.name
            the_assetContainer = assetContainer.assetContainer(player)
            game.game(the_assetContainer)
        elif choice == "load":
            instance.load(player)
            the_assetContainer = assetContainer.assetContainer(player)
            game.game(the_assetContainer)
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
