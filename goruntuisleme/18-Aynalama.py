import cv2
import matplotlib.pyplot as plt
import numpy as np 


resim=cv2.imread("image/lena.png")

aynalananResim= cv2.copyMakeBorder(resim,0,0,512,0,cv2.BORDER_REFLECT)

cv2.imshow("Aynalama",aynalananResim)
cv2.waitKey(0)
cv2.destroyAllWindows()