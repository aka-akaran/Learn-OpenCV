import cv2 as cv

img = cv.imread('Media/Photos/1.jpg')
cv.imshow('img', img)

# # Grayscale : Shows the intensity distriution rather than color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('RBG to Gray Conversion', gray)

# Blur
blur = cv.GaussianBlur( img, (7,7), cv.BORDER_DEFAULT )
cv.imshow( 'Blurred Image', blur )

# Edge Cascading using Canny Method. There are several methods including Canny
canny = cv.Canny( img, 125,175 )
cv.imshow('Edge Cascading By Canny', canny)

# Dilation using cascade image
dilated = cv.dilate( canny, (3,3), iterations=1 )
cv.imshow('Dilated using Canny Edge', dilated )

# Erosion on dilated image to get the structuring element
eroded = cv.erode( dilated, (3,3), iterations= 1 )
cv.imshow('Erosion of the dilated image to get the structuring Element', eroded)

# Resizing
resized = cv.resize( img, (1080,720), interpolation= cv.INTER_CUBIC )
cv.imshow( 'Resizing to the higher dimension using suitable intrpoltation', resized )

# Cropping / Slicing
cropped = img[200:300, 250:400]
cv.imshow( 'Cropped', cropped )








cv.waitKey(0)
cv.destroyAllWindows