from staticcommands import *

class cmdfactory(object): # This will take in the player's command, and execute it from the command's file in staticcommands

    def factory(command, assetContainer): #Takes in the player's command, as well as assetContainer, which contains all player data to pass to each command.
        the_command = None
        if command == ('quit'):
            the_command = quit.quit()
        elif command == ('shop'):
            the_command = shop.shop(assetContainer)
        elif command == ('inv'):
            the_command = inv.inv(assetContainer)
        elif command == ('help'):
            the_command = help.help()
        elif command == ('save'):
            the_command = save.save(assetContainer)
        elif command == ('load'):
            the_command = load.load(assetContainer)
        elif command == ('battle'):
            the_command = battle.battle(assetContainer)
        else:
            the_command = error.error(assetContainer)
        the_command.execute()

    factory = staticmethod(factory)