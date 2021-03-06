#intro

import os
import characters
from assets import *
from command import cmdfactory

def startup():
    os.system('clear')
    player = characters.player(20, 10, "")
    while player.name == "":
        s = raw_input("What would you like to do? New/Load: ")
        choice = s.lower()
        if choice == "new":
            player.name = intro(player)
            print player.name
            the_assetContainer = assetContainer.assetContainer(player)
            game(the_assetContainer)
        elif choice == "load":
            cmdfactory.cmdfactory.factory(choice, player)
            the_assetContainer = assetContainer.assetContainer(player)
            game(the_assetContainer)
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

def output(response):
    for x in response:
        if len(str(x)) > 0:
            print x

def game(assetContainer):
    os.system('clear')
    game_over = False

    while not game_over:
        if assetContainer.player.hp <= 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response = ""
            status = assetContainer.player.get_status()
            output(status)
            command = raw_input("Please enter a command or see commands with 'help': ")
            command = command.lower()
            cmdfactory.cmdfactory.factory(command, assetContainer)
            output(response)
