__author__ = 'buckbaskin'

from graphics import *
from mathiz import locate, size, dist_sort
from math import sin, cos
from random import uniform

def main():
    win = GraphWin("My 3D view", 1920, 1080)
    stopper = 8
    points = [None]*50
    for i in range(0,len(points),1):
        points[i] = tuple([uniform(-stopper/2,stopper/2),uniform(-stopper/2,stopper/2),uniform(-stopper/2,stopper/2)])
    print 'points: '+str(points)
    r = (3,3,3)
    theta = -2.356
    pitch = -0.735
    r1 = (sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch))
    screen_distance = 1
    shift_x = 1920/2
    shift_y = 1080/2
    m2pix = 1920/8
    scalar = 10000

    points = dist_sort(points, r, r1)
    locs = [locate(p,r,theta,pitch,screen_distance) for p in points]
    for loc in locs:
        loc = (m2pix*scalar*loc[0]+shift_x,m2pix*scalar*loc[1]+shift_y)
    print 'locs: '+str(locs)
    actual_size = 0.10

    loc = locate((2,-1,0.25),r,theta,pitch,screen_distance)
    #print 'loc: '+str(loc)
    depth_y = Line(Point(shift_x+m2pix,shift_y),
                   Point(m2pix*loc[0]+shift_x,
                         m2pix*loc[1]+shift_y))

    print 'list comprehension'
    # S = [x**2 for x in range(10)]
    circles = [Circle(Point(shift_x+m2pix*locate(point,r,theta,pitch,screen_distance)[0],
                            shift_y+m2pix*locate(point,r,theta,pitch,screen_distance)[1]),
                      m2pix*size(actual_size,point,r,theta,pitch,screen_distance)) for point in points]
    print 'list comprehension complete'
    count = 0
    for c in circles:
        c.setFill('orange')
        c.draw(win)
        count = count + 1
        print count


    print 'done with circles loop'

    x_axis = Line(Point(.4*(2*shift_x),shift_y) , Point(.6*(2*shift_x),shift_y))
    x_scale = Line(Point(shift_x+m2pix,shift_y-20), Point(shift_x+m2pix,shift_y+20))
    y_axis = Line(Point(shift_x,.4*(2*shift_y)) , Point(shift_x,.6*(2*shift_y)))

    x_axis.setOutline('black')
    x_scale.setOutline('black')
    y_axis.setOutline('black')
    depth_y.setOutline('black')

    x_axis.draw(win)
    x_scale.draw(win)
    y_axis.draw(win)
    depth_y.draw(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

if __name__=='__main__':
    main()