import cv2 as cv
import numpySlicing as np

# Create a blank image using numpy
# uint is the data type of an image
# (500, 300, 3) = (height, width, color channels)
blank = np.zeros( (500, 500, 3), dtype = 'uint8' )
cv.imshow('Blank Image filled with zeros', blank)


# Filling the image with the certain color

# White
blank[:] = 255, 255, 255
cv.imshow('Painted with Red', blank)

# Green
blank[:] = 0, 255, 0
cv.imshow('Painted with Green', blank)

# Blue
blank[:] = 255, 0, 0,
cv.imshow('Painted with Blue', blank)



# Paint the certain portion
blank = np.zeros( (400, 400, 3), dtype = 'uint8' )
blank[0:200, 0:200] = 0, 0, 255
cv.imshow('Painting the certain portion', blank)


cv.waitKey(0)
cv.destroyAllWindows