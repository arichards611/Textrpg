#Characters other than the main character
import random
import sys
from inventory import inventory

class player(object):
    def __init__(self, hp, gold, inv, name):
        self.gold = gold
        self.hp = hp # This is the player's non-static HP.
        self.name = name
        self.inv = inventory()
        self.max_hp = 20 # Max HP will only change on level up
        self.attack = 5 # Determines your damage, effected by weapons later
        self.defense = 5 # Reduces damage by 50% of defense (50% is only temporary)
        self.armor = 0 # Reduces damage by 25% of armor (25% is only temporary)
        self.speed = 10 # Speed will determine who moves first. Can be negatively effected by weight
        self.weight = 0 # Weight of armor effects this.
        self.level = 1
        self.xp = 0 # XP,

    def add_health(self, amount):
        if self.hp >= self.max_hp:
            print "You are at full health."
        else:
            if self.hp < self.max_hp:
                amount = self.max_hp - self.hp
                if amount > 10:
                    self.hp += 10
                    return True
                else:
                    self.hp += amount
                    return amount, True


    def remove_gold(self, amount):
        #do stuff and checks for gold
        if self.gold > 0:
            self.gold -= amount #Gold goes below 0, you cannot have negative gold

    def add_gold(self, amount):
        self.gold += amount

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount
        elif self.hp <= 0:
            sys.exit()

    def get_status(self):  # Since we are using some of the character variables, we pass self, and player
        msg = ("*" * 10,
               str(self.name) + " Level " + str(self.level),
               "Status:",
               "Current HP: " + str(self.hp) + "/" + str(self.max_hp),
               "Current Gold: " + str(self.gold),
               "Current XP: " + str(self.xp),
               "*" * 10)
        return msg

    def xp_up(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.xp -= 100
            self.max_hp += random.randint(5,10)
            self.attack += random.randint(2,5)
            self.defense += random.randint(1,3)
            self.speed += random.randint(2,4)
            self.level += 1
            print "Level up! Your stats are now: {0} Max HP, {1} Attack, {2} Defense, and {3} Speed!".format(self.max_hp, self.attack, self.defense, self.speed)

    def use_cons(self, cons):
        if cons.name.lower() == 'potion':  # Other consumables will be added later
            if self.hp < self.max_hp:
                self.add_health(cons.heal)
                self.inv.remove_item(cons)
            else:
                print "You are at full health!"

class enemy(object):
    def __init__(self, name, hp, gold, xp):
        self.hp = hp
        self.gold = gold
        self.name = name
        self.xp = xp


    def remove_gold(self, amount):
        #do stuff and checks for gold
        if  self.gold > 0:
            self.gold -= amount
            if self.gold <= 0:
                self.gold = 0

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount

    def get_status(self):
        msg = ("*" * 10,
               str(self.name),
               "Status:",
               "Current HP: " + str(self.hp),
               "*" * 10)
        return msg