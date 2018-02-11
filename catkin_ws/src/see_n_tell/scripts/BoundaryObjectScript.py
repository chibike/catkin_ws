#!/usr/bin/env python

#Import support libraries for specialist functions
import math
import numpy as np
import basic_header

class PixelRegion(object):
    def __init__(self, pixel_position):
        #Initialize properties variables
        self.width = 0
        self.height = 0
        self.radius = 0
        self.center_position = (0,0)
        self.top_corner_position = (0,0)
        
        self.pixels_row_position = [pixel_position[0]]
        self.pixels_col_position = [pixel_position[1]]

        #Update region properties
        self.updateProperties()
        
    def addPixel(self, pixel_position, acceptable_range=5):
        #print "Adding pixel at position",pixel_position
        #Verify that the pixel is in range before proceeding
        if basic_header.getDistanceBetweenPoint(self.getCenterPosition(), pixel_position) > (acceptable_range + self.getDimensions()[2]):
            return False
        
        #If pixel has been added already ignore
        if (pixel_position[0] in self.pixels_row_position) and (pixel_position[1] in self.pixels_col_position):
            return True
        
        #Add the pixel position to the list
        self.pixels_row_position.append(pixel_position[0])
        self.pixels_col_position.append(pixel_position[1])

        #Update region properties
        self.updateProperties()

        return True

    def addPixels(self, pixel_positions, acceptable_range=5):
        invalid_pixel_positions = []
        for pixel_position in pixel_positions:
            if not self.addPixel(pixel_position, acceptable_range):
                invalid_pixel_positions.append(pixel_position)

        return invalid_pixel_positions

    def updateProperties(self):
        #Calculate region dimensions
        self._calculateDimensions()

        #Calculate region radius
        self._calculateRadius()

        #Calculate region center position
        self._calculateCenterPosition()

    def getCenterPosition(self):
        #Return region center position
        return self.center_position

    def getTopPosition(self):
        #Return region top position
        return self.top_corner_position

    def getDimensions(self):
        #Return region dimensions
        return (self.width, self.height, self.radius)

    def getArea(self, rect_mode = True):
        if rect_mode:
            #Return area as the area of a rectangle
            return float(self.getDimensions()[0] * self.getDimensions()[1])
        else:
            #Return area as the area of a circle
            return math.pi * float(pow(self.getDimensions()[2], 2))

    def getNumberOfPixels(self):
        #Return the number of pixels
        return len(self.pixels_row_position)

    def getDensity(self, rect_mode=True):
        #Calculate pixel density of the region
        #    Density =  number_of_pixels / regional area
        area = self.getArea(rect_mode)
        if area <= 0:
            return 0
        else:
            return self.getNumberOfPixels() / self.getArea(rect_mode)

    def _calculateDimensions(self):
        #Calculate the minimum and maximum row and column of the region to determine its width and height
        min_row = int(min(self.pixels_row_position))
        max_row = int(max(self.pixels_row_position))

        min_col = int(min(self.pixels_col_position))
        max_col = int(max(self.pixels_col_position))

        #Update the region's width and height
        self.width = max_col - min_col
        self.height = max_row - min_row

        #Update the region's top corner position
        self.top_corner_position = (min_row, min_col)
        
    def _calculateRadius(self):
        #Calculate region radius from width and height using Pythagoras theorem
        self.radius = basic_header.getHypotenuse(self.width, self.height)

    def _calculateCenterPosition(self):
        #Calculate the new center position from the regions height, width, and top corner position
        row = self.top_corner_position[0] + int(self.height/2)
        col = self.top_corner_position[1] + int(self.width/2)

        #Update the region's center position
        self.center_position = (row, col)

def main():
    #TODO: Create a Demo instance of the Pixel Region class
    pass

if __name__ == "__main__":
    main()

