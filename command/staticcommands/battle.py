import characters
import commands
import random

class battle(object):

    def __init__(self, engine):
        self.engine = engine

    def execute(self):
        enemies = [characters.enemy(random.randint(3, 10), random.randint(0, 5), "Weakling"),
                   characters.enemy(random.randint(10, 15), random.randint(5, 10), "Scrub")]
        enemy = random.choice(enemies)
        battle = True
        while battle:
            print "You've encountered a {0}. It has {1} hp.".format(enemy.name, enemy.hp)
            while self.engine.player.hp > 0 and enemy.hp > 0:
                status = commands.commands.status(self, engine)
                for line in status:
                    print line
                l = raw_input("What do you do? (Fight/Use/Run)")
                print ""
                choice = l.lower()
                if choice == ("fight"):
                    playturn = battle.player_attack(self, self.engine.player, enemy)
                    print ""
                    enemyturn = battle.enemy_attack(self, self.engine.player, enemy)
                    print ""
                elif choice == ("use"):
                    result = battle.use_item(self, self.engine.player)
                    print ""
                    print str(result)
                    print ""
                    enemyturn = battle.enemy_attack(self, self.engine.player, enemy)
                    print ""
                    print str(enemyturn)
                    print ""
                elif choice == ("run"):
                    escape = random.randint(0, 10)
                    if escape >= 4:
                        print ""
                        print "You ran away!"
                        battle = False
                    else:
                        print ""
                        print "You failed to run away"
                        print ""
                        enemyturn = battle.enemy_attack(self, self.engine.player, enemy)
                else:
                    print "You can only fight, use or run"
            else:
                if enemy.hp <= 0:
                    print "You win! The enemy {0} dropped {1} gold.".format(enemy.name, enemy.gold)
                    self.engine.player.add_gold(enemy.gold)
                    battle = False
                if self.engine.player.hp <= 0:
                    game_over = True
                    return game_over

    def player_attack(self, engine, enemy):
        damage = random.randint(0, 5)
        if damage == 0:
            print "You missed!"
        else:
            enemy.remove_health(damage)
            if enemy.hp <= 0:
                enemy.hp = 0
            print "You did {0} damage, the enemy has {1} health remaining".format(damage, enemy.hp)

    def enemy_attack(self, engine, enemy):
        if enemy.hp > 0:
            hurt = random.randint(0, 5)
            if hurt == 0:
                print "The enemy {0} missed".format(enemy.name)
            else:
                self.engine.player.remove_health(hurt)
                print "The enemy {0} attacked and did {1} damage.".format(enemy.name, hurt, self.engine.player.hp)