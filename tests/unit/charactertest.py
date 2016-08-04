import unittest
from characters import *
from items import *

class playertest(unittest.TestCase):

    def test_add_health_below_max(self):
        testPlayer = player(10, 10, [], "test");
        testPlayer.add_health(5)
        self.assertEquals(testPlayer.hp, 15)

    def test_add_health_above_max(self):
        # Can't really test this
        return

    def test_remove_gold(self):
        testPlayer = player(10, 10, [], "test");
        testPlayer.remove_gold(5)
        self.assertEquals(testPlayer.gold, 5)

    def test_add_gold(self):
        testPlayer = player(10, 10, [], "test");
        testPlayer.add_gold(5)
        self.assertEquals(testPlayer.gold, 15)
        return

    def test_get_status(self):
        testPlayer = player(10, 10, [], "test");
        expected = ("*" * 10,
               str("test") + " Level " + str(1),
               "Status:",
               "Current HP: " + str(10) + "/" + str(20),
               "Current Gold: " + str(10),
               "Current XP: " + str(0),
               "*" * 10)
        actual = testPlayer.get_status()
        self.assertEquals(actual, expected)

    def test_xp_up_without_level_up(self):
        testPlayer = player(10, 10, [], "test");
        testPlayer.xp_up(10)
        self.assertEquals(testPlayer.xp, 10)

    def test_xp_up_level_up(self):
        testPlayer = player(10, 10, [], "test");
        testPlayer.xp_up(100)
        self.assertEquals(testPlayer.xp, 0)
        self.assertEquals(testPlayer.level, 2)
        self.assertGreater(testPlayer.max_hp, 20)
        self.assertGreater(testPlayer.attack, 5)
        self.assertGreater(testPlayer.defense,  5)
        self.assertGreater(testPlayer.speed, 5)

    def test_use_cons(self):
        testPlayer = player(10, 10, [], "test")
        potion = consumable('Potion', 1, 10, 10)
        testPlayer.inv.add_item(potion)
        self.assertEquals(testPlayer.inv.get_item('Potion'), potion)
        testPlayer.use_cons(potion)
        self.assertEquals(testPlayer.inv.get_item('Potion'), None)
        self.assertEquals(testPlayer.hp, 20)

class enemytest(unittest.TestCase):

    def test_remove_health(self):
        testEnemy = enemy("test", 10, 10, 10)
        testEnemy.remove_health(5)
        self.assertEquals(testEnemy.hp, 5)

    def test_remove_gold(self):
        testEnemy = enemy("test", 10, 10, 10)
        testEnemy.remove_gold(5)
        self.assertEquals(testEnemy.gold, 5)

    def test_get_status(self):
        testEnemy = enemy("test", 10, 10, 10)
        expected = ("*" * 10,
               "test",
               "Status:",
               "Current HP: " + str(10),
               "*" * 10)
        actual = testEnemy.get_status()
        self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()
