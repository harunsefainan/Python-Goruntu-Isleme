import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim = cv2.imread('image/kontrast germe.png',0) 


minmax_img = np.zeros((resim.shape[0],resim.shape[1]),dtype = 'uint8')


for i in range(resim.shape[0]):
    for j in range(resim.shape[1]):
        minmax_img[i,j] = 255*(resim[i,j]-np.min(resim))/(np.max(resim)-np.min(resim))


cv2.imshow("Orijinal Resim",resim)
cv2.imshow("Filtrelenmis Resim",minmax_img)

cv2.waitKey(0)
cv2.destroyAllWindows()