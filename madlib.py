
from graphics import *
from button import*


        

def main():

 
    win = GraphWin("madlibs", 800, 600)

    label = Text(Point(200, 80), "Noun")
    label.draw(win)
    label = Text(Point(200, 180), 'Adjective')
    label.draw(win)
    label = Text(Point(200, 280), "Noun2")
    label.draw(win)
    label = Text(Point(200, 380), 'Verb')
    label.draw(win)
    label = Text(Point(200, 480), 'Exclemation')
    label.draw(win)
  

    N = Entry(Point(200,100), 20)
    N.draw(win)

    N2 = Entry(Point(200,200), 20)
    N2.draw(win)

    V = Entry(Point(200,300), 20)
    V.draw(win)

    A = Entry(Point(200,400), 20)
    A.draw(win)

    E = Entry(Point(200,500), 20)
    E.draw(win)

    B = Button(win, Point(400, 450), Point(520, 550), "tomato", "Print")

    Q = Button(win, Point(400,350), Point(520, 450), 'tomato', "Quit")
       




    while True:

        

        m = win.getMouse()

        if Q.isClicked(m):
            win.close()
            break

        if B.isClicked(m):
            noun = N.getText()
            noun2 = N2.getText()
            verb = V.getText()
            adj = A.getText()
            excl = E.getText()
            #print(noun + " " + adj + " " + noun2 + " " + verb + " " + excl)

            Story = Text(Point(500, 200), noun + "was a very " + adj + " dog who always played with a " + noun2 + "he always loved to" + verb + "The end." + excl)
            Story. draw(win)
            

    

        



if __name__ == "__main__":
    main()



#how to I just make the button do the closing?


#make it so the print goes to the GUI 

    

