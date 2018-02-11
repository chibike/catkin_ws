#!/usr/bin/env python

import math
import colorsys
import numpy as np

#define color by (type, whiteness, blackness)
#simplified to (type, direction)
#where direction = blackness - whiteness
class RGBColor(object):
    def __init__(self, color_as_rgb=(0,0,0)):
        self.rgb_color = None
        self.hsv_color = None
        self.update_color(color_as_rgb)

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Cannot perform sub operation on element of type {0}".format(type(other)))
        return self.get_distance(other)

    def __mul__(self, other):
        if isinstance(other, int):
            pass
        elif isinstance(other, type(self)):
            pass
        else:
            raise TypeError("Cannot perform mul operation on element of type {0}".format(type(other)))

    def __eq__(self, other):
        return self.rgb_color == other.rgb_color

    def update_color(self, color=(0,0,0)):        
        self.rgb_color = (color[0]/255.0,
                          color[1]/255.0,
                          color[2]/255.0)

        self.hsv_color = colorsys.rgb_to_hsv(self.rgb_color[0],
                                             self.rgb_color[1],
                                             self.rgb_color[2])

    def get_bgr(self, scale=255):
        r,g,b = [int(i*scale) for i in self.rgb_color]
        return (b,g,r)

    def get_color_boundary(self, type_diff, direction_diff):
        def _get_circle_point(n1, diff, min_n, max_n):
            n2 = n1 + abs(diff)
            if n2 > max_n: n2 = max_n - n2
            return n2

        def _get_direction_boundary(direction_diff):
            d1 = self.hsv_color[2]-self.hsv_color[1]
            d2 = -1.0* (direction_diff - d1)
            v = d2 + s
            if d2 >= 0:
                v = d2
            #v-s = d2

    def get_distance(self, other_color):
        r1,g1,b1 = self.rgb_color
        r2,g2,b2 = other_color.rgb_color
        p = pow(r2-r1, 2) + pow(g2-g1, 2) + pow(b2-b1, 2)
        return math.sqrt(p)

    def get_type_diff(self, other_color):
        def _get_circle_diff(n1, n2, min_n, max_n):
            #solving as the shortest distance around a circle
            n1 += min_n; n2 += min_n
            a = min(n1, n2); b = max(n1, n2)
            return min( max_n-b+a, b-a )
        
        if not isinstance(other_color, type(self)): return None
        else:
            return _get_circle_diff( self.hsv_color[0],
                                   other_color.hsv_color[0],
                                   0, 1.0 )
        return None

    def get_direction_diff(self, other_color):
        if not isinstance(other_color, type(self)): return None
        else: return (self.hsv_color[2]-self.hsv_color[1]) - (other_color.hsv_color[2]-other_color.hsv_color[1])
        return None


class ColorCluster(object):
    """docstring for ColorCluster"""
    def __init__(self, color = RGBColor(), position = [], accept_radius=5):
        super(ColorCluster, self).__init__()

        self.rows = []
        self.columns = []
        self.color = color
        self.accept_radius = accept_radius

        if len(position) == 2:
            self.rows.append(position[0])
            self.columns.append(position[1])

        self.__update()

    def __dist_frm(self, position):
        r1,c1 = self.position; r2,c2 = position
        return math.sqrt(pow(r2-r1,2) + pow(c2-c1,2))

    def __update(self):
        min_row,max_row = min(self.rows),max(self.rows)
        min_column,max_column = min(self.columns),max(self.columns)

        self.width  = max_column - min_column
        self.height = max_row - min_row
        self.radius = math.sqrt(pow(self.width, 2) + pow(self.height,2))/2.0

        self.position = self.row, self.column = int(min_row + (self.height/2)), int(min_column + (self.width/2))

    def distance(self, other):
        if not isinstance(other, type(self)):
            return None

        return self.__dist_frm(other.position)

    def is_touching(self, other):
        if not isinstance(other, type(self)):
            return None

        return self.__dist_frm(other.position) <= (self.radius + other.radius)

    def append(self, color, position):
        if not self.check_eligibility(color, position):
            return False
        self.rows.append(position[0])
        self.columns.append(position[1])
        self.__update()
        return True

    def merge(self, color_cluster):
        if not isinstance(color_cluster, type(self)):
            return False

        self.rows += color_cluster.rows
        self.columns += color_cluster.columns
        self.__update()
        return True

    def check_eligibility(self, other_color, other_position):
        if (self.color == other_color) and ((self.__dist_frm(other_position) <= (self.radius+self.accept_radius)*2.0)):
            other_row, other_column = other_position
            sort_function = lambda x : abs(x - other_row)
            closest_position_index = self.rows.index(sorted(self.rows, key=sort_function)[0])

            closest_row, closest_column = self.rows[closest_position_index], self.columns[closest_position_index]
            distance = math.sqrt( pow((other_row-closest_row),2) + pow((other_column-closest_column), 2) )

            return distance <= (self.radius * 2.0)
        else:
            return False

    def draw(self, frame, stroke=None, fill=None):
        for index in xrange(min(len(self.rows), len(self.columns))):
            frame[self.rows[index], self.columns[index]] = fill.get_bgr()
        return frame

#Predefined colors
RED_MAX    = RGBColor((255,0,0))
BLUE_MAX   = RGBColor((0,0,255))
BLACK_MAX  = RGBColor((0,0,0))
GREEN_MAX  = RGBColor((0,255,0))
WHITE_MAX  = RGBColor((255,255,255))
YELLOW_MAX = RGBColor((255,255,0))

_PRE_DEF__BINARY  = [BLACK_MAX, WHITE_MAX]
_PRE_DEF__PRIMARY = [RED_MAX, BLUE_MAX, GREEN_MAX]
_PRE_DEF__MAIN_01 = _PRE_DEF__BINARY + _PRE_DEF__PRIMARY + [YELLOW_MAX]

def simplify(color1, color_array=_PRE_DEF__MAIN_01):
    '''returns the color with the closest type in the color array'''
    sort_key = lambda color : abs(color1 - color)
    bar = sorted(color_array, key=sort_key)
    return bar[0]

def get_as_color_clusters(image):
    color_clusters = []
    rows,cols,_ = np.shape(image)

    for row in xrange(rows):
        for col in xrange(cols):
            r,g,b = image[row,col]
            color = RGBColor((b,g,r))
            position = (row,col)

            added_to_a_cluster = False
            def _sort_function(x):
                return not x.check_eligibility(color, position)

            foo = sorted(color_clusters, key=_sort_function)
            if len(foo) > 0 and foo[0].append(color, position):
                added_to_a_cluster = True

            if not added_to_a_cluster:
                color_cluster = ColorCluster(color, position)
                color_clusters.append(color_cluster)

    def remove_holes(color_clusters, min_radius=15):
        holes = filter(lambda x : x.radius < min_radius, color_clusters)
        color_clusters = filter(lambda x : x.radius >= min_radius, color_clusters)

        if len(color_clusters) <= 0:
            return holes

        for hole in holes:
            sort_function = lambda x : x.distance(hole.position)
            color_clusters = sorted(color_clusters, key=sort_function)
            color_clusters[0].merge(hole)

        return color_clusters

    def merge_overlaps(color_clusters):
        for i in range(len(color_clusters)-1, -1, -1):
            current = color_clusters[i]
            filter_function = lambda x : x.is_touching(current) and (x.color == current.color)

            # Avoid checking yourself
            foo = filter(filter_function, color_clusters[:i]+color_clusters[i+1:])
            if len(foo) > 0:
                foo[0].merge(current)
                color_clusters.remove(current)

        return color_clusters

    color_clusters = remove_holes(color_clusters)
    #color_clusters = merge_overlaps(color_clusters)

    return color_clusters