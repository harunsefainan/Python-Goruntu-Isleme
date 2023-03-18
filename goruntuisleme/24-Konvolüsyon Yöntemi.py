import cv2
import numpy as np
from matplotlib import pyplot as plt

resim=cv2.imread("image/netlestirme.PNG",0)


box_blur_ker = np.array([[0.1111111, 0.1111111, 0.1111111],
                    [0.1111111, 0.1111111, 0.1111111],
                    [0.1111111, 0.1111111, 0.1111111]])



resim2 = cv2.filter2D(src=resim, ddepth=-1, kernel=box_blur_ker)

cv2.imshow('Orijinal Resim', resim)
cv2.imshow('Filtrelenmis Resim', resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()