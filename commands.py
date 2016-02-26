#commands class

import json

class commands(object):

    def quit(self):
        confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save! ")
        confirm = confirm.lower()
        if confirm[0] == 'y':
            print "Game over"
            game_over = True

    def status(self, player):
        print ("*"*10)
        print str(player.name)
        print ("Status:")
        print ("Current HP: " + str(player.hp))
        print ("Current gold: " + str(player.gold))
        print ("*"*10)

    def hit(self, player):
        player.hp -= 5
        print ("You got hit.")
        print ("You have {0} health left.").format(player.hp)

    def rob(self, player):
        player.gold -= 5
        print ("You payed up.")
        print ("You have {0} gold left.").format(player.gold)

    def save(self, player):
        filename = "./saves/{0}.txt".format(player.name)
        f = open(filename, "w")
        data = dict()
        data["name"] = player.name
        data["hp"] = player.hp
        data["gold"] = player.gold
        json.dump(data, f)
        print ("Game saved as {0}").format(player.name)
        f.close()

    def load(self, player):
        filename = raw_input("Please enter the name of the save: ")
        f = open("./saves/"+filename+".txt", "r")
        data = json.load(f)
        player.name = data["name"]
        player.hp = data["hp"]
        player.gold = data["gold"]
        f.close()

    def help(self):
        print ("The following commands are useable: ")
        print ("Help, Hit, Load, Quit, Pay, Save")
