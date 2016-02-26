#commands class
class commands(object):

    def quit(self):
        confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save! ")
        confirm = confirm.lower()
        if confirm == 'yes':
            print "Game over"
            game_over = True
        else:
            print ("We all make mistakes.")

    def status(self, player):
        print ("*"*10)
        print str(player.name)
        print ("Status:")
        print ("Current HP: " + str(player.hp))
        print ("Current gold: " + str(player.gold))
        print ("*"*10)

    def hit(self, player):
        player.hp -= 5
        print ("You got hit.")
        print ("You have {0} health left.").format(player.hp)

    def rob(self, player):
        player.gold -= 5
        print ("You payed up.")
        print ("You have {0} gold left.").format(player.gold)

    def help(self):
        print ("The following commands are useable: ")
        print ("Help, Hit, Quit, Pay")
