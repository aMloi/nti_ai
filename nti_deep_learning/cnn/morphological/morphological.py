# -*- coding: utf-8 -*-
"""morphological.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1heu2358p6i3HT1Kfi0SI9Dam0qeCsaG5
"""

import cv2 as cv
import numpy as np
img = cv.imread('j.png',0)

from google.colab.patches import cv2_imshow

cv2_imshow(img)

kernel=np.ones((5,5),np.uint0)
kernel

erosion = cv.erode(img,kernel,iterations=1)

cv2_imshow(erosion)

#dilationis opp of eroison

dilation=cv.dilate(img,kernel,iterations=1)

cv2_imshow(dilation)

img2 = cv.imread('jj.png',0)
cv2_imshow(img2)

opening = cv.morphologyEx(img,cv.MORPH_OPEN,kernel,iterations=1)

cv2_imshow(opening)

img3 = cv.imread('jjj.png',0)
cv2_imshow(img3)

# close when the noise inside the object
# opening when the noise is outside
from contextlib import closing
closing2=cv.morphologyEx(img3,cv.MORPH_CLOSE,kernel,iterations=3)

cv2_imshow(closing2)






















