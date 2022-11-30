class Coffeeshop:
 
    def __init__(self):
        self.blackCoffee = "One Black Coffee... Would you like a bagel with that?\n> "
        self.blackCoffeeBagel = "Black Coffee and Bagel. Okay, that'll be four dollars."
        self.americano = "One Americano... Would you like a bagel with that?\n> "
        self.americanoBagel = "Americano and Bagel. Okay, that'll be six dollars."
        self.bagel = "Just a Bagel?"
        self.menu = "1. Black Coffee\n2. Americano\n3. Bagel"
        self.bagelBlackCoffee = "One Bagel and Black Coffee. Okay, that'll be four dollars."
        self.bagelAmericano = "One Bagel and Americano. Okay, that'll be six dollars."
        self.bagelBagel = "...Two bagels? Okay... that'll be four dollars."
 
   
 
    def getMenu(self):
        return self.menu
 
    def getBlackCoffee(self):
        return self.blackCoffee
 
    def getBlackCoffeeBagel(self):
        return self.blackCoffeeBagel
 
    def getAmericano(self):
        return self.americano
 
    def getAmericanoBagel(self):
        return self.americanoBagel
 
    def getBagel(self):
        return self.bagel
 
    def getBagelBlackCoffee(self):
        return self.bagelBlackCoffee
 
    def getBagelAmericano(self):
        return self.bagelAmericano
 
    def getBagelBagel(self):
        return self.bagelBagel
 
def main():
    shop = Coffeeshop()
 
    print("Welcome to Dutch Bros. Here is our menu.")                           
    print(shop.getMenu())
    drink = input("Please take your time and order.\n> ")
 
    if drink == "1":
        print(shop.getBlackCoffee())
        bagel1 = input("1. Yes\n2. No\n> ")
 
        if bagel1 == "1":
            print(shop.getBlackCoffeeBagel())
 
        elif bagel1 == "2":
            print("Just one Black Coffee then. That'll be two dollars.")
 
    elif drink == "2":
         print(shop.getAmericano())
         bagel2 = input("1. Yes\n2. No\n> ")
 
         if bagel2 == "1":
             print(shop.getAmericanoBagel())
            
         elif bagel2 == "2":
             print("Just one Americano then. That'll be four dollars.")
 
    elif drink == "3":
        print(shop.getBagel())
        bagel3 = input("1. Yes\n2. No\n> ")
 
        if bagel3 == "1":
            print("Just one Bagel then. That'll be two dollars")
 
        elif bagel3 == "2":
            bagelplus = input("Okay, what else on the menu do you want?\n> ")
 
            if bagelplus == "1":
                print(shop.getBagelBlackCoffee())
 
            elif bagelplus == "2":
                print(shop.getBagelAmericano())
 
            elif bagelplus == "3":
                print(shop.getBagelBagel())
 
 
 
if __name__ == "__main__":
    main()
 
