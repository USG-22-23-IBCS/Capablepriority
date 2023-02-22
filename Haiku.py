import random



def main():


    
    file1 = open("oneSyllable.txt")
    file2 = open("twoSyllable.txt")
    file3 = open("threeSyllable.txt")
    file4 = open("fourSyllable.txt")
    contents1 = file1.read()
    contents2 = file2.read()
    contents3 = file3.read()
    contents4 = file4.read()
    List1 = contents1.split()
    List2 = contents2.split()
    List3 = contents3.split()
    List4 = contents4.split()
    print(random.choice(List1), random.choice(List4))
    print(random.choice(List2), random.choice(List3), random.choice(List3))
    print(random.choice(List2), random.choice(List2), random.choice(List1))
    

    
 



  

if __name__ == "__main__":
    main ()


