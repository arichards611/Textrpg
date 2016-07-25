import unittest
from inventory import inventory
from items import *

class inventorytest(unittest.TestCase):

    def test_get_item(self):
        inv = inventory()
        potion = consumable('Potion', 1, 10, 10)
        inv.items.append(potion)
        result = inv.get_item('potion')
        self.assertEquals(result, potion)

    def test_get_item_no_item(self):
        inv = inventory()
        result = inv.get_item('potion')
        self.assertEquals(result, None)

    def test_add_item_new_item(self):
        inv = inventory()
        potion = consumable('Potion', 1, 10, 10)
        inv.add_item(potion)
        self.assertEquals(potion, inv.items[0])

    def test_add_item_duplicate_item(self):
        inv = inventory()
        potion = consumable('Potion', 1, 10, 10)
        inv.add_item(potion)
        inv.add_item(potion)
        self.assertEquals(2, inv.items[0].count)

    def test_remove_item_not_last_item(self):
        inv = inventory()
        potion = consumable('Potion', 2, 10, 10)
        inv.items.append(potion)
        inv.remove_item(potion)
        self.assertEquals(1, inv.items[0].count)

    def test_remove_item_last_item(self):
        inv = inventory()
        potion = consumable('Potion', 1, 10, 10)
        inv.items.append(potion)
        inv.remove_item(potion)
        self.assertEquals(0, len(inv.items))

if __name__ == '__main__':
    unittest.main()
