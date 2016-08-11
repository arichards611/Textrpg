import items

class shop(object):

    def __init__(self, assetContainer):
        self.assetContainer = assetContainer

    def execute(self):
        shop = True
        while shop:
            option = raw_input("Welcome. What would you like to do? [Buy, Sell, Exit]: ")
            option = option.lower()
            if option == "buy":
                shopinv = ["Potion", "Wood Sword"]
                print ("Items for sale are: {0}").format(shopinv)
                buytem = raw_input("What would you like to buy?: ")
                buytem = buytem.lower()

                if buytem == ('potion'):
                    potion = items.consumable('Potion', 1, 10, 10)
                    quantity = raw_input("How many would you like to buy?: ")
                    current = 0
                    if quantity.isalnum():
                        if quantity >= "1":
                            cost = potion.cost * int(quantity)
                            if self.assetContainer.player.gold < cost:
                                print "You don't have enough gold to buy that!"
                            else:
                                while current < int(quantity):
                                    self.assetContainer.player.inv.add_item(potion)
                                    current += 1
                                self.assetContainer.player.remove_gold(cost)
                                print "You bought {0} {1} for {2} gold.".format(quantity, potion.name, cost)
                        else:
                            print "You can't buy 0 of an item."
                    else:
                        print "You can only enter numbers."

                elif buytem == ('wood sword'):
                    sword = items.weapon('Wood Sword', 1, 5, 50, 2)
                    if self.assetContainer.player.gold < sword.cost:
                        print "You don't have enough gold to buy that!"
                    else:
                        self.assetContainer.player.inv.add_item(sword)
                        self.assetContainer.player.remove_gold(sword.cost)
                        print "You bought {0} for {1} gold.".format(sword.name, sword.cost)

            elif option == "sell":
                if self.assetContainer.player.inv.items == []:
                    print "You have no items to sell."
                else:
                    print ""
                    print self.assetContainer.player.inv
                    print ""
                    sell = raw_input("What would you like to sell? ")
                    sell = sell.lower()
                    for item in self.assetContainer.player.inv.items:
                        if item.name.lower() == sell:
                            self.assetContainer.player.inv.remove_item(item)
                            self.assetContainer.player.add_gold(item.cost)
                            print "You sold one {0} for {1} gold.".format(item.name, item.cost)
            elif option == "exit":
                shop = False
            else:
                "That is not a valid choice."