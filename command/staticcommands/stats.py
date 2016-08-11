class stats(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        print "*" * 30
        print "Attack: " + str(self.assetContainer.player.attack)
        print "Defense: " + str(self.assetContainer.player.defense)
        print "Armor: " + str(self.assetContainer.player.armor)
        print "Speed: " + str(self.assetContainer.player.speed)