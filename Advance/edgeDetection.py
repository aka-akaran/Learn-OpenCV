import cv2 as cv
import numpy as np


img = cv.imread( 'Media/Photos/9.jpg' )
cv.imshow( 'Original', img )

gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
cv.imshow('Gray', gray)


## Laplacian Method
lap = cv.Laplacian( gray, cv.CV_64F )  # Calculates the gradiant value from source image
lap = np.uint8( np.absolute(lap) )     # Find the absolute value because lap can have -ve values
cv.imshow('Laplacian Edge Detection - Feels like Pencil Shading', lap)


## Sobel : Calculates gradient in x and y direction
sobelx = cv.Sobel( gray, cv.CV_64F, 1, 0 )
sobely = cv.Sobel( gray, cv.CV_64F, 0, 1 )
combined_sobel = cv.bitwise_or( sobelx, sobely )

cv.imshow( 'SobelX', sobelx )
cv.imshow( 'SobelY', sobely )
cv.imshow( 'Sobel Edge Detection : Sobel_Merged', combined_sobel )


## Canny
canny = cv.Canny( gray, 150, 175 )
cv.imshow('Canny Edge Detection', canny)


## You can compare images by different methods


cv.waitKey(0)
cv.destroyAllWindows