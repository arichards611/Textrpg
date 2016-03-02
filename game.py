#!/usr/bin/env python
# game script

from commands import commands
from story import intro
import characters
import os

def output(response):
    for x in response:
        print x

def game():
    os.system('clear')
    startup = ""
    name = intro(startup)
    player = characters.character(20, 10, name)
    instance = commands()
    game_over = False
    while not game_over:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response =instance.status(player)
            output(response)
            command = raw_input("Please enter a command or see commands with 'help': ")
            command = command.lower()
            if command == ('quit'):
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
            elif command == ('battle'):
                enemy = characters.bonerfart(5, 3, "Bonerfart")
                instance.battle(player,enemy)
            else:
                print ("That is not a valid command. Try again.")
                game_over = False
#test for commit editor
