# Items!

class potion(object):
    def __init__(self, cost, restore):
        self.cost = cost
        self.restore = restore
        self.used = False
        self.amount = 0

    def use(self, player):
        if player.hp < player.max_hp:
            player.add_health()
            self.used = True
