import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim=cv2.imread("image/lena.png")
renkli_negatif = abs(255-resim) 
cv2.imshow("Orijinal Resim",resim)
cv2.imshow("Negatif Resim",renkli_negatif)

cv2.waitKey(0)
cv2.destroyAllWindows()













