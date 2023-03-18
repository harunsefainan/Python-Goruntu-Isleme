import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/medyan.png')

filteredImg = cv2.medianBlur(resim, ksize=3)

cv2.imshow('Original Resim', resim)
cv2.imshow('Filtrelenmis Resim', filteredImg)

cv2.waitKey(0)
cv2.destroyAllWindows()







