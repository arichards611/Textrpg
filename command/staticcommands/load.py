import json

class load(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): #Loads the game. This is currently possible anywhere. Will be restricted with locations as well.
        filename = raw_input("Please enter the name of the save: ")  # Asks which file to open, must know file name
        f = open("./saves/" + filename + ".txt", "r")  # Open file
        data = json.load(f)  # This loads our dictionary entries back into "data"
        self.assetContainer.player.name = data["name"]
        self.assetContainer.player.hp = data["hp"]
        self.assetContainer.player.gold = data["gold"]
        #self.assetContainer.player.inv = data["inv"]
        self.assetContainer.player.max_hp = data["max_hp"]
        self.assetContainer.player.attack = data["attack"]
        self.assetContainer.player.defense = data["defense"]
        self.assetContainer.player.armor = data["armor"]
        self.assetContainer.player.level = data["level"]
        self.assetContainer.player.speed = data["speed"]
        self.assetContainer.player.weight = data["weight"]
        self.assetContainer.player.xp = data["xp"]
        f.close()  # Close the file
        return "Game {0} loaded.".format(self.assetContainer.name)