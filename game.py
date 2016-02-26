#!/usr/bin/env python
# game script

from commands import commands
import os

class character(object):
    def __init__(self, gold, hp, name):
        self.hp = hp
        self.gold = gold
        self.name = name

def game():
    os.system('clear')
    name = raw_input("Please enter your name: ")
    print ("Hello {0} and thank you for playing. Here's 10 gold to start.").format(name)
    player = character(10, 20, name)
    instance = commands()
    game_over = False
    while not game_over:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            instance.status(player)
            command = raw_input("Please enter a command: ")
            command = command.lower()
            if command == 'quit':
                instance.quit()
            elif command == ('hit'): # Debug to test taking damage
                instance.hit(player)
            elif command == ('pay'): # Debug to test losing gold
                if player.gold == 0:
                    print ("You're broke.")
                else:
                    instance.rob(player)
            elif command == ('help'):
                instance.help()
            elif command == ('save'):
                instance.save(player)
            elif command == ('load'):
                instance.load(player)
            else:
                print ("That is not a valid command. Try again.")
                game_over = False
