import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/grilena.png')

laplacian = cv2.Laplacian(resim, cv2.CV_64F)

plt.subplot(121),plt.imshow(resim,cmap = 'gray')
plt.title('Orijinal Resim'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplace Filtresi'), plt.xticks([]), plt.yticks([])

plt.show()



