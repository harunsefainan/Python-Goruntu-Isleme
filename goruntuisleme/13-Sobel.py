import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/grilena.png')

sobelx = cv2.Sobel(resim,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(resim,cv2.CV_64F,0,1,ksize=5)  # y

plt.subplot(121),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()