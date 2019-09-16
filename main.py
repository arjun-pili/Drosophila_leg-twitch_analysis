from imagecrop import imagecrop
from template_match import template_match
import cv2
import numpy as np
import os
from math import sqrt
from os.path import join
import csv
import glob

#iterate through images.
dist=[[],[],[],[]] #2D array with 4 rows.
count=0

path='/home/arjun-pili/drosophila/MLP/'
for filename in sorted(glob.glob(path+'*.jpeg')):
    
    try:
        image=cv2.imread(join(path,filename))
        cropped=imagecrop(image)
        rect_points=template_match(image,cropped)
       # print(rect_points,filename)
        
        for i in range (4):
            dist[i].append(rect_points[i])
    except:
        count+=1

print(count)
x=[]
y=[]
l1=[]
loop=0
for leg in dist:
    #x1=leg[0][0]
    #y1=leg[0][1]
    l1.append(['time','leg1','leg2','leg3','leg4'])
    for i in range(4):
        x2=leg[i][0]
        y2=leg[i][1]
        #res=(pow(x2-x1,2)+pow(y2-y1,2))
        if(loop==0):
            l1.append([i,(x2,y2)])
        else:
            l1[i-1].extend([(x2,y2)])

    loop=1
    print (l1)



#with open('MLP.csv','w') as csvf:
#    writer=csv.writer(csvf)
#    writer.writerows(l1)
#csvf.close()
    
