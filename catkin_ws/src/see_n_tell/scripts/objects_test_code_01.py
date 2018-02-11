import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import colorsys
import basic_header
import math

class Node(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.input_connections = []
        self.output_connections = []

    def connect(self, node):
        self.output_connections.append(node)
        node.input_connections.append(self)

    def numberOfConnections(self):
        return len(self.input_connections) + len(self.output_connections)

    def numberOfInputConnections(self):
        return len(self.input_connections)

    def numberOfOutputConnections(self):
        return len(self.output_connections)
    
class Path(object):
    def __init__(self, row, col, row_locations, col_locations):
        self.row = row
        self.col = col
        self.generateNodes(row_locations, col_locations)
        self.connectNodes()

    def generateNodes(self, rows, cols):
        self.nodes = []
        for i in range(len(rows)):
            self.nodes.append( Node(rows[i], cols[i]) )

    def connectNodes(self):
        if len(self.nodes) <= 1:
            return
        
        for i in range(len(self.nodes)-1):
            curr_node = self.nodes[i]
            next_node = self.nodes[i+1]
            
            curr_node.connect(next_node)

    def drawPathOnImage(self, img, color=(0,255,0), thickness=3, linetype=8):
        if len(self.nodes) <= 1:
            return img
        
        for i in range(len(self.nodes)-1):
            curr_node = self.nodes[i]
            next_node = self.nodes[i+1]

            img = cv2.line(
                img,
                (curr_node.col, curr_node.row),
                (next_node.col, next_node.row),
                color,
                thickness,
                linetype,
                )

        if len(self.nodes) > 2:
            curr_node = self.nodes[-1]
            next_node = self.nodes[0]
            
            img = cv2.line(
                img,
                (curr_node.col, curr_node.row),
                (next_node.col, next_node.row),
                color,
                thickness,
                linetype,
                )

        return img

    def splitPathIntoObjectsByReigions(self):
        top_nodes = [node for node in nodes if node.row <= self.row]
        bottom_nodes = [node for node in nodes if node.row >= self.row+height]

        top_nodes_location = [
            self.col,
            top_nodes[0].col,
            top_nodes[-1].col,
            self.col+length
            ]

        bottom_nodes_location = [
            self.col,
            bottom_nodes[0].col,
            bottom_nodes[-1].col,
            self.col+length
            ]
        

class Object(object):
    def __init__(self, mask, contour):
        self.mask = np.copy(mask)
        self.contour = np.copy(contour)
        self.path = None
        
        self.row_length,self.col_length = self.mask.shape
        
        self.row_locations = self.contour[:,:,1].ravel()
        self.col_locations = self.contour[:,:,0].ravel()

        self.calculateDimensions()

    def calculateDimensions(self):
        #Calculate the minimum and maximum row and column of the region to determine its length and height
        min_row = int(min(self.row_locations))
        max_row = int(max(self.row_locations))

        min_col = int(min(self.col_locations))
        max_col = int(max(self.col_locations))

        #Update the region's length and height
        self.length = max_col - min_col
        self.height = max_row - min_row

        #Calculate region radius from length and height using Pythagoras theorem
        if self.length <= 0 or self.height <= 0:
            self.radius = 0
        else:
            self.radius = basic_header.getHypotenuse(self.length, self.height)/2

        self.area = self.length * self.height

        #Update the region's top corner position
        self.top_corner_position = (min_row, min_col)
        self.center_position = (
            self.top_corner_position[0] + int(self.height/2),
            self.top_corner_position[1] + int(self.length/2)
            )

        self.path = Path(self.top_corner_position[0], self.top_corner_position[1], self.row_locations, self.col_locations)

        self.mask[:] = 0
        self.mask[
            self.top_corner_position[0]:self.top_corner_position[0]+self.height,
            self.top_corner_position[1]:self.top_corner_position[1]+self.length
            ] = 255

    def updateObjectColor(self, img):
        if self.radius <= 0:
            self.color = (0,0,0)
            return

        row,col = self.top_corner_position
        try:
            r = int(np.average(
                img[
                    row : row+self.height,
                    col : col+self.length,
                    0
                    ]
                ))
            g = int(np.average(
                img[
                    row : row+self.height,
                    col : col+self.length,
                    1
                    ]
                ))
            b = int(np.average(
                img[
                    row : row+self.height,
                    col : col+self.length,
                    2
                    ]
                ))
            self.color = (r,g,b)
        except ValueError:
            self.color = (0,0,0)

    def getDimensions(self):
        #Return region dimensions
        return (self.length, self.height, self.radius)
    
    def getLength2HeightRatio(self):
        dimens = self.getDimensions()
        #Description = area, length/height, num of sub objects
        #Prevent zero division error
        try:
            return dimens[0] / float(dimens[1])
        except ZeroDivisionError:
            return -1.0

    def isWithinLocation(self, obj, margin=0.025):
        try:
            row_location_percentage_diff = getPercentageDifference(self.top_corner_position[0], obj.top_corner_position[0], self.row_length)
            col_location_percentage_diff = getPercentageDifference(self.top_corner_position[1], obj.top_corner_position[1], self.col_length)

            if row_location_percentage_diff < 0 or col_location_percentage_diff < 0:
                return False
            elif row_location_percentage_diff <= margin and col_location_percentage_diff <= margin:
                return True
            else:
                return False
        except ZeroDivisionError:
            return False
        
    def isSimilar(self, obj, margin=0.025):
        if obj == self:
            return True

        try:
            ratio_percentage_diff = getPercentageDifference(self.getLength2HeightRatio(), obj.getLength2HeightRatio(), max(self.row_length, self.col_length))
            radius_percentage_diff = getPercentageDifference(self.radius, obj.radius, basic_header.getHypotenuse(self.col_length, self.row_length)/2)

            if ratio_percentage_diff < 0 or radius_percentage_diff < 0:
                return False
            elif ratio_percentage_diff <= margin:
                if radius_percentage_diff <= margin:
                    return True
                else:
                    return False
            else:
                return False
        except ZeroDivisionError:
            return False

def getPercentageDifference(x, y, num_range):
    diff = abs(x-y)
    p_diff = max(min(float(diff)/float(num_range), 1.0), 0.0)
    return p_diff

def colorDifference(color1, color2):
    diff = pow(color1[0] - color2[0], 2) + pow(color1[1] - color2[1], 2) + pow(color1[2] - color2[2], 2)
    return math.sqrt(diff) * 0.5773502691896257

def show(img):
    plt.imshow(img)
    plt.show()

def convertRGB2HSB(color):
    hsb = colorsys.rgb_to_hsv(color[0]/255.0, color[1]/255.0, color[2]/255.0)
    return np.array([i*255.0 for i in hsb])

def convertHSB2RGB(color):
    rgb = colorsys.hsv_to_rgb(color[0]/255.0, color[1]/255.0, color[2]/255.0)
    return np.array([i*255.0 for i in rgb])

def generateColorRanges(width=17):
    color_ranges = []
    for b in range(0, 255, width):
        for s in range(0, 255, width):
            for h in range(0, 255, width):
                lower_color = np.array([h, s, b])
                upper_color = np.array([h+width, s+width, b+width])

                color_range = (lower_color, upper_color)
                color_ranges.append(color_range)
    color_ranges[-1] = (color_ranges[-1][0], np.array([255, 255, 255]))
    return color_ranges

def getMaskForColorRanges(img, color_ranges, threshold=100):
    img = cv2.medianBlur(img, 5)
    #img = cv2.GaussianBlur(img, (5,5), 0)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    masks = []
    contours = []
    objects = []
    for i in range(len(color_ranges)-1):
        mask = cv2.inRange(hsv_img, color_ranges[i][0], color_ranges[i][1])
        cv2.erode(cv2.dilate(mask, (5,5)), (3,3))
            
        if len(np.where(mask > 0)[0]) < threshold:
            continue

        for contour in cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]:
            obj = Object(mask, contour)
            obj.updateObjectColor(img)
            objects.append(obj)
            
        masks.append(mask)
        contours.append(contour)
        
    return masks,contours,objects

def getObjectForColorRanges(img, color_ranges, threshold=100, filter_funcs=[], filter_params=[]):
    img = cv2.medianBlur(img, 5)
    #img = cv2.GaussianBlur(img, (5,5), 0)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    objects = []
    for i in range(len(color_ranges)-1):
        mask = cv2.inRange(hsv_img, color_ranges[i][0], color_ranges[i][1])
        mask = cv2.dilate(mask, (5,5))
        mask = cv2.erode(mask, (3,3))
            
        if len(np.where(mask > 0)[0]) < threshold:
            continue

        for contour in cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]:
            obj = Object(mask, contour)
            obj.updateObjectColor(img)

            if checkFiltersOnObject(obj, filter_funcs, filter_params):
                objects.append(obj)
            else:
                continue
        
    return objects

def drawContoursOnBlankImage(img, contours, color=(0,255,0)):
    blank_img = np.zeros(img.shape, img.dtype)
    cv2.drawContours(blank_img, contours, -1, color, 3)
    return blank_img

def drawContoursOnImage(img, contours, color=(0,255,0)):
    cv2.drawContours(img, contours, -1, color, 3)
    return img

def filterByRatio(obj=None, filter_params=[0.9,1.1]):
    ratio = obj.getLength2HeightRatio()
    if ratio >= filter_params[0] and ratio <= filter_params[1]:
        return True
    else:
        return False

def filterByRadius(obj=None, filter_params=[27,33]):
    radius = obj.radius
    if radius >= filter_params[0] and radius <= filter_params[1]:
        return True
    else:
        return False

def filterByLocation(obj, filter_params=[(0,0),30]):
    dist = basic_header.getDistanceBetweenPoint(filter_params[0], obj.center_position)
    if dist <= filter_params[1]:
        return True
    else:
        return False
    

def filterByColor(obj=None, filter_params=[(0,0,0), 15]):
    color_sim = colorDifference(obj.color, filter_params[0])
    if color_sim <= filter_params[1]:
        return True
    else:
        return False

def checkFiltersOnObject(obj, filters, params):
    passed_test = True
    for i in range(len(filters)):
        if filters[i](obj, params[i]):
            continue
        else:
            passed_test = False
            break
    return passed_test

def removeRedundacies(objects):
    new_objects = []
    for obj in objects:
        found = False
        for new_obj in new_objects:
            if new_obj.isSimilar(obj) and new_obj.isWithinLocation(obj):
                found = True
                break
        if found:
            continue
        else:
            new_objects.append(obj)
    return new_objects

def filerObjects(objects, filter_funcs, filter_params):
    new_objects = []
    for obj in objects:
        found = False
        for new_obj in new_objects:
            if new_obj.isSimilar(obj) and new_obj.isWithinLocation(obj):
                found = True
                break
        if found:
            continue
        else:
            if checkFiltersOnObject(obj, filter_funcs, filter_params):
                new_objects.append(obj)
    return new_objects

#stepThroughContours(img, masks, contours, len(contours))
def stepThroughContours(img, masks, contours, n):
    for i in range(n):
        bimg = cv2.bitwise_and(img, img, mask=masks[i])
        bimg = drawContoursOnImage(bimg, contours[i])
        show(bimg)

#viewObject(img, objects[0])
def viewObject(img, obj):
    bimg = cv2.bitwise_and(img, img, mask=obj.mask)
    bimg = drawContoursOnImage(bimg, obj.contour)
    print "pos",obj.top_corner_position,"dimen",obj.getDimensions(),"color",obj.color
    show(bimg)

#viewObjectWithPath(img, objects[0])
def viewObjectWithPath(img, obj):
    bimg = cv2.bitwise_and(img, img, mask=obj.mask)
    bimg = obj.path.drawPathOnImage(bimg)
    print "pos",obj.top_corner_position,"dimen",obj.getDimensions(),"color",obj.color
    show(bimg)

#stepThroughObjects(img, objects)
def stepThroughObjects(img, objects):
    i = len(objects)
    for obj in objects:
        bimg = cv2.bitwise_and(img, img, mask=obj.mask)
        bimg = drawContoursOnImage(bimg, obj.contour)
        print "sn",i,"pos",obj.top_corner_position,"dimen",obj.getDimensions(),"color",obj.color
        show(bimg)
        i -= 1

#viewObjectsWithPath(img, objects)
def viewObjectsWithPath(img, objects):
    sn = len(objects)
    for obj in objects:
        print "sn",sn,
        viewObjectWithPath(img, obj)
        sn = sn - 1
color_ranges = generateColorRanges(30)
filters = [
    filterByRatio,
    filterByRadius,
    filterByColor,
    #filterByLocation
    ]
filter_params = [
    [0.5,1.5],
    [5,300],
    [(114,126,156), 25]
    #[(288,404),100]
    ]

#img = cv2.imread('pic_02.png')
#img = cv2.imread('pic_03.jpg')
#img = cv2.imread('letter_A_01.png')
#img = cv2.imread('letters_A2D.jpg')
#img = cv2.imread('letters_A2D_02.jpg')
img = cv2.imread('people_01.jpg')
#img = cv2.imread('letter_A_01.jpg')
#img = cv2.imread('pic_02a.jpg')

import time
start_time = time.time()

print "time_1 = ",time.time() - start_time
start_time = time.time()

objects = getObjectForColorRanges(img, color_ranges, 100, filters, filter_params)

print "time_2 = ",time.time() - start_time
start_time = time.time()

objects = removeRedundacies(objects)

print "len(objects) =",len(objects)
print "time_3 = ",time.time() - start_time
