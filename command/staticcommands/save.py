import json

class save(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self): # Saves the game, but will be editing in the future when restricting save areas.
        filename = "./saves/{0}.txt".format(self.assetContainer.player.name)  # Establishes the name of the save
        f = open(filename, "w")  # Set f to opening the file name with w for write permissions
        data = dict()  # Creating the dictionary for easier saving
        data["name"] = self.assetContainer.player.name
        data["hp"] = self.assetContainer.player.hp
        data["gold"] = self.assetContainer.player.gold
        #data["inv"] = self.assetContainer.player.inv
        data["max_hp"] = self.assetContainer.player.max_hp
        data["attack"] = self.assetContainer.player.attack
        data["defense"] = self.assetContainer.player.defense
        data["armor"] = self.assetContainer.player.armor
        data["level"] = self.assetContainer.player.level
        data["speed"] = self.assetContainer.player.speed
        data["weight"] = self.assetContainer.player.weight
        data["xp"] = self.assetContainer.player.xp
        json.dump(data, f)  # Dumps the data dictionary into f
        f.close()  # Closes the file
        return "Game saved as {0}".format(self.assetContainer.player.name)