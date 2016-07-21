class error(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): #Error handing for unvalid commands
        print "Not a valid command, please try again."