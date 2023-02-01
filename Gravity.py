
from graphics import* 
from button import*
import time 

def main():
    
    win = GraphWin("gravity", 800, 600)
    win.setBackground("white")

    Object = Circle(Point(50,50), 10)
    Object .draw(win)

    p = Object.getCenter()
    y= p.getY()

    B = Button(win, Point(600, 200), Point (700, 300), "red", "Click me!")

    


    while y < 550:
        Object.move(0, 10)
        time.sleep(.4)

        if y < 20:
            time.sleep(.1)
            y < 70
            time.sleep(4)
            

        elif y < 200:
            time.sleep(5)
        




        #y = Object.getCenter().getY()

    

    



if __name__ == "__main__":
    main()
    

  

    #while C != Circle(Point(400,500), 20):
        
