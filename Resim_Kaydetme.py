import cv2
import numpy as np

resim = cv2.imread("../4.1 Matplotlib/opencvlogo.jpg", 0)
cv2.imshow("Yazgit",resim)
a = cv2.waitKey(0)
if a == 27:
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("opencv_s_tusu.png", resim)