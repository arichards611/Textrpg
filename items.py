# Items!


class consumable(object):
    def __init__(self, name, count, heal, cost):
        self.name = name
        self.count = count
        self.heal = heal
        self.cost = cost

    def use(player, item):
        if item == ('potion'):
            if player.hp < player.max_hp:
                player.add_health(self.heal)


class inventory(object):
    def __init__(self):
        self.items = {}

    def __str__(self):
        out = '\t'.join(['Name', 'Count', 'Cost'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.count, item.cost]])
        return out

    def add_item(self, item):
        self.items[item.name] = item
