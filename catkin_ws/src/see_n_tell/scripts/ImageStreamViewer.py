#!/usr/bin/env python

#Import support libraries for buffer formatting and other specialists functions
import basic_header
import numpy as np
import cv2

class Viewer(object):
    def __init__(self, window_title="image"):
        #Create setup variables
        self._created = False
        self.color_config=(640,480,30)
        self.title = window_title

        #Set start frame to a demo image :) Better than setting the start frame to all zeros
        self.frame = cv2.imread("pic_01.jpg")

        self.created = False

    def start(self):
        if not self.created:
            basic_header.createNormalWindow(self.title)

        self.created = True

    def end(self):
        self.created = False
        basic_header.destroyWindows()
        exit()

    def updateView(self, rgb_mode=True):
        if self.created:
            basic_header.showFrame(self.title, self.frame, rgb_mode)
            key = cv2.waitKey(300)
            if key == 27:
                self.end()

    
