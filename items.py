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

class inventory(object):
    def __init__(self):
        self.items = []

    def __str__(player):
        out = '\t'.join(['Name', 'Count', 'Cost'])
        for item in player.items:
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.count, item.cost]])
        return out

    def add_item(player, newitem):
        if player.items == []:
            player.items.append(newitem)
            return player.items
        for item in player.items:
            if item.name == newitem.name:
                item.count +=1
                return player.items

    def remove_item(player, choice):
        for item in player.items:
            if item.name.lower() == choice:
                if item.count > 1:
                    item.count -= 1
                else:
                    player.items.remove(item)