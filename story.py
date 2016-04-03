#intro

import os
from commands import commands
import characters
import game
import json

instance = commands()

def startup():
    os.system('clear')
    s = raw_input("What would you like to do? New/Load: ")
    choice = s.lower()
    player = characters.character(20, 10, [], "")
    if choice == "new":
        player.name = intro(player)
        print player.name
        game.game(player)
    elif choice == "load":
        # player = characters.character(20, 10, [], "")
        filename = raw_input("Please enter the name of the save: ") # Asks which file to open, must know file name
        f = open("./saves/"+filename+".txt", "r") # Open file
        data = json.load(f) # This loads our dictionary entries back into "data"
        player.name = data["name"]
        player.hp = data["hp"]
        player.gold = data["gold"]
        f.close() # Close the file
        game.game(player)
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
            print ("Names can only contain characters. Try again.")
            name = ""
    return name
