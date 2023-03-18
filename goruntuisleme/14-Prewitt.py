import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/lena.png')
grilena = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
resim_gaussian = cv2.GaussianBlur(grilena,(3,3),0)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(resim_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(resim_gaussian, -1, kernely)

plt.subplot(121),plt.imshow(img_prewittx,cmap = 'gray')
plt.title('Prewitt X'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_prewitty,cmap = 'gray')
plt.title('Prewitt Y'), plt.xticks([]), plt.yticks([])

plt.show()