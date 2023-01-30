



from graphics import *
from button import*


        

def main():

 
    win = GraphWin("madlibs", 800, 600)

    label = Text(Point(200, 80), 'Adjective')
    label.draw(win)
    label = Text(Point(200, 180), '2nd Noun')
    label.draw(win)
    label = Text(Point(200, 280), "verb")
    label.draw(win)
    label = Text(Point(200, 380), 'Adjective')
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

    if Q.isClicked():
        win.close()



    while True:

        m = win.getMouse()

        if B.isClicked(m):
            noun = N.getText()
            noun2 = N2.getText()
            verb = V.getText()
            adj = A.getText()
            excl = E.getText()
            print(adj + " " + noun + " and " + noun2 + " " + verb + " " + excl)

        if Q.isClicked():
            win.close()



if __name__ == "__main__":
    main()



#how to I just make the button do the closing?


#make it so the print goes to the GUI 

    

