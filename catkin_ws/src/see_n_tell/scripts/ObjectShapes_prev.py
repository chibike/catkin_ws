#!/usr/bin/env python

#Import support libraries for specialist functions
import math
import numpy as np
import basic_header
import cv2

class Object(object):
    def __init__(self, pixel_positions=None):
        #Initialize properties variables
        self.length = 0
        self.height = 0
        self.radius = 0
        self.depth  = 0
        self.column_wise_rotation = 0
        self.row_wise_rotation = 0
        self.center_position = (0,0)
        self.top_corner_position = (0,0)
        self.color = (0,0,0)
        self.pixels_positions = []
        self.sub_objects = []

        self.addPixelPositions(pixel_positions)
    
    def morphIntoObject(self, obj=None):
        #Get dimension difference
        obj_l,obj_h,obj_r = obj.getDimensions()
        self_l,self_h,self_r = self.getDimensions()
        delta_dimens = (
            obj_l - self_l,
            obj_h - self_h,
            obj_r - self_r
        )
        
        #Get position difference
        obj_center_row, obj_center_col = obj.getCenterPosition()
        self_center_row, self_center_col = self.getCenterPosition()
        #Get depth difference
        delta_depth = obj.getDepth() - self.getDepth()
        delta_position = (
            obj_center_row - self_center_row,
            obj_center_col - self_center_col,
            delta_depth
        )
        
        #Get color difference
        obj_h, obj_s, obj_b = obj.getColor()
        self_h, self_s, self_b = self.getColor()
        delta_color = (
            obj_h - self_h,
            obj_s - self_s,
            obj_b - self_b
        )
        
        
        #Copy pixels over and update properties
        self.pixels_positions = obj.getPixelPositions()
        self.sub_objects = obj.getSubObjects()
        self.updateProperties()
        
        return (delta_dimens, delta_position, delta_color)

    def addPixelPositions(self, pixel_positions=None):
        if type(pixel_positions) == None:
            return False

        if not isinstance(self.pixels_positions, list):
            return False

        try:
            self.pixels_positions = list(set(self.pixels_positions + pixel_positions))
        except TypeError:
            data = self.pixels_positions + pixel_positions
            self.pixels_positions = list(set([tuple(i) for i in data]))
        
        self.updateProperties()

        return True
    
    def addSubObjects(self, objects, threshold=0.8):
        pos_1 = self.getTopPosition()
        dimens_1 = self.getDimensions()
        area_1 = self.getArea(True)
        
        if area_1 <= 0:
            return objects
        
        invalid_sub_objects = []
        for obj in objects:
            area_2 = obj.getArea(True)
            if area_2 <= 0 or obj == self:
                continue
               
            pos_2 = obj.getTopPosition()
            dimens_2 = obj.getDimensions()
            overlap_dimens = basic_header.getOverlappingRectDimensions(pos_1, dimens_1, pos_2, dimens_2)
            min_area = min(area_1, area_2)
            
            #Prevent zero division error
            try:
                overlap_ratio = float(overlap_dimens[0]*overlap_dimens[1]) / min_area
                if overlap_ratio >= threshold and self.getArea(True) >= obj.getArea(True):
                    self.sub_objects.append(obj)
                else:
                    invalid_sub_objects.append(obj)
            except ZeroDivisionError:
                continue
                
        return invalid_sub_objects
    
    def isSameObject(self, obj, threshold_percent=0.25):
        #Get object's radius
        obj_r = obj.getDimensions()[2]
        self_r = self.getDimensions()[2]
        
        #Compare radius
        if not basic_header.isWithinPercentage(obj_r, self_r, threshold_percent):
            return False
        
        #Get object's length to height ratio
        obj_r = obj.getLength2HeightRatio()
        self_r = self.getLength2HeightRatio()
        
        #Compare length to height relationship
        if not basic_header.isWithinPercentage(obj_r, self_r, threshold_percent):
            return False
        
        #Get number of sub objects
        obj_n = obj.getNumberOfSubPixels()
        self_n = self.getNumberOfSubPixels()
        
        #Compare number of sub objects
        if not basic_header.isWithinPercentage(obj_n, self_n, threshold_percent):
            return False
        
        return True
    
    def setColor(self, color_img):
        #Stores the average color
        
        if self.getArea(True) < 1:
            return 0
            
        width, height,_ = self.getDimensions()
        start_row, start_column = self.getTopPosition()
        end_row = start_row + height
        end_column = start_column + width
        
        #print "COL width =",width, " height =",height, " s_row",start_row, " s_col",start_column, " e_row",end_row, " e_col",end_column
        #print "img shape =",color_img.shape
        
        try:
            img = cv2.cvtColor(color_img[start_column:end_column, start_row:end_row], cv2.COLOR_BGR2HSV)
            h = int(np.average(img[:,:,0]))
            s = int(np.average(img[:,:,1]))
            v = int(np.average(img[:,:,2]))
        except ValueError:
            h=s=v=0
        self.color = (h,s,v)
        
        return self.getColor()
    
    def setDepth(self, depth_frame):
        #Stores the average depth
        
        if self.getArea(True) < 1:
            return 0
            
        width, height,_ = self.getDimensions()
        start_row, start_column = self.getTopPosition()
        end_row = start_row + height
        end_column = start_column + width
        
        #print "DEP width =",width, " height =",height, " s_row",start_row, " s_col",start_column, " e_row",end_row, " e_col",end_column
        #print "img shape =",depth_frame.shape
        
        try:
            self.depth = int(np.average(depth_frame[start_column:end_column, start_row:end_row]))
        except ValueError:
            self.depth = 0 
            
        return self.getDepth()
    
    def getPixelPositions(self):
        return self.pixels_positions
    
    def getSubObjects(self):
        return self.sub_objects
    
    def getLength2HeightRatio(self):
        dimens = self.getDimensions()
        #Description = area, length/height, num of sub objects
        #Prevent zero division error
        try:
            return dimens[0] / float(dimens[1])
        except ZeroDivisionError:
            return -1
    
    def getNumberOfSubPixels(self):
        return len(self.sub_objects)
    
    def getTagData(self):
        #Return a tag/self description of its self
        return (
            self.getArea(True),
            self.getLength2HeightRatio(),
            self.getNumberOfSubPixels(),
            self.getColor(),
            self.getDepth()
            )
    
    def getColor(self):
        #Returns the average color
        return self.color
    
    def getDepth(self):
        #Returns the average depth
        return self.depth
        
    def getCenterPosition(self):
        #Return region center position
        return tuple(self.center_position)

    def getTopPosition(self):
        #Return region top position
        return tuple(self.top_corner_position)

    def getDimensions(self):
        #Return region dimensions
        return (self.length, self.height, self.radius)

    def getArea(self, rect_mode = True):
        if rect_mode:
            #Return area as the area of a rectangle
            return float(self.getDimensions()[0] * self.getDimensions()[1])
        else:
            #Return area as the area of a circle
            return math.pi * float(pow(self.getDimensions()[2], 2))

    def getNumberOfPixels(self):
        #Return the number of pixels
        return len(self.pixels_positions)

    def getDensity(self, rect_mode=True):
        #Calculate pixel density of the region
        #    Density =  number_of_pixels / regional area
        area = self.getArea(rect_mode)

        #Avoid division by zero error
        if area <= 0:
            return 0
        else:
            return self.getNumberOfPixels() / self.getArea(rect_mode)

    def updateProperties(self):
        #Calculate region dimensions
        self._calculateDimensions()

        #Calculate region radius
        self._calculateRadius()

        #Calculate region center position
        self._calculateCenterPosition()

    def _calculateDimensions(self):
        #Calculate the minimum and maximum row and column of the region to determine its length and height
        rows, columns = zip(*self.pixels_positions)
        
        min_row = int(min(rows))
        max_row = int(max(rows))

        min_col = int(min(columns))
        max_col = int(max(columns))

        #Update the region's length and height
        self.length = max_col - min_col
        self.height = max_row - min_row

        #Update the region's top corner position
        self.top_corner_position = (min_row, min_col)
        
    def _calculateRadius(self):
        #Calculate region radius from length and height using Pythagoras theorem
        self.radius = basic_header.getHypotenuse(self.length, self.height)/2

    def _calculateCenterPosition(self):
        #Calculate the new center position from the regions height, length, and top corner position
        row = self.top_corner_position[0] + int(self.height/2)
        col = self.top_corner_position[1] + int(self.length/2)

        #Update the region's center position
        self.center_position = (row, col)

    def getEdgePositions(self, row_rotation=0, col_rotation=0):
        self.column_wise_rotation = basic_header.constrainf(col_rotation, -90, 90)
        self.row_wise_rotation = basic_header.constrainf(row_rotation, -90, 90)

        bottom_length = top_length = self.length
        right_height = left_height = self.height

        if self.column_wise_rotation >= 0 and self.column_wise_rotation <= 90:
            bottom_length = top_length = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, self.length)
            right_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, self.height)
        elif self.column_wise_rotation <= 0 and self.column_wise_rotation >= -90:
            self.column_wise_rotation = abs(self.column_wise_rotation)
            bottom_length = top_length = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, self.length)
            left_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, self.height)

        if self.row_wise_rotation >= 0 and self.row_wise_rotation <= 90:
            top_length = basic_header.mapf(self.row_wise_rotation, 90, 0, 0, top_length)
            left_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, left_height)
            right_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, right_height)
        elif self.row_wise_rotation <= 0 and self.row_wise_rotation >= -90:
            self.row_wise_rotation = abs(self.row_wise_rotation)
            bottom_length = basic_header.mapf(self.row_wise_rotation, 90, 0, 0, bottom_length)
            left_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, left_height)
            right_height = basic_header.mapf(self.column_wise_rotation, 90, 0, 0, right_height)

        c_row,c_column = self.center_position

        top_left_pos = (c_row-(left_height/2), c_column-(top_length/2))
        top_right_pos = (c_row-(right_height/2), c_column+(top_length/2))
        bottom_left_pos = (c_row+(left_height/2), c_column-(bottom_length/2))
        bottom_right_pos = (c_row+(right_height/2), c_column+(bottom_length/2))

        return [top_left_pos, top_right_pos, bottom_left_pos, bottom_right_pos]


def printPlaneInfo(plane, row_rotation=0, col_rotation=0):
    print "------ Plane Data ------"
    print "Center Position =",plane.getCenterPosition()
    print "Top Position =",plane.getTopPosition()

    width,height,radius = plane.getDimensions()
    print "Width =",width
    print "Height =",height
    print "Radius =",radius
    print "Plane Rect Area =",plane.getArea(True)
    print "Plane Circle Area =",plane.getArea(False)
    print "Plane Rect Density =",plane.getDensity(True)
    print "Plane Circle Density =",plane.getDensity(False)
    print "Number of pixels =",plane.getNumberOfPixels()
    print "Edge positions =",plane.getEdgePositions(row_rotation, col_rotation)


def getIndexOfObjectWithMaxArea(objects):
    max_index = 0
    max_area = objects[max_index].getArea()
    
    new_objects = []
    for index in range(len(objects)):
        obj_area = objects[index].getArea()
        if obj_area > max_area:
            max_index = index
            max_area = obj_area
    return (max_index,max_area)
    
class Rectangle(object):
    def __init__(self,row=None,column=None,width=None,height=None):
        self.row = row
        self.col = column
        self.width = width
        self.height = height
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.top_left_origin = (self.row, self.col)
        self.bottom_left_origin = (self.row+self.height, self.col+self.width)

    def drawOnImage(self, img = None, text="", text_size=0.4, bcolor=(0,0,255), tcolor=(0,255,229), thickness=1, line_type=8):
        return cv2.putText(
            cv2.rectangle(
                img,
                self.top_left_origin,
                self.bottom_left_origin,
                bcolor,
                thickness,
                line_type
                ),
            text,
            self.top_left_origin,
            self.font,
            0.4,
            tcolor,
            1,
            cv2.LINE_8
            )

def main():
    pixels = [(0,0),(0,10),(10,10),(10,0)]
    plane = Object(pixels)
    printPlaneInfo(plane)

if __name__ == "__main__":
    main()
















        
