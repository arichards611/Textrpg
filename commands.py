#commands class
class commands(object):

    def quit(self):
        confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save!")
        confirm = confirm.lower()
        if confirm == 'yes':
            print "Game over"
            game_over = True
        else:
            print ("We all make mistakes.")

    def status(self, player):
        print ("Current HP: " + str(player.hp))
        print ("Current gold: " + str(player.gold))

    def hit(self, player):
        player.hp -= 5
        print ("Oh shit you got hit.")
        print ("You have {0} health left.").format(player.hp)

    def rob(self, player):
        player.gold -= 1
        print ("Oh shit you got robbed.")
        print ("You have {0} gold left.").format(player.gold)
