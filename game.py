#!/usr/bin/env python
# game script

class character:
    def __init__(self, gold, hp, ):
        self.hp = hp
        self.gold = gold
        self.name = ""



def game():
    player = character(10, 20)
    game_over = False
    while game_over == False:
        if player.hp == 0:
            print ("Oh no, you are dead. Game Over.")
            game_over = True
            return game_over
        command = raw_input("Please enter a command: ")
        command = command.lower()
        if command == 'quit':
            confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save!")
            confirm = confirm.lower()
            if confirm == 'yes':
                print "Game over"
                game_over = True
                return game_over
            else:
                print ("We all make mistakes.")
        elif command == 'status':
            print ("Current HP: " + str(player.hp))
            print ("Current gold: " + str(player.gold))
        elif command == ('talk shit get hit'): # Debug to test taking damage
            player.hp -= 5
            print ("Oh shit you got hit.")
            print ("You have {0} health left.").format(player.hp)
        elif command == 'look away lose some pay': # Debug to test losing gold
            player.gold -= 1
            print ("Oh shit you got robbed.")
            print ("You have {0} gold left.").format(player.gold)
        else:
            print ("That is not a valid command. Try again.")
            game_over = False
