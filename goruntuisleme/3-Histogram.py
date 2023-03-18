import cv2
import matplotlib.pyplot as plt
import numpy as np 

resim= cv2.imread("image/grilena.png",0)


cv2.imshow("Grilestirilmis Resim",resim)
plt.hist(resim.ravel(),256,[0,256]); plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

