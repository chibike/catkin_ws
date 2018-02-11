#!/usr/bin/env python

import math
import numpy as np
from pi_dtypes import *
import matplotlib.pyplot as plt

def sinf(x):
    return math.sin(math.radians(x))

def cosf(x):
    return math.cos(math.radians(x))

def tanf(x):
    return math.tan(math.radians(x))

def asinf(x):
    return math.degrees(math.asin(x))

def acosf(x):
    return math.degrees(math.acos(x))

def atanf(x):
    return math.degrees(math.atan(x))

def get_distance_bwt_points(point_1, point_2):
    distance = math.sqrt(pow(point_2.x - point_1.x, 2) + pow(point_2.y - point_1.y, 2))
    return distance

def plot(title, x, y):
    plt.title(title)
    plt.plot(x, y)
    plt.grid()
    plt.show()

def rotate_about_the_origin(point, angle):
    x = round((point.x*cosf(angle)) - (point.y*sinf(angle)), 3)
    y = round((point.y*cosf(angle)) + (point.x*sinf(angle)), 3)
    return Point(x, y)

def get_intersecting_point(l1, l2):
    def _det(x):
        '''returns the determinant of x'''
        return np.linalg.det(x)
    
    #Line 01
    x1 = l1.start.x; x2 = l1.end.x
    y1 = l1.start.y; y2 = l1.end.y

    #Line 02
    x3 = l2.start.x; x4 = l2.end.x
    y3 = l2.start.y; y4 = l2.end.y
    
    a = np.array([[x1, y1], [x2, y2]])
    b = np.array([[x1,  1], [x2,  1]])
    c = np.array([[x3, y3], [x4, y4]])
    d = np.array([[x3,  1], [x4,  1]])
    e = np.array([[y1,  1], [y2,  1]])
    f = np.array([[y3,  1], [y4,  1]])

    A = np.array([[_det(a), _det(b)], [_det(c), _det(d)]])
    B = np.array([[_det(b), _det(e)], [_det(d), _det(f)]])

    x = _det(A)/_det(B)

    C = np.array([[_det(a), _det(e)], [_det(c), _det(f)]])

    y = _det(C)/_det(B)

    return Point(x,y)
