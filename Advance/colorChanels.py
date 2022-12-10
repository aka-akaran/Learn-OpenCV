import cv2 as cv
import numpy as np

img = cv.imread( 'Media/Photos/1.jpg' )


# split image into number of channels
b,g,r = cv.split(img)
cv.imshow('Original', img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# Merge Images
merged = cv.merge([b,g,r])
cv.imshow( 'Merged', merged )



# Merging With Blank Image

blank = np.zeros( img.shape[:2], 'uint8' )

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue merged with blank', blue)
cv.imshow('green merged with blank', green)
cv.imshow('red merged with blank', red)










cv.waitKey(0)
cv.destroyAllWindows