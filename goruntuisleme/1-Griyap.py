import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim= cv2.imread("image/lena.png")

resimGri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)#gri kodu

cv2.imshow("Orijinal",resim)
cv2.imshow("Grilestirilmis Resim",resimGri)

cv2.waitKey(0)
cv2.destroyAllWindows()













