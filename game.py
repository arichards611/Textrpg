#!/usr/bin/env python
# game script

from commands import commands
import story
import characters
import os
from command import cmdfactory


def output(response):
    for x in response:
        if len(str(x)) > 0:
            print x

def game(engine):
    os.system('clear')
    instance = commands()
    game_over = False

    while not game_over:
        if engine.player.hp <= 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            response = ""
            status = instance.status(engine.player)
            output(status)
            command = raw_input("Please enter a command or see commands with 'help': ")
            command = command.lower()
            cmdfactory.cmdfactory.factory(command, engine)

            # if command == ('quit'):
            #     if instance.quit(game_over) is True:
            #         game_over = True
            # elif command == ('hit'): # Debug to test taking damage
            #     response = instance.hit(player)
            # elif command == ('rob'): # Debug to test losing gold
            #     response = instance.rob(player)
            # elif command == ('pot'): #Debug to add potion
            #     response = instance.potion_add(player)
            # elif command == ('shop'):
            #     shopmenu = instance.shop(player)
            # elif command == ('help'):
            #     response = instance.help()
            # elif command == ('save'):
            #     response = instance.save(player)
            # elif command == ('load'):
            #      response = instance.load(player)
            # elif command == ('battle'):
            #     enemies = [characters.enemy(randint(3, 10), randint(0,5), "Bonerfart"),
            #     characters.enemy(randint(10, 15), randint(5,10), "Scrub")]
            #     enemy = choice(enemies)
            #     instance.battle(player,enemy)
            # else:
            #     response = ("That is not a valid command. Try again.",)
            #     game_over = False

            output(response)
