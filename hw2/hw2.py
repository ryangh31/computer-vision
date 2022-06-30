#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
img = cv2.imread('noise_image.png')
Height, width, channels = img.shape[:3]
Mean_img= np.zeros((Height, width, 1), np.uint8)
Median_img= np.zeros((Height, width, 1), np.uint8)


# In[2]:


# mean filter 
def Meanfilter(x,y,noiseimg):
    mean_value=0
    for i in range(0,3):
        for j in range(0,3):
            mean_value=mean_value+noiseimg[x+i,y+j,0]
    mean_value=mean_value//9
    return mean_value

for i in range(0,Height-2):
        for j in range(0,width-2):
            Mean_img[i+1,j+1,0]=Meanfilter(i,j,img)
cv2.imwrite('output1.png',Mean_img)   



# In[3]:


# median filter
def Medianfilter(x,y,a):
    for n in range(0,8):
        for i in range(0,3):
            for j in range(0,3):
                nc=i
                nr=j+1
                if(j==2):
                    nc=(i+1)
                    nr=0
                    if(nc==3):
                        break
                if(a[x+i,y+j,0]>a[x+nc,y+nr,0]):
                    temp=a[x+i,y+j,0]
                    a[x+i,y+j,0]=a[x+nc,y+nr,0]
                    a[x+nc,y+nr,0]=temp
                    
    return a[x+1,y+1,0]

for i in range(0,Height-2):
        for j in range(0,width-2):
            Median_img[i,j,0]=Medianfilter(i,j,img)
cv2.imwrite('output2.png',Median_img)



