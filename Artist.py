import Turtlefinal

class Artist:

    def __init__(self, t):
        self.t = t
    
    def triangle(self, size = 100):
        for i in range(3):
            self.t.right(120)
            self.t.forward(size)

    def move(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def square(self, size = 100):
        for i in range(4):
            self.t.right(90)
            self.t.forward(size)

    def pentagon(self, size = 50):
        for i in range(6):
            self.t.right(60)
            self.t.forward(size)

    def star(self, size = 30):
        for i in range(5):
            self.t.right(144)
            self.t.forward(size)

    def circle(self, size = 1):
        for i in range(360):
            self.t.right(1)
            self.t.forward(size)

    def pattern(self, size = 20):
        for i in range(4):
            for i in range(3):
                self.t.left(90)
                self.t.forward(size)
            for i in range(3):
                self.t.right(90)
                self.t.forward(size)
            for i in range(3):
                self.t.left(90)
                self.t.forward(size)
            for i in range(3): 
                self.t.right(90)
                self.t.forward(size)

    def diamond(self, size = 30):
        for i in range(8):
            self.t.right(45)
            self.t.forward(size)
        
        
            

            


def main():
    canvas = Turtlefinal.Screen()
    canvas.bgcolor("purple")
    canvas.title("Turtle Example")
    t = Turtlefinal.Turtle()
    t.shape("turtle")
    t.speed(100)
    art = Artist(t)

    art.triangle()
    art.move(150,200)
    art.triangle(200)
    art.move(-150, 200)

    art.square()
    art.move(120,300)

    art.pentagon()
    art.move(300,200)

    art.star()
    art.move(20,20)

    art.circle()
    art.move(-100,-100)

    art.pattern()
    art.move(150,- 200) 

    art.diamond()
    art.move(200,200) 


  

   

    
    

    
    
    
    


if __name__ == "__main__":
    main()
