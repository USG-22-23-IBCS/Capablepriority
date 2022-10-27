import random

class House:

    def __init__(self):
        self.rating = random.randint(1,10)

    def getRating(self):
        return self.rating

def randPath(m, num):
    #create an empty path
    p = []

    #try to add coordinates to the path
    #if the path were to get stuck or be 'unfinished' in anyway, try again
    #only finish once a fair path is generated
    while (len(p) < num):
        p = []


        x = random.randint(0,4)
        y = random.randint(0,4)
        pVal = m[x][y]
        p.append([x,y])


        #keep track of the value of the path
        #choose a random coordinate to start at



        #add neighbors to the path at a randomly chosen direction
        #keep track of whether we get stuck. If we get stuck, break
        for i in range(num - 1):

            neighbors = [[x+1, y], [x-1, y], [x, y+1], [x,y-1]]
            bad = []

            for n in neighbors:
                if (n[0] > 4) or (n[0] < 0):
                        bad.append(n)
                elif (n[1]  > 4) or (n[1] < 0):
                         bad.append(n)
                elif n in p:
                         bad.append(n)

            for b in bad:
                neighbors.remove(b)

            if len(neighbors) == 0:
                break 

            nextHouse = random.choice(neighbors)
            p.append(nextHouse)
            x = nextHouse[0]
            y = nextHouse[1]
            pVal = pVal + m[x][y]



                
    return pVal, p
                        
                
  
def main():



    
    m = [[], [], [], [], []]
    for l in m:
        for i in range(5):
            h = House()
            l.append(h.getRating())

    for i in range(5):
        print(m[0][i], m[1][i], m[2][i], m[3][i], m[4][i]) 

    num = int(input("How many houses?\n"))


    ''' Greedy Path Call '''
    #pVal, p = greedyPath(m, num)

    #print(p)



    ''' Random Path Call '''

    total = 0
    for i in range(5):
        for j in range(5):
            total = total + m[i][j]

    average = total/25

    pVal, p = randPath(m, num)

    while (average > pVal/num):
        pVal, p = randPath(m,num)

    print(p)

    print("The average value in the path is: " + str(pVal/num))
    print("the average value in the neighborhood" +str(average))
    


    
    #while the average of value of the house is greater than the
    #average of the path randomly chosen, try getting another random
    #path. stop, once it is better, and print it.


            

        

if __name__ == "__main__":
    main()

