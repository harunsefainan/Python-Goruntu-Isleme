import cv2
import numpy as np
import matplotlib.pyplot as plt

foto=cv2.imread("image/grilena.png")
kernel = np.ones((5,5),np.uint8)
gradient= cv2.morphologyEx(foto, cv2.MORPH_GRADIENT, kernel)

plt.subplot(121), plt.imshow(foto), plt.title("Orijinal Resim")
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(gradient), plt.title("Gradient")
plt.xticks([]), plt.yticks([])
plt.show()