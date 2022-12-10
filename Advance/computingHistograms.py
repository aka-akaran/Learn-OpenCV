import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt








img = cv.imread( 'Media/Photos/9.jpg' )
cv.imshow('Original', img)








# #### Gray Histogram




# gray = cv.cvtColor( img, cv.COLOR_BGR2GRAY )
# cv.imshow( 'Gray Image', gray )





# # Forming Mask
# blank = np.zeros( img.shape[:2], 'uint8' )
# circle = cv.circle( blank.copy(), (img.shape[1]//2, img.shape[0]//2), 120, 255, -1 )
# rectangle = cv.rectangle( blank.copy(), (100, 100), (400,500), 255, -1 )

# tempMask = cv.bitwise_xor(circle, rectangle)
# cv.imshow('tempMask', tempMask)

# masked_image = cv.bitwise_and( gray, gray, mask= tempMask )
# cv.imshow('masked_image', masked_image)







# # mask is used to produce the histogram for the masked portion

# gray_hist = cv.calcHist( [gray], [0], masked_image, [256], [0,256] )

# plt.figure()
# plt.title('Histogram of Gray Masked Image')
# plt.xlabel('Bins')
# plt.ylabel('No. of Bins')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()














# # Color Histogram









# Forming Mask
blank = np.zeros( img.shape[:2], 'uint8' )
circle = cv.circle( blank.copy(), (img.shape[1]//2, img.shape[0]//2), 120, 255, -1 )
rectangle = cv.rectangle( blank.copy(), (100, 100), (400,500), 255, -1 )

tempMask = cv.bitwise_xor(circle, rectangle)
cv.imshow('tempMask', tempMask)

# This masked_image has three chanels
masked_image = cv.bitwise_and( img, img, mask= tempMask )
cv.imshow('masked_image', masked_image)







plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')

### There are 3 color chanels for BGR image
### chanel Number : color = { 0:blue, 1:green, 2:red }

colorChannels = ( 'b', 'g', 'r' )
for i, color, in enumerate( colorChannels ):
    hist = cv.calcHist( [img], [i], tempMask, [256], [0,256] )
    plt.plot(hist, color = color)
    plt.xlim([0,256])

plt.show()

# We used the tempMask becaues it is binary, mask should always be binary



















cv.waitKey(0)
cv.destroyAllWindows