from graphics import *

import time

# Initialize the window
win = GraphWin("Bouncing Ball with Gravity", 800, 600)


ball = Circle(Point(400, 100), 20)
ball.setFill("red")
ball.draw(win)
win.setBackground("white")

speed = 1
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
win.close()


