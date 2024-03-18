import cv2
import numpy as np
from HoughCV import HoughCV
from GeneralHough import GenHough

# load the input images
image = "test_image/one_circle.png"
img1 = GenHough(image)
img2 = HoughCV(image)


# img1 = cv2.imread('panda.jpg')
# img2 = cv2.imread('panda1.jpg')

# convert the images to grayscale
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# define the function to compute MSE between two images
def mse(img1, img2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))
    return mse, diff


# error, diff = mse(img1, img2)
# print("Image matching Error between the two images:", error)
#
# cv2.imshow("difference", diff)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
