import items

class potion(object):

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        potion = items.consumable('Potion', 1, 10, 10)
        print "im in potion"
        print self.engine.player.name
        self.engine.player.inv.add_item(potion)
        print "Added 1 potion to inventory"