import MyHybridImages
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

import cv2

img = cv2.imread("C:/Southampton_Studies/Computer Vision/Coursework/Coursework1/Coursework1/hybrid-images/data/bicycle.bmp")
img2 = cv2.imread("C:/Southampton_Studies/Computer Vision/Coursework/Coursework1/Coursework1/hybrid-images/data/motorcycle.bmp")

a= MyHybridImages.myHybridImages(img,1,img2,5)
cv2.imshow("Image",a)
cv2.waitKey(0)

cv2.destroyAllWindows()

# print("Hello World")