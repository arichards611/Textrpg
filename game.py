#!/usr/bin/env python
# game script

from items import potion
from commands import commands
from random import randint
from random import choice
import story
import characters
import os

def output(response):
    for x in response:
        if len(str(x)) > 0:
            print x

def game(player):
    os.system('clear')
    instance = commands()
    game_over = False

    while not game_over:
        if player.hp <= 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response = ""
            status = instance.status(player)
            output(status)
            command = raw_input("Please enter a command or see commands with 'help': ")
            command = command.lower()

            if command == ('quit'):
                if instance.quit(game_over) is True:
                    game_over = True
            elif command == ('hit'): # Debug to test taking damage
                response = instance.hit(player)
            elif command == ('rob'): # Debug to test losing gold
                response = instance.rob(player)
            elif command == ('pot'): #Debug to add potion
                response = instance.pot_add(player)
            elif command == ('inv'):
                invmenu = instance.inv(player)
            elif command == ('use'):
                response = instance.use_item(player)
            elif command == ('help'):
                response = instance.help()
            elif command == ('save'):
                response = instance.save(player)
            elif command == ('load'):
                 response = instance.load(player)
            elif command == ('battle'):
                enemies = [characters.enemy(randint(3, 10), randint(0,5), "Bonerfart"),
                characters.enemy(randint(10, 15), randint(5,10), "Scrub")]
                enemy = choice(enemies)
                instance.battle(player,enemy)
            else:
                response = ("That is not a valid command. Try again.",)
                game_over = False

            output(response)
