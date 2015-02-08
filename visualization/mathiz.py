__author__ = 'buckbaskin'

import math
from math import cos, sin, sqrt

def cross_mag(a1,a2,a3,b1,b2,b3):
    return dist(a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)

def dist(x,y,z):
    return sqrt(x*x+y*y+z*z)

def dot_mag(a1,a2,a3,b1,b2,b3):
    return a1*b1+a2*b2+a3*b3

def dist_from_line(x0,y0,z0,x1,y1,z1,x2,y2,z2):
    x01 = x0-x1
    y01 = y0-y1
    z01 = z0-z1
    x02 = x0-x2
    y02 = y0-y2
    z02 = z0-z2
    x21 = x2-x1
    y21 = y2-y1
    z21 = z2-z1

    return cross_mag(x01,y01,z01,x02,y02,z02) / dist(x21,y21,z21)

def dist_on_line(x0,y0,z0,x1,y1,z1,x2,y2,z2):
    #v
    x21 = x2-x1
    y21 = y2-y1
    z21 = z2-z1
    #u
    x01 = x0-x1
    y01 = y0-y1
    z01 = z0-z1

    return dot_mag(x01,y01,z01,x21,y21,z21) / dist(x21,y21,z21)

def dist_sort(list, x1, y1, z1, x2, y2, z2):
    return sorted(list, key=lambda v3: dist_on_line(v3[0],v3[1],v3[2],x1,y1,z1,x2,y2,z2), reverse=True )

def test():
    pass

if __name__ == '__main__':
    x1=0
    y1=0
    z1=0

    x2=1
    y2=0
    z2=0
    print 'go'
    l = [ (1,1,0) , (2,0,1) , (.5,-1,0) ]
    print str(l)
    l = dist_sort(l,x1,y1,z1,x2,y2,z2)
    print str(l)