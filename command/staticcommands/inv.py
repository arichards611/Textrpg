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
                cons = self.assetContainer.player.inv.get_item(choice)
                self.assetContainer.player.use_cons(cons)
        else:
            print "You have no items in your inventory."