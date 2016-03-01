#Characters other than the main character

class character(object):
    def __init__(self, gold, hp, name):
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
        else:
            game_over = True
            return game_over
