import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('image/lena.png',0)
rows,cols = resim.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
cıktı = cv2.warpAffine(resim,M,(cols,rows))


plt.subplot(121),plt.imshow(resim,cmap = 'gray')
plt.title('Orijinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cıktı,cmap = 'gray')
plt.title('Ters Resim'), plt.xticks([]), plt.yticks([])

plt.show()