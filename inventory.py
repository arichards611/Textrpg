#Inventory, these are functions for handling the players inventory. Adding/removing items and displaying inventory.

class inventory(object):

    def __init__(self):
        self.items = []

    def __str__(player): # Prints out inventory items in a nice neat charts
        out = '\t'.join(['Name', 'Count', 'Cost'])
        for item in player.items:
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.count, item.cost]])
        return out

    def get_item(self, choice):
        for item in self.items:
            if item.name.lower() == choice.lower():
                return item
        return None

    def add_item(self, newitem):
        if self.items == []:
            self.items.append(newitem)
        else:
            for item in self.items:
                if item.name == newitem.name:
                    item.count +=1

    def remove_item(self, newitem):
        for item in self.items:
            if item.name == newitem.name:
                if item.count > 1:
                    item.count -= 1
                else:
                    self.items.remove(item)