import items

class inv(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): # This brings up the inventory MENU for the player. Not to be confused with player's inventory
        if self.assetContainer.player.inv.items != []: #If player's inv.items is blank (this IS iterable!)
            print ""
            print self.assetContainer.player.inv
            print ""
            choice = raw_input("What item would you like to use? (""Back"" to cancel): ")
            choice = choice.lower()
            if choice == ('back'):
                return False
            elif choice == ('potion'):
                items.consumable.use_cons(self, choice)
        else:
            print "You have no items in your inventory."