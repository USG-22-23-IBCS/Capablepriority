class GroceryStore:
 
    def __init__(self):

        self.items = ["banana", "orange", "clementine", "tomato", "plum", "milk","tea","cereal","pasta","eggs", "bagels", "peach", "tomato", "plum",]  
        self.Available = ["banana", "orange", "clementine", "plum", "milk","tea","cereal","pasta","eggs"]
        self.sold = ["peach", "tomato", "plum", "leak", "bagels"]

    def getItems(self):
        return self.items

    def getAvailable(self):
        return self.Available
 
    def getSold(self):
        return self.sold
       
def main():

    

    store = GroceryStore()
    
    print(store.getAvailable())

    food = {"banana" : 1.25,
                  "orange" : 0.75,
                  "apple" : 2.50,
                  "clementine" : 0.50,
                  "peach" : 1.75,
                  "tomato" : 0.75,
                  "plum" : 0.50,
                  "leak" : 0.50,
                  "milk" : 0.50,
                  "tea" : 0.50,
                  "cereal" : 2.50,
                  "pasta" : 4,
                  "eggs" : 12,
                  "bagels" : 5}
    
    foodList = list(food.keys())

    response = input("what would you like to buy?")

    userchoice = response.split()

    #print(items.get("banana", "orange", "apple", "clementine", "peach", "tomato", "plum", "leak", "milk", "tea", "cereal", "pasta", "eggs", "bagels")) 

    total  = 0

    for f in userchoice:

        total = total + food.get(f)
        print(f)

    print(total)


    #food = input("Hello, welcome to TheLimitedStockStore, please let me know if you need anything.")
    #print(store.getItems())
  


    #while true:

    #if food == "banana":
        #print(shop.getBanana())
       # Banana1 = input("1. Yes\n2. No\n> ")
 
       # if Banana == "1":
            #print(shop.getBanana())
 
       # elif Banana == "2":
           # print("Just one banana then. That'll be two dollars.")
 
   #elif drink == "2":
        # print(shop.getMilk())
        # bagel2 = input("1. Yes\n2. No\n> ")
 
        #if bagel2 == "1":
            # print(shop.getMilk())
            
         #elif bagel2 == "2":
             #print("Just one Americano then. That'll be four dollars.")
 
    #elif drink == "3":
       # print(shop.getMilk())
       # bagel3 = input("1. Yes\n2. No\n> ")
 
        #if bagel3 == "1":
          # print("Just one Bagel then. That'll be two dollars")
 
       # elif bagel3 == "2":
            #bagelplus = input("Okay, what else on the menu do you want?\n> ")
 
            #if bagelplus == "1":
                #print(shop.getBagelBlackCoffee())
 
           #elif bagelplus == "2":
                #print(shop.getBagelAmericano())
 
            #elif bagelplus == "3":
               # print(shop.getBagelBagel())
 
 
 
if __name__ == "__main__":
    main()
 
