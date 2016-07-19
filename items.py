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
        self.items = []

    def __str__(player):
        out = '\t'.join(['Name', 'Count', 'Cost'])
        for item in player.items:
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.count, item.cost]])
        return out

    def add_item(player, newitem):
        print newitem
        for item in player.items:
            if item.name == newitem.name:
                item.count +=1
            else:
                player.items.append(item)
                print "added"
