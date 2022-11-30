class Animal:
    def __init__(self, fur, species, clas, color):

        self.fur = fur
        self.species = species
        self.clas = clas
        self.color = color

    def getFur(self):
        return self.fur

    def getSpecies(self):
        return self.species
    
    def getClasification(self):
        return self.clas
    
    def getColor(self):
        return self.color

    def setFur(self, red):
        self.Fur = red


def main():
    pan1 = Animal("white", "mammal", "black and white panda", "tan")
    pan2 = Animal("white", "mammal", "red panda", "red")

    print(pan1.getFur())
    print(pan1.getSpecies())
    print(pan2.getClasification())
    print(pan2.getColor())
    pan2.setFur("red")
    print(pan2.getFur())
  

if __name__ == "__main__":
    main ()
