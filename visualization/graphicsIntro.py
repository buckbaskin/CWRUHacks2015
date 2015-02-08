__author__ = 'buckbaskin'
from graphics import *

def main():
    win = GraphWin("My Circle", 1920, 1080)
    c = Circle(Point(50,50), 10)
    c._move(1,1)
    c.setFill('blue')
    c.draw(win)

    c2 = Circle(Point(100,100), 6)
    c2.setFill('blue')
    c2.draw(win)

    line = Line(Point(50,50) , Point(100,100))
    line.setOutline('red')
    line.draw(win)


    win.getMouse() # Pause to view result
    win.close()    # Close window when done

if __name__=='__main__':
    main()