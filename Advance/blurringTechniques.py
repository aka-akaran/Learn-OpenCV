import cv2 as cv



img = cv.imread( 'Media/Photos/7.jpg' )
cv.imshow('Original', img)

# Blur : Smooths the images/ reduce the noise

# Average Blurring : centre pixel value = average of all surrounding pixels in the kernel

avg_blur = cv.blur( img, (3,3) )
cv.imshow('Average Blur', avg_blur)


# Guassian Blur : More Natural compared to average, get less blur image
# sigmax = standard deviation in x direction

guass_blur = cv.GaussianBlur( img, (3,3), 0 )
cv.imshow('Guassian Blur', guass_blur)


# Median Blur : Central pixel value is median of the surrounding pixels in the kernel
#               More Effective in reducing noise
#               Single integer value for the kernel, automatically detected
#               Not meant for high kernel sizes

median_blur = cv.medianBlur( img, 3, 0 )
cv.imshow('Median Blur', median_blur)


# Bilateral Blur : Most Effective, takes care of edges while blurring
# d : diameter not kernel 
# sigmaColor : if it's more in the radius then retain the central pixel value of that color
# sigmaSpace : If it's more in the radius then used for blurring, for larger values result same as median blur

bilateral_blur = cv.bilateralFilter(img, 5, 15, 15 )
cv.imshow( 'Bilateral Blur', bilateral_blur )



cv.waitKey(0)
cv.destroyAllWindows