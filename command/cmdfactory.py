from staticcommands import *

class cmdfactory(object):
    def factory(command, engine):
        the_command = None
        if command == ('quit'):
            the_command = quit.quit()
        elif command == ('hit'):  # Debug to test taking damage
            #todo
            return
        elif command == ('rob'):  # Debug to test losing gold
            #todo
            return
        elif command == ('pot'):  # Debug to add potion
            print ("{0} being called").format(command)
            the_command = potion.potion(engine)
        elif command == ('shop'):
            #todo
            return
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
            #todo
            return
        else:
            response = ("That is not a valid command. Try again.",)
        the_command.execute()

    factory = staticmethod(factory)