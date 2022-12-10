import cv2 as cv
import numpy as np

# Thresholding : Used to convert image to binary
# Types : (1) Simple    (2) Adaptive


img = cv.imread( 'Media/Photos/4.jpg' )
cv.imshow('Original', img)

gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
cv.imshow( 'Gray Image', gray )




# Simple Thresholding
thresholdValue, threshImg = cv.threshold( gray, 150, 255, cv.THRESH_BINARY )
cv.imshow( 'Thresh Image', threshImg )


thresholdValue, threshInvImg = cv.threshold( gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow( 'Inverse Thresh Image', threshInvImg )







# # Adaptive Thresholding : Overcome the disadvantage of passing threshold value manually
adaptiveThresh = cv.adaptiveThreshold( gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3 )
cv.imshow('Adaptive Threshold Image', adaptiveThresh)



adaptiveInvThresh = cv.adaptiveThreshold( gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 9, 3 )
cv.imshow('Adaptive Inverse Threshold Image', adaptiveInvThresh)















cv.waitKey(0)
cv.destroyAllWindows