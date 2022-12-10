import cv2 as cv
import numpy as np


# img = cv.imread( 'Media/Photos/7.jpg' )
# cv.imshow('Original', img)

blank = np.zeros( (400,400), 'uint8' )

rectangle = cv.rectangle( blank.copy(), (100,100), (300,300), 255, -1 )
circle = cv.circle( blank.copy(), (200, 200), 110, 255, -1 )

cv.imshow('Rectangle', rectangle)
cv.imshow( 'Circle', circle )

# Bitwise AND
bitwise_and = cv.bitwise_and( rectangle, circle )
cv.imshow( 'Bitwise AND of Rectangle and circle', bitwise_and )


# Bitwise OR
bitwise_or = cv.bitwise_or( rectangle, circle )
cv.imshow( 'Bitwise OR of Rectangle and circle', bitwise_or )


# Bitwise XOR
bitwise_xor = cv.bitwise_xor( rectangle, circle )
cv.imshow( 'Bitwise XOR of Rectangle and circle', bitwise_xor )


# Bitwise NOT : Revert the pixels value
bitwise_not = cv.bitwise_not( rectangle )
cv.imshow( 'Bitwise NOT of Rectangle and circle', bitwise_not )






cv.waitKey(0)
cv.destroyAllWindows