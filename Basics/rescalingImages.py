from pickle import NONE
from tkinter import Frame
from turtle import width
import cv2 as cv


def resizeFrame(img, scale = 0.75) :
    width = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

# Interpolation is the way the extra pixels in the new image is calculated.
# If the original image is smaller, then a larger rescaled
# image has extra pixels which is not exactly the same as a nearby pixels.
# https://iq.opengenus.org/different-interpolation-methods-in-opencv/


img = cv.imread( 'Media/Photos/3.jpg' )

cv.imshow('Original Image', img)
resizedImage = resizeFrame(img)
cv.imshow('Resized Image', resizedImage)
cv.waitKey(0)

cv.destroyAllWindows
