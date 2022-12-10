import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread( 'Media/Photos/1.jpg' )
cv.imshow('Original', img)

# RBG Image : inversion of BGR format
# matplotlib has default image as rgb

# plt.imshow(img)
# plt.show()



# BGR to Gray

gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
cv.imshow('Gray', gray)


# BGR to HSV

hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
cv.imshow('hsv', hsv)


# BGR to l*a*b

lab = cv.cvtColor( img, cv.COLOR_BGR2LAB )
cv.imshow('l*a*b', lab)


# BGR to RBG
rbg = cv.cvtColor( img, cv.COLOR_BGR2RGB )
cv.imshow('RBG image', rbg)
plt.imshow(rbg)
plt.show()

# NOTE : matplotlib consider that the input image is 'BGR' and i have to convert it to 'RBG' because by default matplotlib has display "RGB" color pattern


# HSV to BGR

hsv_bgr = cv.cvtColor( hsv, cv.COLOR_HSV2BGR )
cv.imshow('HSV --> BGR', hsv_bgr)


# We can't directly convert Gray to HSV 
# First we have to convert it to the BGR, then to HSV

# gray_bgr = cv.cvtColor( gray, cv.COLOR_GRAY2BGR )
# bgr_hsv = cv.cvtColor( gray_bgr, cv.COLOR_BGR2HSV )
# cv.imshow( 'GRAY --> BGR', bgr_hsv )










cv.waitKey(0)
cv.destroyAllWindows