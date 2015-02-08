__author__ = 'buckbaskin'

import math
from math import cos, sin, sqrt

def cross_mag(a1,a2,a3,b1,b2,b3):
    tup = cross_tup(a1,a2,a3,b1,b2,b3)
    return dist(tup[0], tup[1], tup[2])

def cross_tup(a1,a2,a3,b1,b2,b3):
    return toTuple(a2*b3-a3*b2, a3*b1-a1*b3, a1*b2-a2*b1)

def dist(x,y,z):
    return sqrt(x*x+y*y+z*z)

def dot_mag(a1,a2,a3,b1,b2,b3):
    return a1*b1+a2*b2+a3*b3

def dist_from_line(p0 , p1 ,p2 ,y0,z0,y1,z1,x2,y2,z2):
    '''dist of point 0 from line p1-p2'''
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

def dist_on_line(p0,p1,p2):
    ''' Returns the distance along the line from p1 to p2, dist to p0
    p0-2 are tuples/triples'''
    #print 'dist on line'
    #v
    x21 = p2[0]-p1[0]
    y21 = p2[1]-p1[1]
    z21 = p2[2]-p1[2]
    #print '21: '+str( (x21,y21,z21) )
    #u
    x01 = p0[0]-p1[0]
    y01 = p0[1]-p1[1]
    z01 = p0[2]-p1[2]
    #print '01: '+str( (x01,y01,z01) )

    return dot_mag(x01,y01,z01,x21,y21,z21) / dist(x21,y21,z21)

def dist_sort(list, p1, p2):
    '''Uses the lambda to sort the field in terms of distance along the line to p1, reversed.
    Render in order on the list for depth'''
    return sorted(list, key=lambda v3: dist_on_line(v3,p1,p2), reverse=True )

def toTuple(x,y,z):
    return (x,y,z)

### API ###

def locate(p,r,theta,pitch, screen_distance):
    '''locate point p on screen given robot x,y,z (collectively r),theta,pitch, distance'''
    y_unit = cross_tup(sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch),p[0]-r[0],p[1]-r[1],r[2]-p[2])
    y_unit = (y_unit[0] / dist(y_unit[0],y_unit[1],y_unit[2]) , y_unit[1] / dist(y_unit[0],y_unit[1],y_unit[2]) , y_unit[2] / dist(y_unit[0],y_unit[1],y_unit[2]))
    z_unit = cross_tup(sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch),0,0,1)
    x_unit = cross_tup(y_unit[0],y_unit[1],y_unit[2],z_unit[0],z_unit[1],z_unit[2])

    w = tuple( [ p[0] - r[0] , p[1] - r[1] , p[2] - r[2] ] )
    xy = (dot_mag(w[0],w[1],w[2],x_unit[0],x_unit[1],x_unit[2]), dot_mag(w[0],w[1],w[2],y_unit[0],y_unit[1],y_unit[2]))
    # return (x,y)
    xy = (xy[0]*screen_distance/dist_on_line(p,r,(r[0]+z_unit[0],r[1]+z_unit[1],r[2]+z_unit[2])), xy[1]*screen_distance/dist_on_line(p,r,(r[0]+z_unit[0],r[1]+z_unit[1],r[2]+z_unit[2])))

    return xy

def size(actual, p, r, theta, pitch, screen_distance):
    z_unit = cross_tup(sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch),0,0,1)
    print 'dist_on_line for size: '+str(dist_on_line(p,r,(r[0]+z_unit[0],r[1]+z_unit[1],r[2]+z_unit[2])))
    return actual*screen_distance/dist_on_line(p,r,(r[0]+z_unit[0],r[1]+z_unit[1],r[2]+z_unit[2]))


def test_tup():
    a = (1,2,3)
    b = (1,1,1)
    print a-b

def viz_test():
    print 'viz (0,0,0)0,0 -> (4,3,)'
    r = (0,0,0)
    p = (4,3,0)
    theta = 0
    pitch = 0
    screen_distance = 2
    actual_size = 1

    y_unit = cross_tup(sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch),p[0]-r[0],p[1]-r[1],r[2]-p[2])
    y_unit = (y_unit[0] / dist(y_unit[0],y_unit[1],y_unit[2]) , y_unit[1] / dist(y_unit[0],y_unit[1],y_unit[2]) , y_unit[2] / dist(y_unit[0],y_unit[1],y_unit[2]))
    z_unit = cross_tup(sin(theta)*cos(pitch),cos(theta)*cos(pitch),sin(pitch),0,0,1)
    x_unit = cross_tup(y_unit[0],y_unit[1],y_unit[2],z_unit[0],z_unit[1],z_unit[2])
    print 'xt: '+str(x_unit)
    print 'yt: '+str(y_unit)
    print 'zt: '+str(z_unit)
    print 'dist on line --> '+str(dist_on_line(p,r,(r[0]+z_unit[0],r[1]+z_unit[1],r[2]+z_unit[2])))
    print 'locate() --> '+str(locate(p,r,theta,pitch,screen_distance))
    print 'size() -->   '+str(size(actual_size,p,r,theta, pitch, screen_distance))

def cross_test():
    print 'cross'
    print cross_tup(0,1,0,1,.75,0)

def test():
    p1 = (0,0,0)
    p2 = (1,0,0)

    print 'go'
    l = [ (1,1,0) , (2,0,1) , (.5,-1,0) ]
    print str(l)
    l = dist_sort(l,p1,p2)
    print str(l)

if __name__ == '__main__':
    #test_tup()
    #test()
    viz_test()
    #cross_test()


#255