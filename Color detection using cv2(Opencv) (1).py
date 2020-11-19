#!/usr/bin/env python
# coding: utf-8

# # Color identification in images using Opencv(cv2)

# In[1]:


# before proceeding with the program make sure that you have installed these libraries
#pip install cv2
#pip install opencv-python
#pip install numpy
#pip install pandas


# # Importing the packages and performing the Color Detection

# In[2]:


import numpy as np
import pandas as pd
import cv2


# In[3]:


#Reading the image and reading the csv file to give the name of the color detected from the dataset.

img = cv2.imread('Downloads/color_detection_testimage.jpg')
index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('C:/Users/Shivamani/Downloads/colors.csv', names=index, header=None)


# In[4]:


# Declaring the Global variables

clicked = False
r = g = b = xpos = ypos = 0


# In[5]:


# Creating a fucnction to undergo the Color detection process

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


# In[6]:


#Creating a function to record the mouse click action to pick the color to be recognised and to give the output

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[7]:


#The output of the color and the source image will be called and displayed .

cv2.namedWindow('Color Recognition')
cv2.setMouseCallback('Color Recognition', mouse_click)
while(1):
    cv2.imshow("Color Recognition",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
            #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
        
cv2.destroyAllWindows()


# In[ ]:




