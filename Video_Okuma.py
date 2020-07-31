import cv2
import numpy as np

yakala = cv2.VideoCapture(0)


while (True):
    deger, kare = yakala.read()
    cv2.imshow("Ben", kare)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break


yakala.release()
cv2.destroyAllWindows()