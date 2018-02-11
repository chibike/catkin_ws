#!/usr/bin/env python

#Setup import files from the manifest file
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)
import rospy

#Import support libraries for buffer formatting and other specialists functions
import basic_header
import ObjectShapes
import struct
import numpy as np
import cv2
import math

#Import the necessary message formats needed
from see_n_tell.msg import Int32Array
from see_n_tell.msg import TaggedObjects

class TagObjects(object):
    def __init__(self, fps=7):
        #Create setup variables
        self._created = False
        self.color_config=(640,480,30)
        self.depth_config=(640,480,30)

        #Set start frames to None
        self.color_frame = None
        self.depth_frame = None

        #Initialize this module as a rospy node
        rospy.init_node("tag_objects", anonymous=True)

        #Setup publish data rate
        self.fps = basic_header.constrainf(fps, 1, 30) #constrain the fps to 1-30 Hz
        self.rate = rospy.Rate(self.fps)

        #Setup publisher
        self.tagged_objects_pub = rospy.Publisher("TaggedObjects_1", TaggedObjects, queue_size=10)

        #Create buffer for data to send
        self.tagged_objects = TaggedObjects()

        
        #Setup the buffers for data to send
        self.clearTaggedObjectsData()
        
        #Create and array to keep track of objects in the frame
        self.objects_buffer = []
        self.scrap_objects_buffer = []
        

    def start(self):
        if not self._created:
            #Subscribe to ColorData_1 ros_topic
            rospy.Subscriber("ColorData_1", Int32Array, self.color_callback)
            rospy.Subscriber("DepthData_1", Int32Array, self.depth_callback)

        #Update the created variable
        self._created = True

    def end(self):
        #Update the created variable
        self._created = False

        #Exit program
        exit()

    def run(self):
        while not rospy.is_shutdown() and self._created:
            #Get image sections
            sections = self.splitImageIntoSections()

            #Extract the contour locations from the frame diff
            self.extractObjectsData(sections)

            #print "Publishing tracked data..."

            #Publish data
            self.publishTrackedData()

            #Maintain frame rate
            self.rate.sleep()           

    def publishTrackedData(self):
        #Exit function if the object has not created
        if not self._created or len(self.tagged_objects.row) <= 0:
            return None

        #Publish data
        self.tagged_objects_pub.publish(self.tagged_objects)
    
    def clearTaggedObjectsData(self):
        self.tagged_objects.row    = []
        self.tagged_objects.column = []
        self.tagged_objects.depth  = []
        self.tagged_objects.width  = []
        self.tagged_objects.height = []
        self.tagged_objects.tag   = []
    
    def appendObject(self, row, column, depth, width, height, tag_data):
        self.tagged_objects.row.append(row)
        self.tagged_objects.column.append(column)
        self.tagged_objects.depth.append(depth)
        self.tagged_objects.width.append(width)
        self.tagged_objects.height.append(height)
        self.tagged_objects.tag.append(tag_data)
    
    def color_callback(self, data):
        #Retreive data and convert it to a numpy array
        self.color_frame = np.array(data.data, dtype=np.int32).astype(np.uint8)

        #Describe the shape of the data
        self.color_frame.shape = (self.color_config[1], self.color_config[0], 3)

    def depth_callback(self, data):
        #Retreive data and convert it to a numpy array
        self.depth_frame = np.array(data.data, dtype=np.int32)

        #Map data from 0, 33559 to 0, 255 and convert it to an unsigned 8bits int
        self.depth_frame = basic_header.mapf(
            self.depth_frame.astype(np.float32).ravel(), #Trying to force float division during mapping
            0,
            33559,
            0,
            255
          ).astype(np.uint8)

        #Describe the shape of the data
        self.depth_frame.shape = (self.depth_config[1], self.depth_config[0])
        
    def isValid(self, frame, config):
        try:
            if tuple(frame.shape) == (config[1], config[0], 3):
                return True
            elif tuple(frame.shape) == (config[1], config[0], 1):
                return True
            elif tuple(frame.shape) == (config[1], config[0]):
                return True
            else:
                return False
        except:
            return False
        
    def splitImageIntoSections(self, use_depth=False):
        if use_depth:
		    #Create buffer to store the image sections
		    depth_frame_sections = None
		    
		    if self.isValid(self.depth_frame, self.depth_config):
		        #Blurify the image using a 15 by 15 kernel to reduce noise
		        depth_frame_sections = cv2.GaussianBlur(self.depth_frame, (15, 15), 0)
		        
		        #Get edges
		        depth_frame_sections = cv2.Laplacian(depth_frame_sections, cv2.CV_8U)
		        #depth_frame_sections = cv2.Canny(depth_frame_sections, 5, 240)
		        
		        #Expand pixels to join them
		        for i in range(3):
		            depth_frame_sections = cv2.dilate(depth_frame_sections, (5,5))
		            
		        #Reduce pixels to make lines thinner
		        for i in range(3):
		            depth_frame_sections = cv2.erode(depth_frame_sections, (5,5))
		            
		    #Returns an sections as edges in the frame
		    return depth_frame_sections
        else:
            #Create buffer to store the image sections
            color_frame_sections = None

            if self.isValid(self.color_frame, self.color_config):
                #Convert image to grayscale
                color_frame_sections = cv2.cvtColor(self.color_frame, cv2.COLOR_BGR2GRAY)
                
                #Blurify the image using a 5 by 5 kernel to reduce noise
                color_frame_sections = cv2.GaussianBlur(color_frame_sections, (3, 3), 0)

                #Get edges
                color_frame_sections = cv2.Canny(color_frame_sections, 60, 100)

                #Expand pixels to join them
                for i in range(3):
                    color_frame_sections = cv2.dilate(color_frame_sections, (15,15))

                #Reduce pixels to make lines thinner
                #for i in range(3):
                #    color_frame_sections = cv2.erode(color_frame_sections, (5,5))

            #Returns an sections as edges in the frame
            return color_frame_sections
    
    def extractObjectsData(self, sections):
        #Create buffer to store the contour data
        depth_contours = []

        #Verify that the section is valid
        if type(sections) != type(None):
            depth_contours = cv2.findContours(
                sections,
                mode=cv2.RETR_TREE,
                method=cv2.CHAIN_APPROX_SIMPLE,
                offset=(0, 0)
                )[1]

        #Clear the data to send buffer
        self.clearTaggedObjectsData()

        #Get the objects from the contour information
        objects = self.objects_buffer + self.scrap_objects_buffer
        self.objects_buffer = []
        self.scrap_objects_buffer = []
        
        morph_params = []
        for contour in depth_contours:
            contour.shape = (contour.shape[0], 2)
            obj = ObjectShapes.Object(contour.tolist())
            area = obj.getArea()
            if area < 1: continue
            #if area >= 60000: continue
            
            if self.isValid(self.color_frame, self.color_config):obj.setColor(self.color_frame)
            if self.isValid(self.depth_frame, self.depth_config):obj.setDepth(self.depth_frame)
            
            for index in range(len(objects)):
                #print "obj =",objects
                if objects[index].isSameObject(obj):
                    morph_params.append( objects[index].morphIntoObject(obj) )
                    self.objects_buffer.append(objects[index])
                    
                    #Remove object
                    objects = objects[:index] + objects[index+1:]
                    break
                    
            self.scrap_objects_buffer.append(obj)
        
        objects = []
        morph_params_dup = []
        for i in range(len(self.objects_buffer)):
            objb_dr,objb_dc,_ = morph_params[i][1]
            
            found = False
            for j in range(len(objects)):
                obj_dr,obj_dc,_ = morph_params_dup[j][1]
                if basic_header.isWithinPercentage(obj_dr, objb_dr, 0.25) and basic_header.isWithinPercentage(obj_dc, objb_dc, 0.25):
                    objects[j].addPixelPositions(self.objects_buffer[i].getPixelPositions())
                    found = True
                    break
            
            if not found:
                objects.append(self.objects_buffer[i])
                morph_params_dup.append(morph_params[i])
        
        #print morph_params
        #print len(self.objects_buffer),len(objects)
        
        for obj in objects:
            width,height = obj.getDimensions()[0:2]
            row,column = obj.getTopPosition()
            tag_data = obj.getTagData()
            
            data = ""# "H"+str(tag_data[3][0])+" D"+str(tag_data[4])+" S"+str(tag_data[3][1])+" B"+str(tag_data[3][2])
            
            self.appendObject(
                row,
                column,
                depth = tag_data[4],
                width = width,
                height = height,
                tag_data = data
                )


def main():
    #Create a tagger object
    my_object_tagger = TagObjects()

    #Start the tagger
    my_object_tagger.start()

    #Run the tagger
    my_object_tagger.run()

    #End the tagger
    my_object_tagger.end()

#Run the main function if this program is running directly
if __name__ == "__main__":
    main()

