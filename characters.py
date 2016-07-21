#Characters other than the main character

from inventory import inventory

class player(object):
    def __init__(self, hp, gold, inv, name):
        self.gold = gold
        self.hp = hp
        self.name = name
        self.inv = inventory()
        self.max_hp = 20
        self.armor = 0

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
        if  self.gold > 0:
            self.gold -= amount

    def add_gold(self, amount):
        self.gold += amount

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount
        elif self.hp <= 0:
            game_over = True
            return game_over

    def get_status(self):  # Since we are using some of the character variables, we pass self, and player
        msg = ("*" * 10,
               str(self.name),
               "Status:",
               "Current HP: " + str(self.hp),
               "Current Gold: " + str(self.gold),
               "*" * 10)
        return msg

    def use_cons(self, cons):
        if cons.name.lower() == 'potion':  # Other consumables will be added later
            if self.hp < self.max_hp:
                self.add_health(cons.heal)
                self.inv.remove_item(cons)
            else:
                print "You are at full health!"

class enemy(object):
    def __init__(self, hp, gold, name):
        self.hp = hp
        self.gold = gold
        self.name = name

    def remove_gold(self, amount):
        #do stuff and checks for gold
        if  self.gold > 0:
            self.gold -= amount

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