# import numpy as np
# import cv2
#
# # Read image
# img = cv2.imread('start.jpg')
# # Smooth it
# img = cv2.medianBlur(img,3)
# img_copy = img.copy()
# # Convert to greyscale
# img_gray = cv2.cvtColor(img_copy,cv2.COLOR_BGR2GRAY)
# # Apply Hough transform to greyscale image
# circles = cv2.HoughCircles(img_gray,cv2.HOUGH_GRADIENT,1,20,
#                      param1=60,param2=40,minRadius=0,maxRadius=0)
# circles = np.uint16(np.around(circles))
# # Draw the circles
# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
# cv2.imshow('detected circles',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Load image
origin = "test_images/small.PNG"


def CircleDetction(origin):
    origin = cv.imread(origin)
    image = cv.cvtColor(origin, cv.COLOR_BGR2GRAY)

    # Set our filtering parameters
    # Initialize parameter setting using cv2.SimpleBlobDetector
    params = cv.SimpleBlobDetector_Params()

    # Set Area filtering parameters
    params.filterByArea = True
    params.minArea = 100

    # Set Circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = 0.9

    # Set Convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = 0.2

    # Set inertia filtering parameters
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints = detector.detect(image)

    # Draw blobs on our image as red circles
    blank = np.zeros((1, 1))
    blobs = cv.drawKeypoints(image, keypoints, blank, (0, 255, 0),
                             cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)
    text = "Number of Circular Blobs: " + str(len(keypoints))
    cv.putText(blobs, text, (20, 550),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

    return blobs
    # Show blobs
    # cv2.imshow("Filtering Circular Blobs Only", blobs)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


blobs = CircleDetction(origin)
plt.imshow(cv.cvtColor(blobs, cv.COLOR_BGR2RGB))
plt.show()
