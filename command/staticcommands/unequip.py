class unequip(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        print self.assetContainer.player.inv
        choice = raw_input("What would you like to unequip?: ")
        choice = choice.lower()
        if choice == ("back"):
            return False
        elif choice == ("wood sword"):
            item = self.assetContainer.player.inv.get_item(choice)
            self.assetContainer.player.unequipWeapon(item)