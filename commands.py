#commands class

from items import potion
import json
import random

class commands(object):

    def quit(self):
        confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save! ") # Input for quit
        confirm = confirm.lower() # Lowercases the string
        if confirm[0] == 'y': # Checks that first letter is Y, if yes
            print "Thanks for playing!"
            return True
        else: # If first letter is anything but Y
            return False

    def status(self, player): # Since we are using some of the character variables, we pass self, and player
        msg = ("*"*10,
                str(player.name),
                "Status:",
                "Current HP: " + str(player.hp),
                "Current Gold: " + str(player.gold),
                "Inventory: "+str(len(player.inv)),
                "*"*10)
        return msg

    def enemy_status(self, enemy):
        return ("*"*10, str(enemy.name), "Status:", "Current HP: " + str(enemy.hp),
                "*"*10)

# Test commands

    def hit(self, player):  # Same as above
        player.remove_health(5)
        return "You got hit.", "You have {0} health left.".format(player.hp) # Returns both lines as a list, for our output function

    def rob(self, player): # and again
        if player.gold > 0:
            player.remove_gold(5)
            return "You payed up.", "You have {0} gold left.".format(player.gold) # Same as hit
        else:
            return "You're broke",

    def pot_add(self, player):
        new_potion = potion(0, 10)
        player.inv.append(new_potion)
        return "Added 1 potion to inventory",

    def use_item(self, player):
        if len(player.inv) > 0:
            p = player.inv[0]
            p.use(player)
            if p.used:
                player.inv.remove(p)
                return "You used a potion and recovered some hp.",
            else:
                return "You're at full health. Nothing happened.",
        else:
            return "You have no potions to use.",

# Saving, loading, help functions

    def save(self, player):
        filename = "./saves/{0}.txt".format(player.name) # Establishes the name of the save
        f = open(filename, "w") # Set f to opening the file name with w for write permissions
        data = dict() # Creating the dictionary for easier saving
        data["name"] = player.name
        data["hp"] = player.hp
        data["gold"] = player.gold
        json.dump(data, f) # Dumps the data dictionary into f
        f.close() # Closes the file
        return 'Game saved as {0}'.format(player.name)

    def load(self, player):
        filename = raw_input("Please enter the name of the save: ") # Asks which file to open, must know file name
        f = open("./saves/"+filename+".txt", "r") # Open file
        data = json.load(f) # This loads our dictionary entries back into "data"
        player.name = data["name"]
        player.hp = data["hp"]
        player.gold = data["gold"]
        f.close() # Close the file
        return 'Game {0} loaded.'.format(player.name)

    def help(self):
        print ("The following commands are useable: ")
        self.cmds = [] # Creates empty list, referring to self for this scope
        exclude = ["_", "cmds", "status", "hit", "rob", "pot_add" "use_item"]
        for x in dir(self): # for each entry of this directory
            if x[0] != "_" and x not in exclude: # If it doesn't begin with _, cmds, or status
                cap = x[0].upper() + x[1:] # Capitalizes the first letter, then finishes the word with lowercase
                self.cmds.append(cap) # Add to the self.cmds list
        return self.cmds

# Fighting functions

    def battle(self, player, enemy):
        print "You've encountered a {0}. It has {1} hp.".format(enemy.name, enemy.hp)
        while player.hp > 0 and enemy.hp > 0:
            l = raw_input("What do you do? (Fight/Run)")
            choice = l.lower()
            if choice == ("fight"):
                damage = random.randint(0,5)
                if damage == 0:
                    print "You missed!"
                else:
                    enemy.remove_health(damage)
                    if enemy.hp <= 0:
                        enemy.hp = 0
                    print "You did {0} damage, the enemy has {1} health remaining".format(damage, enemy.hp)
            elif choice == ("run"):
                print "You ran away!"
                return False
            else:
                print "You can only fight or run"
        else:
            if enemy.hp <= 0:
                print "You win!"
                player.gold += enemy.gold
                return False
