import cv2 as cv
import numpySlicing as np

blank = np.zeros( (300,1250,3), dtype = 'uint8' )

cv.putText( blank, "hey! it's me AKA_RAN", (0,250), cv.FONT_HERSHEY_DUPLEX, 3, (156,23,89), 2 )
cv.imshow('writing text', blank)

cv.waitKey(0)
cv.destroyAllWindows