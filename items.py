# Items!

class consumable(object): #Consumable items, will be adding equipables in the future
    def __init__(self, name, count, heal, cost):
        self.name = name
        self.count = count
        self.heal = heal
        self.cost = cost

    def use_cons(self, assetContainer, choice):
        if choice == 'potion': #Other consumables will be added later
            if assetContainer.player.hp < assetContainer.player.max_hp:
                assetContainer.player.add_health(self.heal)
        assetContainer.player.items.remove(choice)