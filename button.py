Python 3.10.3 (v3.10.3:a342a49189, Mar 16 2022, 09:34:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

from graphics import *

class Button(Rectangle):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(p1, p2)
        super().draw(win)
        super().setFill(color)

        self.minX = p1.getX()
        self.maxX = p2.getX()
        self.minY = p1.getY()
        self.maxY = p2.getY()

        self.text = Text(Point((self.minX + self.maxX)/2, (self.minY + self.maxY)/2), text)
        self.text.draw(win)

    def isClicked(self, p):
        x = p.getX()
        y = p.getY()
        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True
        return False

class QuitButton(Button):

    def __init__(self, win, p1, p2, color = "red", text = "Quit"):
        super().__init__(win, p1, p2, color, text)




