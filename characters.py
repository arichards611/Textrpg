#Characters other than the main character

class character(object):
    def __init__(self, hp, gold, inv, name):
        self.gold = gold
        self.hp = hp
        self.name = name
        self.inv = inv
        self.max_hp = 20
        self.armor = 0

    def add_health(self):
        if self.hp >= self.max_hp:
            return False
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

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount
        else:
            game_over = True
            return game_over

class enemy(object):
    def __init__(self, hp, gold, name):
        self.gold = gold
        self.hp = hp
        self.name = name

    def remove_gold(self, amount):
        #do stuff and checks for gold
        if  self.gold > 0:
            self.gold -= amount

    def remove_health(self, amount):
        if self.hp > 0:
            self.hp -= amount
