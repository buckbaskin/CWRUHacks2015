__author__ = 'buckbaskin'

import math
from math import cos, sin, sqrt

def cross_mag(a1,a2,a3,b1,b2,b3):
    return dist(a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)

def dist(x,y,z):
    return sqrt(x*x+y*y+z*z)

def dot_mag(a1,a2,a3,b1,b2,b3):
    return a1*b1+a2*b2+a3*b3

def dist_from_line(p0 , p1 ,p2 ,y0,z0,y1,z1,x2,y2,z2):
    x01 = p0[0]-p1[0]
    y01 = p0[1]-p1[1]
    z01 = p0[2]-p1[2]

    x02 = p0[0]-p2[0]
    y02 = p0[1]-p2[1]
    z02 = p0[2]-p2[2]

    x21 = p2[0]-p1[0]
    y21 = p2[1]-p1[1]
    z21 = p2[2]-p1[2]

    return cross_mag(x01,y01,z01,x02,y02,z02) / dist(x21,y21,z21)

def dist_on_line(p0,p1,p2, x1,y1,z1,x2,y2,z2):
    ''' Returns the distance along the line from p1 to p2, dist to p0
    p0-2 are tuples/triples'''
    #v
    x21 = p2[0]-p1[0]
    y21 = p2[1]-p1[1]
    z21 = p2[2]-p1[2]
    #u
    x01 = p0[0]-p1[0]
    y01 = p0[1]-p1[1]
    z01 = p0[2]-p1[2]

    return dot_mag(x01,y01,z01,x21,y21,z21) / dist(x21,y21,z21)



def dist_sort(list, p1, p2):
    '''Uses the lambda to sort the field in terms of distance along the line to p1, reversed.
    Render in order on the list for depth'''
    return sorted(list, key=lambda v3: dist_on_line(v3[0],v3[1],v3[2],p1[0],p1[1],p1[2],p2[0],p2[1],p2[2]), reverse=True )

def toTuple(x,y,z):
    return (x,y,z)

def test():
    pass

if __name__ == '__main__':
    p1 = (0,0,0)
    p2 = (1,0,0)

    print 'go'
    l = [ (1,1,0) , (2,0,1) , (.5,-1,0) ]
    print str(l)
    l = dist_sort(l,p1,p2)
    print str(l)

#255