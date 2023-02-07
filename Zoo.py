#Class notes Zoo.py
#OOP

class Zoo:




    #constructor method  
    def __init__(self, name):


        self.animals = ["Snakes", "Flamingo", "Elephant",  "Penguin", "Horse", "Whale"]
        self.employees = ["Yuliia", "Me", "Mr Phillips"]
        self.name = "Point Defiance Zoo"
        self.price = 60
        self.enclosures = {1 : "Savannah",
                                  2 : "aquarium",
                                  3 : "Jungle",
                                  4: "Barn"}
        
        self.habitats = {"Snake" : 3,
                                 "Flamingo" : 1,
                                 "Elephant" : 1,
                                 "Penguin" : 2,
                                 "Horse" : 4,
                                 "Whale" : 2}

    def setPrice(self, price):
        self.price = price

        

    def getName(self):
        return self.name

    def getAnimals(self):
        return self.animals

    def addAnimal(self, animal, habitat):
        self.animals.append(animal)

        for e in self.enclosures.keys():
            h = self.enclosures.get(e)
            if h == habitat:
                self.habitats.update({animal : e})

    def getHabitat(self, animal):
        enclosure = self.habitats.get(animal)
        habitat = self.enclosures.get(enclosure)
        return habitat
    



def main():

    Z = Zoo("Point Defience Zoo")
    Z.setPrice(30)
    Z.addAnimal("Zebra", "Savannah")
    
    print(Z.getAnimals())
    print(Z.getHabitat("Zebra"))
    print(Z.getHabitat("Penguin"))
    print(Z.getName())
    















if __name__ == "__main__":
    main()
