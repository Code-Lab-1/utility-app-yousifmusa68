# making a class for the vending machine item
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0: # In the absence of any available items
            # not raise item exception
            pass
        self.stock -= 1 # or else the item's stock drops by one.

# make a class for the actual vending machine
class VendingMachine:

    def __init__(self):
        self.amount = 0   
        self.items = [] # make a class for the actual vending machine.

    def addItem(self, item):
        self.items.append(item) # way to add anything to a vending machine

    # the process of displaying the commodities in the vending machine
    def showItems(self):
        print('\nitems available \n***************')

        for item in self.items: # for each item in this vending machine
            if item.stock == 0: # if the stock of this item is 0
                self.items.remove(item) # remove this item from being displayed
        for item in self.items:
            print(item.name + ": " "AED", item.price) # the procedure for putting goods on display in the vending machine

        print('***************\n')

    def addCash(self, money):
        self.amount = self.amount + money # add money

    def buyItem(self, item): # if the amount you put is less than the price
        if self.amount < item.price:
            print('You can\'t buy this item. Insert more coins.') # then obvs you cant buy this item
        else:
            self.amount -= item.price # subtract item price from available cash
            item.buyFromStock() # the steps involved in displaying goods in a vending machine
            # (What if we purchase additional ones?)
            print('You got ' +item.name)
            print('Cash remaining: ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret

    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
                self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(str(self.amount) + " refunded.")
            self.amount = 0

        print('Thank you, have a nice day!\n')


def vend():

    machine = VendingMachine()
    item1 = Item('chips',  1,  2)
    item2 = Item('pepsi', 1.50,  1)
    item3 = Item('kitkat',  2.0,  3)
    item4 = Item('apple guice',  3.50, 1)
    item5 = Item('coffee',4,  3)
    item6 = Item('tea',1.2, 5 )
    machine.addItem(item1)
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)
    machine.addItem(item5)
    machine.addItem(item6)

    print('Welcome to the vending machine!\n***************')

    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('select item: ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('buy something else? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Item not available. Select another item.')
            continue

vend()