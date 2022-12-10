import cv2 as cv
import numpy as np


img = cv.imread('Media/Photos/1.jpg')
cv.imshow( 'Original Image', img )





# Translation : Shifting along x, y axis

def translate( image, x, y ) :
    transMat = np.float32( [[1,0,x],[0,1,y]] )
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down 

translated = translate( img, 200, 50 )
cv.imshow( 'Shifted the image', translated )










# Rotation : Rotate the image, new coordinates are calculated acc to the translaion matrix

def rotate( image, angle, rotPoint = None ) :
    (height, width) = image.shape[:2]
    if( rotPoint == None ) :
        rotPoint = ( width//2, height//2 )
    
    transMat = cv.getRotationMatrix2D( rotPoint, angle, 1.0 )
    dimensions = (width, height)

    return cv.warpAffine( image, transMat, dimensions )


(height, width) = img.shape[:2]
rotPoint = ( width//4, height//4 )

rotatedImage = rotate( img, 45, rotPoint )
cv.imshow( 'Rotated image', rotatedImage )

rotRotImage = rotate( rotatedImage, 45 )
cv.imshow( 'Rotated the already rotated image', rotRotImage )

rotImage = rotate( img, 90 )
cv.imshow( 'Rotated by 90 degree', rotImage )











# Resizing
resized = cv.resize( img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv.INTER_CUBIC )
cv.imshow( 'Resized the image', resized )






# Fliping : '0' --> about x axis, '1' --> about y axis, '-1' -->about x and y both
flipped = cv.flip( img, 0 )
cv.imshow( 'Flipped Image', flipped )







# Cropping : img[rowStart:rowEnd:rowSkip , colStart, colEnd, colSkip]
(height, width) = img.shape[:2]
croped = img[0:height//2 , 0:width//2]
cv.imshow( 'Croped Image', croped )







cv.waitKey(0)
cv.destroyAllWindows