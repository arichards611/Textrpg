import json

class load(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): #Loads the game. This is currently possible anywhere. Will be restricted with locations as well.
        filename = raw_input("Please enter the name of the save: ")  # Asks which file to open, must know file name
        f = open("./saves/" + filename + ".txt", "r")  # Open file
        data = json.load(f)  # This loads our dictionary entries back into "data"
        self.assetContainer.name = data["name"]
        self.assetContainer.hp = data["hp"]
        self.assetContainer.gold = data["gold"]
        f.close()  # Close the file
        return "Game {0} loaded.".format(self.assetContainer.name)