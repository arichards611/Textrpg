import characters
import random
import sys

class battle(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        enemies = [characters.enemy("Weakling", random.randint(3, 10), random.randint(0, 5), 10),
                   characters.enemy("Strongling", random.randint(10, 15), random.randint(5, 10), 25)]
        enemy = random.choice(enemies)
        print "You've encountered a {0}. It has {1} hp.".format(enemy.name, enemy.hp)
        while self.assetContainer.player.hp > 0 and enemy.hp > 0:
            status = self.assetContainer.player.get_status()
            for line in status:
                print line
            l = raw_input("What do you do? (Fight/Use/Run)")
            print ""
            choice = l.lower()
            if choice == ("fight"):
                self.player_attack(enemy)
                print ""
                self.enemy_attack(enemy)
                print ""
            elif choice == ("use"):
                pass #TODO ADD USE OF ITEMS OR AT LEAST POTIONS
                enemyturn = self.enemy_attack(enemy)
                print ""
                print str(enemyturn)
                print ""
            elif choice == ("run"):
                escape = random.randint(0, 10)
                if escape >= 2:
                    print ""
                    print "You ran away!"
                    return
                else:
                    print ""
                    print "You failed to run away"
                    print ""
                    self.enemy_attack(enemy)
            else:
                print "You can only fight, use or run"
        else:
            if enemy.hp <= 0:
                print "You win! You gained {0} XP. The enemy {1} dropped {2} gold.".format(enemy.xp, enemy.name, enemy.gold)
                self.assetContainer.player.add_gold(enemy.gold)
                self.assetContainer.player.xp_up(enemy.xp)
                return
            if self.assetContainer.player.hp <= 0:
                print "You died. Game over."
                sys.exit()

    def player_attack(self, enemy):
        damage = self.assetContainer.player.attack + random.randint(1,3)
        miss = random.randint(0,10)
        if miss <= 2:
            print "You missed!"
        else:
            enemy.remove_health(damage)
            if enemy.hp <= 0:
                enemy.hp = 0
            print "You did {0} damage, the enemy has {1} health remaining".format(damage, enemy.hp)

    def enemy_attack(self, enemy):
        if enemy.hp > 0:
            hurt = random.randint(0, 3)
            if hurt == 0:
                print "The enemy {0} missed".format(enemy.name)
            else:
                self.assetContainer.player.remove_health(hurt)
                print "The enemy {0} attacked and did {1} damage.".format(enemy.name, hurt, self.assetContainer.player.hp)