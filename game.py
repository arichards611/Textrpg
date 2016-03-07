#!/usr/bin/env python
# game script

from commands import commands
from random import randint
from story import intro
import characters
import os

def output(response):
    for x in response:
        if len(str(x)) > 0:
            print x

def game():
    os.system('clear')
    startup = ""
    name = intro(startup)
    player = characters.character(20, 10, [], name)
    instance = commands()
    game_over = False

    while not game_over:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response = instance.status(player)
            status = instance.status(player)
            output(status)
            command = raw_input("Please enter a command or see commands with 'help': ")
            command = command.lower()

            if command == ('quit'):
                response = instance.quit()
            elif command == ('hit'): # Debug to test taking damage
                response = instance.hit(player)
            elif command == ('rob'): # Debug to test losing gold
                response = instance.rob(player)
            elif command == ('pot'):
                response = instance.pot_add(player)
            elif command == ('use'):
                response = instance.use_item(player)
            elif command == ('help'):
                response = instance.help()
            elif command == ('save'):
                response = instance.save(player)
            elif command == ('load'):
                instance.load(player)
            elif command == ('battle'):
                enemy = characters.bonerfart(randint(3, 10), randint(0,5), "Bonerfart")
                instance.battle(player,enemy)
                response = ""
            else:
                response = ("That is not a valid command. Try again.",)
                game_over = False
            output(response)
