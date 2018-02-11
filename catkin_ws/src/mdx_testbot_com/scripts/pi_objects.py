#!/usr/bin/env python

import cv2
import math
import warnings
import numpy as np
import pi_arithmetic
from pi_dtypes import *
import matplotlib.pyplot as plt

class Path(object):
    """docstring for Path"""
    def __init__(self, raw_point_data, stroke_color=(0,255,255), fill_color=(0,255,255), thickness=1, linetype=cv2.LINE_8, closed=False):
        super(Path, self).__init__()
        
        self.raw_point_data = raw_point_data
        self.xs,self.ys = zip(*self.raw_point_data)

        self.points = list()
        for data in self.raw_point_data:
            self.points.append(Point(data[0], data[1]))

        #Attributes
        self.stroke_color = stroke_color
        self.fill_color = fill_color
        self.thickness = thickness
        self.linetype = linetype
        self.closed = closed

        self.boundary_lines = self.getBoundaryLines()

    def getStartPoint(self):
        return (self.xs[0], self.ys[0])

    def getEndPoint(self):
        return (max(self.xs), max(self.ys))

    def getRectInfo(self):
        top_left_corner = (min(self.xs), min(self.ys))
        width = max(self.xs) - top_left_corner[0]
        height = max(self.ys) - top_left_corner[1]
        bottom_right_corner = (top_left_corner[0]+width, top_left_corner[1]+height)
        area = float(width * height)
        return {"top_left_corner":top_left_corner,"height":height,"width":width,"area":area,"bottom_right_corner":bottom_right_corner}

    def getCircleInfo(self):
        top_left_corner = (min(self.xs), min(self.ys))
        width = max(self.xs) - top_left_corner[0]
        height = max(self.ys) - top_left_corner[1]
        center_origin = (top_left_corner[0]+int(width/2.0), top_left_corner[1]+int(height/2.0))
        bottom_right_corner = (top_left_corner[0]+width, top_left_corner[1]+height)
        radius = (width/2.0)**2 + (height/2.0)**2
        area = 2.0*math.pi*(radius**2.0)
        return {"bottom_right_corner":bottom_right_corner, "center_origin":center_origin, "top_left_corner":top_left_corner,"height":height,"width":width,"radius":radius,"area":area}

    def getBoundaryLines(self):
        points = self.points

        # close path
        if points[0] != points[-1]: points.append(points[0])

        lines = []
        for index in xrange(len(points)-1):
            start_point = points[index]
            end_point   = points[index+1]

            line = Line(start_point, end_point)
            lines.append(line)

        return lines

    def getIntersectingPoints(self, test_line):
        intersecting_points = []

        # ignore division by zero warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            
            for line in self.boundary_lines:
                    p = test_line.get_intersecting_point(line)
                    if not (math.isnan(p.x) or math.isnan(p.y)):
                        intersecting_points.append(p)

        return intersecting_points


    def getShadingLines(self, spacing=10, angle=0, padding=0):
        lines = []

        rect_info = self.getRectInfo()
        min_x, min_y = rect_info["top_left_corner"]
        max_x, max_y = rect_info["bottom_right_corner"]

        min_x -= padding
        max_x += padding
        min_y -= padding
        max_y += padding

        cx = (max_x - min_x)/2.0 + min_x
        cy = (max_y - min_y)/2.0 + min_y

        # create lines
        for y in xrange(min_y,max_y+1, spacing):
            start_point = Point(min_x, y)
            end_point = Point(max_x, y)
            line = Line(start_point, end_point)

            about_point = Point(cx, cy)
            line.rotate(angle, about_point)
            lines.append(line)

        return lines

    def getIntersectingLines(self, spacing=10, angle=0):
        self.boundary_lines = self.getBoundaryLines()

        rect_info = self.getRectInfo()
        padding = max(rect_info["height"], rect_info["width"])
        lines = self.getShadingLines(spacing, angle, padding)

        intersecting_lines_array = []
        for line in lines:
            intersecting_points = self.getIntersectingPoints(line)
            sort_function = lambda point : point.x
            intersecting_points = sorted(intersecting_points, key=sort_function)

            for index in xrange(0, len(intersecting_points)-1, 2):
                start_point = intersecting_points[index]
                end_point = intersecting_points[index+1]
                line = Line(start_point, end_point)
                intersecting_lines_array.append(line)

        return intersecting_lines_array


    def drawAsRect(self, image, fill=False):
        rect_info = self.getRectInfo()
        image = cv2.rectangle(
            image,
            rect_info['top_left_corner'],
            rect_info['bottom_right_corner'],
            self.stroke_color,
            self.thickness,
            self.linetype
            )
        return image

    def drawAsCircle(self, image, fill=False):
        circle_info = self.getCircleInfo()
        image = cv2.circle(
            image,
            circle_info['center_origin'],
            int(circle_info['radius']),
            self.stroke_color,
            self.thickness,
            int(self.linetype)
        )
        return image

    def drawAsPath(self, image, fill=False):
        vertices = np.array(self.raw_point_data, np.int32)
        vertices = vertices.reshape((-1,1,2))
        image = cv2.polylines(image, [vertices], self.closed, self.stroke_color, self.thickness, self.linetype)
        return image

    def drawAsPathWithBoundaries(self, image, fill=False):
        image = self.drawAsRect(image, fill)
        image = self.drawTerminals(image, 10)
        return self.drawAsPath(image, fill)

    def drawTerminals(self, image, radius=2):
        red = (255, 0, 0)
        green = (0, 255, 0)

        # Draw start
        image = cv2.circle(
            image,
            self.getStartPoint(),
            radius,
            red,
            self.thickness,
            int(self.linetype)
        )

        # Draw end
        image = cv2.circle(
            image,
            self.getEndPoint(),
            radius+1,
            green,
            self.thickness,
            int(self.linetype)
        )

        return image

    def getPath(self):
        return self.points

    def calculateDirection(self):
        #TODO return average direction
        return None

    def plot(self, title="Path-01", flip=True):
        plt.title(title)
        plt.grid()
        #Flip y axis for graph : because img starts with 0 up
        if flip:
            plt.plot(self.xs, [max(self.ys)-y for y in self.ys])
        else:
            plt.plot(self.xs, ys)

class Line(object):
    """docstring for Line"""
    def __init__(self, point1, point2):
        super(Line, self).__init__()
        self.start = point1
        self.end = point2

        self.compute()

    def compute(self):
        self.line = (self.start, self.end)
        self.m = self.get_gradient()
        self.ref_point = self.start
        self.length = self.get_length()
        self.angle = self.get_angle()

    def _rotate_coord(self, coord, angle, about_point):
        c1,c2 = about_point.x,about_point.y
        xold, yold = coord.x,coord.y

        x = np.array([[c1], [c2]])
        y = np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        z = np.array([[xold - c1], [yold - c2]])

        a = x + np.dot(y,z)
        return Point(a[0][0],a[1][0])

    def rotate(self, angle, about_point=None):
        #rotate start point about midpoint
        if not about_point:
            about_point = self.get_midpoint()

        self.start = self._rotate_coord(self.start, angle, about_point)
        self.end = self._rotate_coord(self.end, angle, about_point)

        self.compute()

    def get_length(self):
        return pi_arithmetic.get_distance_bwt_points(self.start, self.end)

    def get_gradient(self):
        return math.tan(self.get_angle())

    def get_angle(self):
        dy = float(self.end.y - self.start.y)
        dx = float(self.end.x - self.start.x)
        angle = math.atan2(dy,dx)
        return angle

    def get_midpoint(self):
        midpoint = Point( (self.start.x+self.end.x)/2.0, (self.start.y+self.end.y)/2.0 )
        return midpoint

    def plot(self, title="Line-01"):
        plt.title(title)
        plt.grid()
        xs = [self.start.x, self.end.x]
        ys = [self.start.y, self.end.y]
        plt.plot(xs, ys)

    def is_on_line(self, point):
        # This works based on the principle
        # A-C----B; AC + CB == AB
        
        ac = pi_arithmetic.get_distance_bwt_points(self.start, point)
        cb = pi_arithmetic.get_distance_bwt_points(point, self.end)
        ab = pi_arithmetic.get_distance_bwt_points(self.start, self.end)
        diff = (ac + cb) - ab
        return round(diff) == 0

    def get_intersecting_point(self, other):
        def _det(x):
            '''returns the determinant of x'''
            return np.linalg.det(x)
    
        #Line 01
        x1 = self.start.x; x2 = self.end.x
        y1 = self.start.y; y2 = self.end.y

        #Line 02
        x3 = other.start.x; x4 = other.end.x
        y3 = other.start.y; y4 = other.end.y
        
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

        point = Point(x,y)

        #print "point {0},{1}".format(point.x, point.y)
        #print "self {0},{1} - {2},{3} {4}".format(self.start.x, self.start.y, self.end.x, self.end.y, self.is_on_line(point))
        #print "other {0},{1} - {2},{3} {4}".format(other.start.x, other.start.y, other.end.x, other.end.y, other.is_on_line(point))

        if self.is_on_line(point) and other.is_on_line(point):
            return point
        else:
            return Point(float('nan'), float('nan'))
        

class Point(object):
    """docstring for Point"""
    def __init__(self, x,y):
        super(Point, self).__init__()
        if not (isinstance(x, Infinity) or isinstance(x, Undefined)):
            self.x = float(x)
        else:
            self.x = x

        if not (isinstance(x, Infinity) or isinstance(x, Undefined)):
            self.y = float(y)
        else:
            self.y = y

        self.r = math.sqrt(pow(x,2)+pow(y,2))
        self.theta = math.atan2(y, x)

        self.point = (self.x,self.y)
        self.point_polar = (self.r,self.theta)

    def __add__(self, other):
        if isinstance(other, tuple) and 2 == len(other):
            other = Point(other[0], other[1])
        elif not isinstance(other, type(self)):
            raise ValueError("Invalid type {0} for other".format(type(other)))

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, tuple) and 2 == len(other):
            other = Point(other[0], other[1])
        elif not isinstance(other, type(self)):
            raise ValueError("Invalid type {0} for other".format(type(other)))

        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, tuple) and 2 == len(other):
            other = Point(other[0], other[1])
        elif not isinstance(other, type(self)):
            raise ValueError("Invalid type {0} for other".format(type(other)))

        return (self.x == other.x) and (self.y == other.y)
    
    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.point = (self.x,self.y)
        return self

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y
        self.point = (self.x,self.y)
        return self

    def getAsPolar(self):
        return (self.r, self.theta)



def main():
    xs = [10, 20, 40, 20, 8]
    ys = [10, 50, 4, 30, 10]

    my_path = Path(list(zip(xs, ys)))
    #my_path.plot(flip=False)

    lines = my_path.getBoundaryLines()
    for line in lines:
        line.plot()

    # lines = my_path.getShadingLines(1, math.radians(-80))
    # for line in lines:
    #     line.plot()

    lines = my_path.getIntersectingLines(1, math.radians(0))
    for line in lines:
        line.plot()
    print len(lines)
        
    lines = my_path.getIntersectingLines(1, math.radians(90))
    for line in lines:
        line.plot()

    plt.show()


if __name__ == '__main__':
    main()