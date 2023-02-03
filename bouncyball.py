from graphics import *
from button import*
import time

def fall(C, direction):
     height = 560 - C.getCenter().getY()
     print(height)
     time = 0
     if direction == "down":
         while C. getCenter().getY() < height +40:
             time = time + .1
             v = 9.8*time
             C.move(0, v)
             
     if direction == "up":
         while C. getCenter().getY() > 560 - height*10 - 40:
            time = time + .1
            v = 9.8*time
            C.move(0, -v)

def main():
   
# Initialize the window

    win = GraphWin("Bouncing Ball with Gravity", 800, 600)
    C = Circle(Point(400, 100), 40)
    C.setFill("red")
    C.draw(win)
    win.setBackground("white")
    fall(C, "down")
    fall(C, "up")



    """"speed = 5
    gravity = 9.8




while True:
    y = ball.getCenter().getY() + speed
    if y > 550:
        speed = speed - gravity
    if speed < 1:
        break
    ball.move(0, speed)
    time.sleep(0.05)


    Text(Point(400, 300), "Bouncing Stopped").draw(win)
    win.getMouse()
    win.close()"""

if __name__ == "__main__":
    main()
    
    


