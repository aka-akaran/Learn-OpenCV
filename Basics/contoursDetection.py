# Mathematically Contours and edges are different
# Contours are boundary of the objects



from configparser import Interpolation
import cv2 as cv
import numpy as np


# img = cv.imread('Media/Photos/6.jpg')
# cv.imshow( 'Original', img )



img = cv.imread("Media/Photos/6.jpg")
gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
ret, thresh = cv.threshold( gray, 90, 230, cv.THRESH_BINARY )
def resizeFrame(img, scale = 0.75) :
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)
img = resizeFrame(thresh, scale=0.2)


# findContours returns contours and hierarchy from the structuring element
# contours only consider binary images for processing
# mode : returns contours belonging to that group. Group can be tree(return contours which are hierarchial), list(returns all) and so on
# method : used to reduce the contours based on the method



# scale = 0.01
# widthImg = int(img.shape[1]*scale)
# heightImg = int(img.shape[0]*scale)


# blur = cv.GaussianBlur( gray, (3,3), cv.BORDER_DEFAULT )
# canny = cv.Canny( gray, 125, 175 )

# contours, hierarchy = cv.findContours( canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE )
# print( f'{len(contours)} contour(s) found!' )







# We can find contours by threshoding the image also instead of canny
# But it's better to use the canny first

# Thresholding is used to binarizing the image

# if the pixel value is less than 120 then change it to 0
# if the pixel value is more than 120 then change it to 255 i.e. white


# img = cv.resize( img, (500, 500), fx=0.5, fy=0.25, interpolation=cv.INTER_AREA )
cv.imshow( 'Threshold Image', img )

# contours, hierarchy = cv.findContours( thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE )
# print( f'{len(contours)} contours(s) found!' )















# We can visualize the contours by drawing them on the blank image

# structuring element to find contours(canny/threshold/some other) must be similar to the contours on the blank Image

# cv.imshow('frame', resized)
# blank = np.zeros( img.shape, 'uint8' )
# cv.imshow('Blank Image', blank)

# contours, hierarchy = cv.findContours( canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE )
# cv.drawContours( blank, contours, -1, (255,255,255), 1 )
# cv.imshow( 'Canny Image', canny )
# cv.imshow( 'Contours on blank Image', blank )






cv.waitKey(0)
cv.destroyAllWindows