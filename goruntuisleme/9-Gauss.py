import cv2
import matplotlib.pyplot as plt
import numpy as np  

resim= cv2.imread("image/gauss.png")
cv2.imshow("Orijinal Resim",resim)
gauss = cv2.GaussianBlur(resim, (5, 5), 5)
cv2.imshow("Filtrelenmis Resim",gauss)

cv2.waitKey(0)
cv2.destroyAllWindows()