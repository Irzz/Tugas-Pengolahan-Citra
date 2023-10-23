import cv2

img = cv2.imread("D:\Codingan\Python\Tugas Pengolahan Citra\R.jpg")
img = cv2.resize(img, (350, 250))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 70, 255, 0)

cv2.imshow("Original", img)
cv2.imshow("Binary", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()