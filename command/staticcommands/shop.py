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
                shopinv = ["Potion"]
                print ("Items for sale are: {0}").format(shopinv)
                buytem = raw_input("What would you like to buy?: ")
                buytem = buytem.lower()
                if buytem == ('potion'):
                    potion = items.consumable('Potion', 1, 10, 10)
                    self.assetContainer.player.inv.add_item(potion)
                    self.assetContainer.player.remove_gold(potion.cost)
                    print "You bought one {0} for {1} gold.".format(potion.name, potion.cost)
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