#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cv2
import math

def show(img):
    plt.imshow(img)
    plt.show()
    
def isWithinPercentage(num, reference_num, percentage):
    threshold_range = reference_num * percentage
    if num >= (reference_num - threshold_range) and num <= (threshold_range + reference_num):
        return True
    else:
        return False

def getPercentageDifference(x, y, num_range):
    diff = abs(x-y)
    p_diff = max(min(float(diff)/float(num_range), 1.0), 0.0)
    return p_diff

def colorDifference(color1, color2):
    diff = pow(color1[0] - color2[0], 2) + pow(color1[1] - color2[1], 2) + pow(color1[2] - color2[2], 2)
    return math.sqrt(diff) * 0.5773502691896257

def mapf(x, in_min, in_max, out_min, out_max):
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min)) + out_min

def mapArrayf(data, in_min, in_max, out_min, out_max):
    print "in_min",in_min
    print "in_max",in_max
    print "out_min",out_min
    print "out_max",out_max
    new_data = []
    for i in range(len(data)):
        new_data.append( int(mapf(data[i], in_min, in_max, out_min, out_max)) )
    return new_data
    
def constrainf(x, out_min, out_max):
    return min(max(x, out_min), out_max)

def get1dIndex(row, col, number_of_col):
    return col + (row*number_of_col)

def getDistanceBetweenPoint(point_1, point_2):
    #Returns distance bwt points
    return math.sqrt( pow(point_2[0] - point_1[0], 2) + pow(point_2[1] - point_1[1], 2) )

def getHypotenuse(width, height):
    return math.sqrt( pow(width, 2) + pow(height, 2) )

def showFrame(title, frame, rgb_mode=True):
    if type(frame) == type(None):
        print "Error: Invalid Frame Type"
        return
    if rgb_mode:
        cv2.imshow(title, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    else:
        cv2.imshow(title, frame)

def getOverlappingRectDimensions(pos_1, dimens_1, pos_2, dimens_2):
    overlapping_rect_length = min(dimens_1[0] - abs(pos_2[1] - pos_1[1]), dimens_2[0])
    overlapping_rect_height = min(dimens_1[1] - abs(pos_2[0] - pos_1[0]), dimens_2[1])
    return (overlapping_rect_length, overlapping_rect_height)

def createNormalWindow(title="image"):
    cv2.namedWindow(title, cv2.WINDOW_NORMAL)

def destroyWindows():
    cv2.destroyAllWindows()

def printFrameProperties(title, frame):
    print "--",title,"---"
    print "Frame type =",type(frame)
    print "Frame length =",len(frame)
    print "Frame min =",min(frame)
    print "Frame max =",max(frame)
    print "Frame[0] =",frame[0]

def normalizef(x, min_val, max_val):
    return mapf(x, min(x.ravel()), max(x.ravel()), min_val, max_val)

def getRateOfChange(x):
    return x[:-1] - x[1:]

def checkSignChange(x):
    x[np.where(x >= 0)] = 1
    x[np.where(x < 0)] = 0
    return x

def getRateOfChange_SignBased(x, nom_min, nom_max):
    x[:,0] = normalizef(x[:,0], nom_min, nom_max)
    x[:,1] = normalizef(x[:,1], nom_min, nom_max)
    
    x[:-1,0] = getRateOfChange(x[:,0])
    x[:-1,1] = getRateOfChange(x[:,1])
    
    x[:-1,0] = checkSignChange(x[:-1,0])
    x[:-1,1] = checkSignChange(x[:-1,1])
    
    return x

def getMatchIndex(x, max_index):
    minimum_match_score = np.average(np.absolute(x[:,0] - x[:,1]))
    minimum_match_index = 0
    
    for index in range(1, max_index):
        match_score = np.average(np.absolute(x[:-index,0] - x[index:,1]))
        if match_score < minimum_match_score:
            minimum_match_score = match_score
            minimum_match_index = index

    for index in range(1, max_index):
        match_score = np.average(np.absolute(x[index:,0] - x[:-index,1]))
        if match_score < minimum_match_score:
            minimum_match_score = match_score
            minimum_match_index = -index

    return (minimum_match_index, minimum_match_score)

def getLeadIndexf(datain, nom_min=-1, nom_max=1, max_index=100):
    x = np.copy(datain)
    x = getRateOfChange_SignBased(x, nom_min, nom_max)
    return getMatchIndex(x, max_index)
