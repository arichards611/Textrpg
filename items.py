# Items!

class potion(object):
    def __init__(self, cost, name):
        self.cost = 10
        self.name = name

    def use(self, player):
        if player.hp < player.max_hp:
            player.add_health()
            self.used = True
