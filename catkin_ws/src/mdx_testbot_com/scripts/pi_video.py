#!/usr/bin/env python

import os
import cv2
import time
import pi_color
import numpy as np
import matplotlib.pyplot as plt

PACKAGE_NAME = "mdx_testbot_com"
ABS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
IMAGE_DIR = "{0}/{1}/images/".format(ABS_FILE_PATH[:ABS_FILE_PATH.rfind("/{0}".format(PACKAGE_NAME))], PACKAGE_NAME)

class Camera(object):
    def __init__(self, device_id=1):
        self.started = False
        self.cap = None
        self.device_id = device_id

    def start(self):
        if not self.started:
            self.started = True
            self.cap = cv2.VideoCapture(self.device_id)
        return self.started

    def stop(self):
        if self.started:
            self.started = False
            self.cap.release()
        return not self.started

    def get_next_frame(self):
        if not self.started: return self.started
        self.ret, self.frame = self.cap.read()
        return self.frame

    def get_prev_frame(self):return self.frame

class StaticImage(object):
    def __init__(self, image_name=""):
        self.started = False
        self.frame = None
        self.image_name = image_name

    def start(self):
        self.frame = cv2.imread(self.image_name)

    def stop(self):
        self.started = False
        self.frame = None
        return not self.started

    def get_next_frame(self):
        return self.frame

    def get_prev_frame(self):
        return self.frame

class Viewer(object):
    def __init__(self, fps=10, title="frame"):
        self.started = False
        self.title = title
        self.fms = int(1000.0/fps)

    def start(self):
        if not self.started:self.started = True
        return self.started

    def stop(self):
        if self.started:
            self.started = False
            cv2.destroyAllWindows()
        return not self.started

    def show_frame(self, frame):
        if not self.started: return False
        cv2.imshow(self.title, frame)
        if (cv2.waitKey(self.fms) & 0xFF) == ord('q'):return self.started
        else:return False

class FrameAnalyzer(object):
    def __init__(self, num_of_trails=5):
        self.num_of_frames = num_of_trails
        self.frames = []

    def update_frame(self, frame):
        if type(frame) == type(None): return None
        self.frames.append(frame)
        if len(self.frames) > self.num_of_frames:
            #Delete oldest frame
            self.frames = self.frames[1:]
        return True

    def get_current_frame(self):
        return self.frames[-1]

    def get_image_trace(self):
        return self._image_trace(self.get_current_frame())

    def get_chunks_trace(self, intensity=4):
        frame = self._boxify(np.copy(self.get_current_frame()), intensity)
        return self._image_trace(frame)

    def get_as_boxified(self, factor=2):
        return self._boxify(np.copy(self.get_current_frame()), factor)

    def overlay_frame(self, bk_frame, color=(0,255,0)):
        self.frames[-1] = self._overlay_frame(self.get_current_frame(), bk_frame, color)
        return self.get_current_frame()

    def _get_colors(self, frame):
        #Get the unique set of colors used in this frame
        frame_shape = frame.shape
        frame.shape = (frame_shape[0]*frame_shape[1], frame_shape[2])
        colors = tuple(set(tuple([tuple(i) for i in frame.tolist()])))
        return colors

    def _overlay_frame(self, frame, bk_frame, color=(0,255,0)):
        frame[np.where(bk_frame == 255)] = color
        return frame
    
    def _boxify(self, frame, factor):
        frame_width,frame_height,_ = np.shape(frame)
        frame = cv2.resize(frame, (frame_height/factor, frame_width/factor))
        #frame = cv2.GaussianBlur(frame, (3, 3), 0)
        frame = cv2.resize(frame, (frame_height, frame_width))
        #kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        #frame = cv2.filter2D(frame, -1, kernel)
        return frame

    def _image_trace(self, frame):
        if np.shape(frame) != (480, 640, 3): return None
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Blur frame using a (5 by 5) kernel to reduce noise
        frame = cv2.GaussianBlur(frame, (5, 5), 0)
        #Get canny edges from frame
        frame = cv2.Canny(frame, 60, 100)
        #Expand edges to merge shorter edges
        for i in range(5):frame = cv2.dilate(frame, (15,15))
        #Erode edges to reduce edges thickness
        for i in range(5):frame = cv2.erode(frame, (5,5))
        return frame

    def _extract_contours(self, bk_frame):
        try:
            b = bk_frame.ravel().tolist()
            if b.count(0) + b.count(255) != len(b): return None
        except: return None

        contours = cv2.findContours(bk_frame,
                                    mode=cv2.RETR_TREE,
                                    method=cv2.CHAIN_APPROX_SIMPLE,
                                    offset=(0, 0)
                                    )[1]
        return contours

def simplify_image(frame, color_array=pi_color._PRE_DEF__MAIN_01):
    rows,cols,_ = np.shape(frame)
    for row in xrange(rows):
        for col in xrange(cols):
            bgr = frame[row, col]
            color = pi_color.RGBColor((bgr[2],bgr[1],bgr[0]))
            color = pi_color.simplify(color, color_array)
            frame[row, col] = color.get_bgr()
    return frame

def main_video():
    #Create objects
    my_camera = Camera(); my_camera.start()
    my_viewer = Viewer(); my_viewer.start()
    #Create frame analyzer
    my_analyzer = FrameAnalyzer(num_of_trails=1)
    
    while True:
        if ( my_analyzer.update_frame( my_camera.get_next_frame() ) ):
            detailed_trace = my_analyzer.get_image_trace()
            chunks_trace = my_analyzer.get_chunks_trace(10)
            #my_analyzer.overlay_frame(detailed_trace, color=(255,0,0))
            my_analyzer.overlay_frame(chunks_trace, color=(0,255,0))
            if my_viewer.show_frame( my_analyzer.get_as_boxified(10) ): break
            #if my_viewer.show_frame( my_analyzer.get_current_frame() ): break

    #End objects
    my_camera.stop()
    my_viewer.stop()
    return my_camera,my_viewer

def main_still(image_name="comp_001.jpeg"):
    #Create objects
    my_still = StaticImage(IMAGE_DIR + image_name); my_still.start()
    my_viewer = Viewer(); my_viewer.start()

    frame = my_still.get_next_frame()
    frame = simplify_image(frame)
    
    while True:
        if my_viewer.show_frame( frame ): break

    #End objects
    my_still.stop()
    my_viewer.stop()
    return my_still,my_viewer

def test_particular_image(image_name="comp_003.jpeg"):
    start_time = 0
    simplify_time = 0
    color_clusters_time = 0

    #Create objects
    my_still = StaticImage(IMAGE_DIR + image_name); my_still.start()
    my_viewer = Viewer(); my_viewer.start()

    frame = my_still.get_next_frame()

    start_time = time.time()
    frame = simplify_image(frame)
    simplify_time = time.time() - start_time

    start_time = time.time()
    color_clusters = pi_color.get_as_color_clusters(frame)
    color_clusters_time = time.time() - start_time

    print "Length: {0}".format(len(color_clusters))
    print "simplify time: {0}".format(simplify_time)
    print "color_clusters time: {0}".format(color_clusters_time)

    data = [(color_cluster.radius, color_cluster.color.rgb_color, color_cluster.position) for color_cluster in color_clusters]

    
    f = lambda x: x[0]
    #r = list(zip(radai,colors,positions))
    s = sorted(data, key=f)
    print s

    counter = 0
    frame = np.zeros(np.shape(frame))
    for color_cluster in color_clusters:
        color_cluster.draw(frame, fill=color_cluster.color)
        print "progress: {0}%".format(counter/len(color_clusters)*100.0)
        counter += 1

    
    while True:
        if my_viewer.show_frame( frame ): break

    #End objects
    my_still.stop()
    my_viewer.stop()
    return my_still,my_viewer,color_clusters

def test_particular_image_2(image_name="comp_003.jpeg"):
    #Create objects
    my_still = StaticImage(IMAGE_DIR + image_name); my_still.start()

    img = my_still.get_next_frame()
    print "Main ..."
    
    sim_img = simplify_image(np.copy(img))
    print "Simple ..."

    plt.subplot(121); ax = plt.imshow(img);
    plt.subplot(122); ax = plt.imshow(sim_img);
    plt.show()

    color_clusters = pi_color.get_as_color_clusters(np.copy(sim_img))
    print "Processed Clusters ..."

    counter = 0
    for color_cluster in color_clusters:
        clu_frame = np.zeros(np.shape(img), dtype=np.uint8)
        color_cluster.draw(clu_frame, fill=color_cluster.color)
        
        print "Showing color cluster {0}".format(counter)
        print "Color    : {0}".format(color_cluster.color.rgb_color)
        print "Radius   : {0}".format(color_cluster.radius)
        print "position : {0}".format([color_cluster.position[1], color_cluster.position[0]])

        plt.subplot(111); ax = plt.imshow(clu_frame);
        plt.show()

        counter += 1

    clu_frame = np.zeros(np.shape(img), dtype=np.uint8)
    for color_cluster in color_clusters:
        color_cluster.draw(clu_frame, fill=color_cluster.color)
    print "Color Clustified ..."

    print "Number of clusters := {0}".format(len(color_clusters))

    plt.subplot(221); ax = plt.imshow(img);# ax.title.set_text("main")
    plt.subplot(222); ax = plt.imshow(sim_img);# ax.title.set_text("simple")
    plt.subplot(223); ax = plt.imshow(clu_frame);# ax.title.set_text("color clustified")
    plt.show()

    #End objects
    my_still.stop()
    return my_still,color_clusters

def test_all_images_for_main_still():
    c,v = None, None
    image_names = [i for i in os.listdir(IMAGE_DIR)]
    for image_name in image_names:
        print "using image:{0}".format(image_name)
        c,v = main_still(image_name)
    return c,v

#If code is running directly run the main function
if __name__ == '__main__':
    #main_still(image_name="comp_001.jpeg")
    #c,c_c = test_particular_image_2("comp_002.jpeg")
    #c,v,c_c = test_particular_image("comp_004.jpeg")
    #c,v = test_all_images_for_main_still()

    color = pi_color.RGBColor((0, 0, 0))
    color = pi_color.simplify(color, pi_color._PRE_DEF__MAIN_01)
    print color.rgb_color
