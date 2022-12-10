import cv2 as cv
import numpySlicing as np

# Created the blank Image
blank = np.zeros( (500, 500, 3), dtype = 'uint8' )


cv.circle( blank, (250,250), 100, (0,255,0), 5 )
cv.imshow('Drawn Circle', blank)

# Drawing Line
cv.line( blank, (0,125), (256,379), (255,255,255), 2 )
cv.imshow('Line Drawn', blank)



cv.waitKey(0)
cv.destroyAllWindows