#!/usr/bin/env python
# game script

from commands import commands
from story import intro
import os

class character(object):
    def __init__(self, gold, hp, name):
        self.hp = hp
        self.gold = gold
        self.name = name

    def remove_gold(self, amount):
        #do stuff and checks for gold
        if  self.gold > 0:
            self.gold -= amount

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount
        else:
            game_over = True
            return game_over

def output(response):
    for x in response:
        print x

def game():
    os.system('clear')
    startup = ""
    name = intro(startup)
    player = character(10, 20, name)
    instance = commands()
    game_over = False
    while not game_over:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response =instance.status(player)
            output(response)
            command = raw_input("Please enter a command: ")
            command = command.lower()
            if command == 'quit':
                game_over = instance.quit()
            elif command == ('hit'): # Debug to test taking damage
                response = instance.hit(player)
                output(response)
            elif command == ('rob'): # Debug to test losing gold
                response = instance.rob(player)
                output(response)
            elif command == ('help'):
                response = instance.help()
                output(response)
            elif command == ('save'):
                instance.save(player)
            elif command == ('load'):
                instance.load(player)
            else:
                print ("That is not a valid command. Try again.")
                game_over = False
