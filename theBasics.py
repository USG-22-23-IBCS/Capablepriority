def csClass():
    print("I enjoy coding")
    print("Not sarcastic")

def bioclass(name):
    happy = True
    study = False
    return name + str(happy) 
    


# main methods are useful for holding information 
def main():

    # data types and their uses

    #String
    name = "yuliia"
    name2 = "Jenny"
    name3= "Anna is in computer science class"
    #characters can be accesed through index
    print(name[0]) #-this would print y
    print(name2[3])

    #print(name[10]) #-syntax error out of the range of the name, range = 5
    print(name2[0:3]) 
    print(name3[1:]) #the semi collon makes it go from the 
    print(name3[::-1]) #-this reverses the string and prints it backwards

    # strings can be added together through "concatenation"
    print(name + name2)
    print(name , name2) #- not concatenation, just printing out the names
    print(name2*10) # concatentation because it will print out "Jenny" 10 times
    #String data trpes cannot beadded with integer data types
    #Sometimes it is necessary to convert the integer into a string
    x = 100 
    print(name3 + str(x))

    #Integers are number data types
    y = 40
    z = 30.5 
    z = int(z)
    print(z) #- this will print to 30 because when a float goes to an integer it will always round down 30.9 = 30
    

    #rounding
    w = 20.65678 
    print(round(w, 2))
    print(round(w, 0))
    #rounding a float up and converting to an integer
    print(int(round(w, 0)))

    #integer division
    g = 12
    print(g/5) 
    print(g/4)
    # sometimes referred to as "div" 
    print(g//4)
    print(g//5)
    #module opertor
    print(g % 5)
    # with mod, if you a=start with a float answer is gonna be float with a integer it is going to be an integer

    #Lists can have different types of data within the collection
    L = ["Leah", "Mr. Considine", 10, 2.5, True]
    print(L[0])
    print(L[4])
    # sublists can be accessed by positions [start : stop]
    subL = L[1:3]
    for element in subL:
          print(element)
    #lists can be added to other lists
    L2 = L + ["Anna" , "Mr. Phillips", False]
    print(L2)

    #nested loop
    names = ["John", "Jerry", "Wilson"]
    for n in names:
        for char in n:
            print(char)

    

    
    csClass()
    csClass()
    csClass()
          
    S = bioclass("Jenny")
    print(S)
    


    #bob = Jenny - 9
    #print(bob) 











if __name__ == "__main__":
    main()
