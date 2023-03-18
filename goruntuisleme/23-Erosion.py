import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/morfoloji2.jpeg')
kernel = np.ones((5,5),np.float32)/25
erosion = cv2.erode(resim,kernel,iterations = 1)

cv2.imshow('Original Resim', resim)
cv2.imshow('Filtrelenmis Resim', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()