# Items!

class consumable(object): #Consumable items, will be adding equipables in the future
    def __init__(self, name, count, heal, cost):
        self.name = name
        self.count = count
        self.heal = heal
        self.cost = cost
