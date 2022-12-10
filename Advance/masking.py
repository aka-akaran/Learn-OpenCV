import cv2 as cv
import numpy as np

# Mask Image Dimensions have to be same as Source image


img = cv.imread( 'Media/Photos/9.jpg' )
cv.imshow('Original', img)

blank = np.zeros( img.shape[:2], 'uint8' )

circle = cv.circle( blank.copy(), (img.shape[1]//2, img.shape[0]//2), 120, 255, -1 )
rectangle = cv.rectangle( blank.copy(), (100, 100), (400,500), 255, -1 )

mask = cv.bitwise_xor(rectangle, circle)
cv.imshow( 'mask', mask )

masked_image = cv.bitwise_and( img, img, mask=mask )
cv.imshow('Masked Image', masked_image)


cv.waitKey(0)
cv.destroyAllWindows