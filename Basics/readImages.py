import cv2 as cv

# Reading Images

img = cv.imread('Media/Photos/3.jpg')
cv.imshow('Tom and Jerry', img)
# cv.waitKey(x) :wait for the infinite time for keypress when x<=0 
# waits milliseconds to check if the key is pressed,
#  if pressed in that interval return its ascii value, otherwise it still -1
charr = cv.waitKey(-2)
print(chr(charr))


cv.destroyAllWindows()