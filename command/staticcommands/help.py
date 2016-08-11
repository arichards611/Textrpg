class help(object):

    def execute(self): # Help command, just add player usable commands here
        cmds = ["Shop", "Inv", "Battle", "Equip", "Unequip", "Stats" "Save", "Load", "Quit"]
        print ("The following commands are useable: {0}").format(cmds)