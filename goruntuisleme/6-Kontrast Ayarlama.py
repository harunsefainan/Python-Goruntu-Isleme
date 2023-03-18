import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('image/lena.png') 
alpha=3
beta=10
adjusted = cv2.convertScaleAbs(resim, alpha=alpha, beta=beta)

cv2.imshow("Orijinal Resim",resim)
cv2.imshow('Kontrast Resim', adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()












