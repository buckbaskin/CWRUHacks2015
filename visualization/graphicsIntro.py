from graphics import *

def main():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50,50), 10)
    c.draw(win)

    c._move(1,1)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

if __name__=='__main__':
    main()