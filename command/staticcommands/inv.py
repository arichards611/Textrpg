class inv(object):

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        if self.engine.player.inv.items != []:
            print ""
            print self.engine.player.inv
            print ""
            choice = raw_input("What item would you like to use? (""Back"" to cancel): ")
            choice = choice.lower()
            if choice == ('back'):
                return False
            else:
                self.engine.player.inv.remove_item(choice)
        else:
            print "You have no items in your inventory."