import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\ManoBharathi\\Desktop\\q.png',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,3,255,cv2.THRESH_BINARY)

titles = ['Original Image', 'Global Thresholding']
images = [img, th1]

for i in range(2):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite('C:\\Users\\ManoBharathi\\Desktop\\sun\\q78.png',th1)
