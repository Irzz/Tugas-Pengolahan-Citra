import cv2
import numpy as np

img = cv2.imread("D:\Codingan\Python\Tugas Pengolahan Citra\R.jpg")
img = cv2.resize(img, (350, 250))

red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

cv2.imshow("Red", red)
cv2.imshow("Green", green)
cv2.imshow("Blue", blue)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
