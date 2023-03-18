import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('image/lena.png',0)
rows,cols = resim.shape

M = np.float32([[1,0,100],[0,1,50]])
cıktı = cv2.warpAffine(resim,M,(cols,rows))

plt.subplot(121),plt.imshow(resim,cmap = 'gray')
plt.title('Orijinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cıktı,cmap = 'gray')
plt.title('Ötelenmiş Resim'), plt.xticks([]), plt.yticks([])

plt.show()