__author__ = 'buckbaskin'

from graphics import *
from mathiz import locate, size, dist_sort
from math import sin, cos
from random import uniform
import copy

### UTILS ###
def rand_location_gen( stopper ):
    return uniform(-stopper/2,stopper/2)

class ViewNode(object):
    def __init__(self, x, y, z, radius, viewer):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.viewer = viewer
        self.xy = locate(self.location_tup(), viewer.location_tup(), viewer.theta, viewer.pitch, viewer.sd)
        self.apparent_size = size(self.radius, self.location_tup(), viewer.location_tup(), viewer.theta, viewer.pitch, viewer.sd)
        self.shape = Circle(Point(viewer.shift_x+viewer.m2pix*x,viewer.shift_y+viewer.m2pix*y),radius)

    def __str__(self):
        return '[VN:'+str(self.xy)+' sz:'+str(self.apparent_size)+']'

    def shape(self):
        return self.shape

    def draw(self, window):
        self.shape.draw(window)

    def update(self, window):
        old_xy = copy.copy(self.xy)
        self.xy = locate(self.location_tup(), self.viewer.location_tup(), self.viewer.theta,
                         self.viewer.pitch, self.viewer.sd)
        dx = (self.xy[0]-old_xy[0] , self.xy[1]-old_xy[1])
        self.apparent_size = size(self.radius, self.location_tup(), self.viewer.location_tup(),
                                  self.viewer.theta, self.viewer.pitch, self.viewer.sd)
        self.shape.radius = self.apparent_size
        self.shape.move(self.viewer.m2pix*dx[0],self.viewer.m2pix*dx[1])


    def location_tup(self):
        return (self.x, self.y, self.z)


class Viewer(object):
    def __init__(self , screen_distance, window, shift_x, shift_y, m2pix, sim_hook):
        self.x = sim_hook.state[0]
        self.y = sim_hook.state[1]
        self.z = 0.0
        self.theta = sim_hook.state[2]
        self.pitch = sim_hook.state[3]
        self.sd = screen_distance
        self.simulator = sim_hook
        self.window = window
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.m2pix = m2pix

    def location_tup(self):
        return (self.x, self.y, self.z)

    def update(self):
        self.x = self.simulator.state[0]
        self.y = self.simulator.state[1]
        self.z = 0.0
        self.theta = self.simulator.state[2]
        self.pitch = self.simulator.state[3]