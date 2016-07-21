#Inventory, these are functions for handling the players inventory. Adding/removing items and displaying inventory.

class inventory(object):
    def __init__(self):
        self.items = []

    def __str__(player): # Prints out inventory items in a nice neat charts
        out = '\t'.join(['Name', 'Count', 'Cost'])
        for item in player.items:
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.count, item.cost]])
        return out

    def add_item(player, newitem):
        if player.items == []:
            player.items.append(newitem)
        else:
            for item in player.items:
                if item.name == newitem.name:
                    item.count +=1

    def remove_item(player, choice):
        for item in player.items:
            if item.name.lower() == choice:
                if item.count > 1:
                    item.count -= 1
                else:
                    player.items.remove(item)