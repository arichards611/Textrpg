#!/usr/bin/env python
# game script

from commands import commands
import os

class character(object):
    def __init__(self, gold, hp):
        self.hp = hp
        self.gold = gold
        self.name = ""

def game():
    os.system('clear')
    player = character(10, 20)
    instance = commands()
    game_over = False
    while not game_over:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
        else:
            command = raw_input("Please enter a command: ")
            command = command.lower()
            if command == 'quit':
                instance.quit()
                game_over = True
            elif command == ('status'):
                instance.status(player)
            elif command == ('talk shit get hit'): # Debug to test taking damage
                instance.hit(player)
            elif command == ('look away lose some pay'): # Debug to test losing gold
                if player.gold == 0:
                    print ("You're broke, you can't lose anymore money!")
            else:
                print ("That is not a valid command. Try again.")
                game_over = False
