__author__ = 'buckbaskin'

from graphics import *
from mathiz import locate, size, dist_sort
from math import sin, cos
from random import uniform
from visualization.NetViz import *
from leap_motion.location_sim import *
from leap_motion.simple_motion import *


def main():
    win = GraphWin("My 3D view", 1920, 1080)
    shift_x = 1920 / 2
    shift_y = 1080 / 2
    m2pix = 1920 / 8

    stopper = 8
    screen_distance = 1
    # (start_x, start_y, start_theta, start_v, start_w, start_pitch, start_roll)
    lsim = LeapSimulator(4, 4, -2.356, -.735, 0.0, 0.0, 0.0)

    controller = Leap.Controller()

    # self , x, y, z, theta, pitch, screen_distance, sim_hook
    v = Viewer(screen_distance, win, shift_x, shift_y, m2pix, lsim)

    obs = []

    for i in range(0, 50):
        obs.append(ViewNode(rand_location_gen(stopper), rand_location_gen(stopper), rand_location_gen(stopper), 0.1, v))

    for obj in obs:
        #print 'object '+str(obj)
        pass

    for obj in obs:
        obj.draw(win)

    print 'create vn'
    vn = ViewNode(rand_location_gen(stopper), rand_location_gen(stopper), rand_location_gen(stopper), 0.1, v)
    vn.draw(win)
    print 'draw vn '+str(vn)

    x_axis = Line(Point(.4 * (2 * shift_x), shift_y), Point(.6 * (2 * shift_x), shift_y))
    x_scale = Line(Point(shift_x + m2pix, shift_y - 20), Point(shift_x + m2pix, shift_y + 20))
    y_axis = Line(Point(shift_x, .4 * (2 * shift_y)), Point(shift_x, .6 * (2 * shift_y)))

    x_axis.setOutline('black')
    x_scale.setOutline('black')
    y_axis.setOutline('black')

    x_axis.draw(win)
    x_scale.draw(win)
    y_axis.draw(win)

    print 'animate'
    ### Update and run forward ###
    '''
    while (True):
        try:
            print 'update'
            lsim.update(controller)
            v.update()
            for obj in obs:
                obj.update(win)
        except Exception as e:
            print str(e)
            print 'error'
            raise e
        time.sleep(.01)'''



    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


if __name__ == '__main__':
    main()