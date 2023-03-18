import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread("image/mean.png")
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(resim,-1,kernel)

cv2.imshow('Original Resim', resim)
cv2.imshow('Filtrelenmis Resim', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()










