from staticcommands import *
import characters
from random import randint
from random import choice

class cmdfactory(object):
    def factory(command, engine):
        the_command = None
        if command == ('quit'):
            the_command = quit.quit()
        elif command == ('hit'):  # Debug to test taking damage
            the_command = hit.hit(engine)
        elif command == ('rob'):  # Debug to test losing gold
            the_command = rob.rob(engine)
        elif command == ('pot'):  # Debug to add potion
            the_command = potion.potion(engine)
        elif command == ('shop'):
            the_command = shop.shop(engine)
        elif command == ('inv'):
            the_command = inv.inv(engine)
        elif command == ('help'):
            #todo
            return
        elif command == ('save'):
            #todo
            return
        elif command == ('load'):
            #todo
            return
        elif command == ('battle'):

            the_command = battle.battle(engine)
        else:
            response = ("That is not a valid command. Try again.",)
        the_command.execute()

    factory = staticmethod(factory)