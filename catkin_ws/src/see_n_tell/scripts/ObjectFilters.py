import basic_header
import math
import colorsys
import numpy as np

def getPercentageDifference(x, y, num_range):
    diff = abs(x-y)
    p_diff = max(min(float(diff)/float(num_range), 1.0), 0.0)
    return p_diff

def colorDifference(color1, color2):
    diff = pow(color1[0] - color2[0], 2) + pow(color1[1] - color2[1], 2) + pow(color1[2] - color2[2], 2)
    return math.sqrt(diff) * 0.5773502691896257

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
