import cv2
import numpy as np
from matplotlib import pyplot as plt


def template_match(image,cropped):
    t=[]
    t.append(cv2.imread('/home/arjun-pili/drosophila/T1.jpeg'))
    t.append(cv2.imread('/home/arjun-pili/drosophila/T2.jpeg'))
    t.append(cv2.imread('/home/arjun-pili/drosophila/T3.jpeg'))
    t.append(cv2.imread('/home/arjun-pili/drosophila/T4.jpeg'))
    res=[]
    max_loc=[]
    
    for i in range (4):
        img=image[cropped[i][0]:cropped[i][1],cropped[i][2]:cropped[i][3]]
        res.append(cv2.matchTemplate(img,t[i],cv2.TM_CCOEFF_NORMED))
        max_loc.append(cv2.minMaxLoc(res[i])[3])
    
    return max_loc
    