#!/usr/bin/env python
# game script

import os
from command import cmdfactory


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