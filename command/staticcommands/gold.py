class gold(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        self.assetContainer.player.gold += 50