__author__ = 'buckbaskin'

import os, sys, inspect, thread, time
import datetime
import math
from math import cos, sin, tan, atan2
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

class LeapSimulator(object):

    def __init__(self, start_x, start_y, start_theta, start_pitch, start_v, start_w, start_roll):
        #           [ 0        1        2           3              4        5       6           ]
        self.state = [start_x, start_y, start_theta, start_pitch, start_v, start_w, start_roll]

        #controller
        self.last_frame = None
        self.this_frame = None
        self.last_v = 0.0
        self.last_w = 0.0
        self.last_r = 0.0

        self.last_time = datetime.datetime.now()
        self.this_time = datetime.datetime.now()

    def update_frames(self, zero, one):
        self.this_frame = zero
        self.last_frame = one

    def update_cmd(self):
        # calculated from frames
        if self.this_frame and len(self.this_frame.hands) == 2:
            hands = self.this_frame.hands

            leftmost = hands.leftmost.palm_position
            rightmost = hands.rightmost.palm_position
            print 'rightmost '+str(rightmost)
            print ' --> x: '+str(rightmost.x)+'  y: '+str(rightmost.y)+'  z: '+str(rightmost.z)
            print 'leftmost  '+str(leftmost)
            print ' --> x: '+str(rightmost.x)+'  y: '+str(rightmost.y)+'  z: '+str(rightmost.z)
            print 't? '+str(not abs(leftmost.x))
            if ((abs(leftmost.x) or abs(leftmost.y) or abs(leftmost.z)) and ( abs(rightmost.x) or abs(rightmost.y) or abs(rightmost.x))):
                print str(len(self.this_frame.hands))+ ' hands visible'
                print 'L x: '+str(leftmost.x)+' y: '+str(leftmost.y)+' z: '+str(leftmost.z)
                print 'R x: '+str(rightmost.x)+' y: '+str(rightmost.y)+' z: '+str(rightmost.z)
                print '\n\n'
                self.last_v = .0125 * (-rightmost.z-leftmost.z)*.5
                #print '|v|'
                self.last_w = .4 * (rightmost.z-leftmost.z)*(1.0/self.xzdist(leftmost, rightmost))

                if (abs(self.last_v) < .1):
                    self.last_v = 0.0
                if (abs(self.last_w) < .03):
                    self.last_w = 0.0

                #print '|w|'
                self.last_r = 0.0
                #print '|r|'
        else:
            self.last_v = 0.0
            self.last_w = 0.0
            self.last_r = 0.0
        #print '|'
        print '( v w r ) ( '+str(self.last_v)+' '+str(self.last_w)+' '+str(self.last_r)+' )'


    def xzdist(self, l_palm, r_palm):
        print 'xzdist'
        print 'lpalm '+str(l_palm)
        dx = l_palm.x-r_palm.x
        print 'dx'
        dz = l_palm.z-r_palm.z
        print 'dz'
        return math.sqrt( dx * dx + dz * dz)

    def update_state(self):
        self.this_time = datetime.datetime.now()
        dt = (self.this_time-self.last_time).total_seconds()
        new_s =  [None]*7
        new_s[0] = self.state[0]+cos(self.state[2])*self.state[4]*dt
        new_s[1] = self.state[1]+sin(self.state[2])*self.state[4]*dt
        new_s[2] = self.state[2]+self.state[5]*dt
        new_s[3] = max(-1, min(1, self.state[3]+self.state[6]*dt)) #bounded to 1 to -1 radians
        new_s[4] = self.last_v
        new_s[5] = self.last_w
        new_s[6] = self.last_r
        self.last_time = datetime.datetime.now()

    def update(self, controller):
        self.update_frames(controller.frame(), controller.frame(1))
        self.update_cmd()
        self.update_state()

    def state(self):
        return self.state

class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        print 'on frame'
        if self.simulator:
            self.simulator.this_frame = controller.frame()
            self.simulator.last_frame = controller.frame(1)
        #print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d" % ...
        # (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools))


def main():
    #def        __init__(start_x, start_y, start_theta, start_v, start_w, start_pitch, start_roll):
    lsim = LeapSimulator(0.0    , 0.0    , 0.0        , 0.0    , 0.0    , 0.0        , 0.0)

    controller = Leap.Controller()

    while(True):
        try:
            print 'update'
            lsim.update(controller)
        except Exception as e:
            print str(e)
            print 'error'
            raise e
        time.sleep(.1)


if __name__ == '__main__':
    main()