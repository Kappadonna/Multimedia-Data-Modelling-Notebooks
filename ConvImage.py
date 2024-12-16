#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[27]:


k = np.random.randint(0,2,(3,3))
k
k = np.array([[-1,0,-1], [0,4,0],[-1,0,-1]])  #filtro laplaciano


# In[4]:


import cv2


# In[16]:


img = cv2.imread('OneDrive\Desktop\image.png', 0)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[28]:


convI = np.zeros(img.shape)
N = img.shape[0]
M = img.shape[1]
for i in range(1,N-2):
    for j in range(1,M-2):
        subpatch = img[i-1:i+2, j-1:j+2]
        multresults = subpatch*k
        somma = np.sum(multresults)
        convI[i,j] = somma


# In[29]:


cv2.imshow("convImage", convI)
cv2.waitKey(0)
cv2.destroyAllWindows()

