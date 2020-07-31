import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("opencvlogo.jpg",0)
plt.imshow(img, cmap= "gray", interpolation="bicubic" )
plt.show()