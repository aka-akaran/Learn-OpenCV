import cv2 as cv
import numpySlicing as np

# Created the blank Image
blankImg1 = np.zeros( (500, 500, 3), dtype = 'uint8' )
blankImg2 = np.zeros( (500, 500, 3), dtype = 'uint8' )
blankImg3 = np.zeros( (500, 500, 3), dtype = 'uint8' )




# Draw rectangle on image

# Giving Pixel Values
cv.rectangle(blankImg1, (125,125), (375,375), (200,200,200), 10 )
cv.imshow('Drawn Rectangle by Specific Pixel Values', blankImg1)


# Pixels according to the images
cv.rectangle( blankImg2, (blankImg2.shape[1]//4, blankImg2.shape[0]//4), (int(blankImg2.shape[1]*0.75), int(blankImg2.shape[0]*0.75) ), (200,200,200), 10 )
cv.imshow('Pixels Calculated by claculations', blankImg2)






# # Color Filling

# Pixel Range and color value
blankImg1[200:375 , 125:300] = 0,255,0 #filling with green color
cv.imshow('Coloring By giving Pixels', blankImg1)


# Thickness = rectange size
cv.rectangle( blankImg2, (125,125), (375,375), (200,200,200), cv.FILLED )
cv.imshow('Color Filling with thickness', blankImg2)


# Thickness == -1
cv.rectangle( blankImg3, (125,125), (375,375), (200,200,200), -1 )
cv.imshow('Color Negative Thickness Value', blankImg3)






cv.waitKey(0)
cv.destroyAllWindows