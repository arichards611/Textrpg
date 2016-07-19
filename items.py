# Items!

class consumable(object):
    def __init__(self, name, count, heal, cost):
        self.name = name
        self.count = count
        self.heal = heal
        self.cost = cost

    def use_cons(self, player, choice):
        if player.hp < player.max_hp:
            player.add_health(self.heal)
        player.items.remove(choice)