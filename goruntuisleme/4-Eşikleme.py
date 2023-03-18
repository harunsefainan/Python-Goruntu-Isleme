import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim= cv2.imread("image/grilena.png")
cv2.imshow("Grilestirilmis Resim",resim)
(thresh, blackAndWhiteImage) = cv2.threshold(resim, 100, 255, cv2.THRESH_BINARY)#eşikleme kodu

plt.imshow(blackAndWhiteImage)
plt.show()      