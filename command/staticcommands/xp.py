class xp(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): # debug command to force level up
        self.assetContainer.player.xp_up(100)