import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread('image/lena.png')
BuyukResim=cv2.pyrUp(resim)


cv2.imshow("Orijinal resim",resim)
cv2.imshow("Buyuk resim",BuyukResim)

cv2.waitKey(0)
cv2.destroyAllWindows()