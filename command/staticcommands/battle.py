import characters
import random
import sys
import command

class battle(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        #Enemy formatted with: Name, Attack, Speed, HP, Gold, XP
        enemies = [characters.enemy("Weakling", random.randint(1,3), 5, random.randint(4, 8), random.randint(0, 5), 10),
                   characters.enemy("Strongling", random.randint(2,5), random.randint(8, 12), random.randint(10, 15), random.randint(5, 10), 25)]
        encounter = random.randint(0,10)
        if encounter <= 7: #Choose your enemy
            enemy = enemies[0]
        else:
            enemy = enemies[1]
        print "You've encountered a {0}. It has {1} hp.".format(enemy.name, enemy.hp)
        while self.assetContainer.player.hp > 0 and enemy.hp > 0: #While both players are breathing
            status = self.assetContainer.player.get_status()
            for line in status:
                print line
            l = raw_input("What do you do? (Fight/Use/Run)")
            print ""
            choice = l.lower()
            if choice == ("fight"):
                if self.assetContainer.player.speed > enemy.speed: #If you're faster, you go first
                    self.player_attack(enemy)
                    print ""
                    self.enemy_attack(enemy)
                    print ""
                else:
                    self.enemy_attack(enemy)
                    print ""
                    self.player_attack(enemy)
            elif choice == ("use"): #Uses items, and the enemy takes its turn
                command.cmdfactory.cmdfactory.factory("inv", self.assetContainer)
                enemyturn = self.enemy_attack(enemy)
                print ""
                print str(enemyturn)
                print ""
            elif choice == ("run"):
                if self.assetContainer.player.speed > enemy.speed: #If you're faster, you run away
                    print ""
                    print "You ran away!"
                    return
                else:
                    spd = enemy.speed - self.assetContainer.player.speed #if you're not faster, subtract your speed from
                    chance = random.randint(0,5)
                    if spd > chance:
                        print ""
                        print "You ran away!"
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

    def player_attack(self, enemy): #player attack function
        damage = self.assetContainer.player.attack + random.randint(-2,2)
        miss = random.randint(0,10) #Might do a different hit/miss someday
        if miss <= 2:
            print "You missed!"
        else:
            enemy.remove_health(damage)
            if enemy.hp <= 0:
                enemy.hp = 0
            print "You did {0} damage, the enemy has {1} health remaining".format(damage, enemy.hp)

    def enemy_attack(self, enemy): #enemy's attack
        if enemy.hp > 0:
            hurt = enemy.attack + random.randint(-2,2)
            if hurt <= 0:
                print "The enemy {0} missed".format(enemy.name)
            else:
                self.assetContainer.player.remove_health(hurt)
                print "The enemy {0} attacked and did {1} damage.".format(enemy.name, hurt, self.assetContainer.player.hp)