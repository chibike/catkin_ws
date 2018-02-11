#!/usr/bin/env python
from basic_header import *
from primesense import openni2
from primesense import _openni2 as c_api

class OrbbecDepthCamera(object):
    def __init__(self, depth_config=(640,480,30), color_config=(640,480,30)):
        #Initialize variables
        self._started = False
        self._device = None
        self._sensor_info = None
        self.depth_stream = None
        self.color_stream = None
        self.last_depth_frame = None
        self.last_color_frame = None
        self.depth_config = depth_config
        self.color_config = color_config
        
    def start(self):
        #If the object has not been started before
        if not self._started:
            #Setup device
            openni2.initialize()
            self._device = openni2.Device.open_any()
            self._sensor_info = self._device.get_sensor_info(openni2.SENSOR_DEPTH)

            #Create Streams
            self.depth_stream = self._device.create_depth_stream()
            self.color_stream = self._device.create_color_stream()

            #Configure streams
            self.depth_stream.set_video_mode(
                c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_100_UM,
                                   resolutionX = self.depth_config[0],
                                   resolutionY = self.depth_config[1],
                                   fps = self.depth_config[2])
                )
            self.color_stream.set_video_mode(
                c_api.OniVideoMode(pixelFormat = c_api.OniPixelFormat.ONI_PIXEL_FORMAT_RGB888,
                                   resolutionX = self.color_config[0],
                                   resolutionY = self.color_config[1],
                                   fps = self.color_config[2])
                )

            #Start streams
            self.depth_stream.start()
            self.color_stream.start()

            #Update start variable
            self._started = True
        return self._device
            
    def end(self):
        if self._started:
            #Stop Stream
            self.depth_stream.stop()
            self.color_stream.stop()
            openni2.unload()
            
        self._started = False
        
    def getDepthFrame(self, format_shape = True):
        #Ensure stream has started
        if not self._started:
            return None

        #Read new frame
        new_depth_frame = np.frombuffer(
            self.depth_stream.read_frame().get_buffer_as_uint16(), #Get data as buffer
            dtype=np.uint16                                        #New data type
            )
        
        #Set the data's shape
        if format_shape:
            new_depth_frame.shape = (
                self.depth_config[1], #Row
                self.depth_config[0], #Width
                1                     #pixel_data_width
                )

        #Update the last frame
        self.last_depth_frame = new_depth_frame

        #Return data
        return new_depth_frame
    
    def getColorFrame(self, format_shape = True):
        #Ensure stream has started
        if not self._started:
            return None

        #Read new frame
        new_color_frame = np.frombuffer(
            self.color_stream.read_frame().get_buffer_as_uint8(), #Data as buffer
            dtype=np.uint8                                       #New data type
            )

        #Set the data's shape
        if format_shape:
            new_color_frame.shape = (
                self.color_config[1], #Row
                self.color_config[0], #Width
                3                     #pixel_data_width
                )

        #Update the last frame
        self.last_color_frame = new_color_frame

        #Return data
        return new_color_frame

    def getLastDepthFrame(self):
        #Ensure stream has started
        if not self._started:
            return None

        return self.last_depth_frame

    def getlastColorFrame(self):
        #Ensure stream has started
        if not self._started:
            return None

        return self.last_color_frame

def main():
    #Create variables for Window_Name and Loop_Speed
    my_title = "My Test View"
    wait_timeout = 10

    #Create and start camera
    my_camera = OrbbecDepthCamera()
    my_camera.start()

    #Select frame to view
    show_color_frame = True

    #Create image window
    createNormalWindow(my_title)

    #Start main loop
    frame = None
    while True:

        #Select frame to draw
        if show_color_frame:
            frame = my_camera.getColorFrame()
        else:
            frame = my_camera.getDepthFrame()

        #Ensure frame is valid
        if type(frame) == type(None):
            print "Error: Invalid Frame"
            break

        #Display the frame
        showFrame(my_title, frame)

        #Wait for ESC key to exit
        key = cv2.waitKey(wait_timeout) #wait would timeout after <wait_timeout> ms.
        if key == 27:
            break

    #Close all open windows and stop the camera
    destroyWindows()
    my_camera.end()

if __name__ == "__main__":
    print "Staring","orbbec_class"
    main()
