class rob(object):

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        if self.engine.player.gold > 0:
            self.engine.player.remove_gold(5)
            return "You payed up.", "You have {0} gold left.".format(player.gold)  # Same as hit
        else:
            return "You're broke"