class hit(object):

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        self.engine.player.remove_health(5)
        return "You got hit.", "You have {0} health left.".format(self.engine.player.hp)  # Returns both lines as a list, for our output function
