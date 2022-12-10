import cv2 as cv


# Reading Videos

video = cv.VideoCapture('Media/Videos/1.mp4')

while True :
    isTrue, frame = video.read()
    cv.imshow('Reading Videos', frame)

# During waiting period, waits for any key to input
# 0xFF = 11111111 i.e. 8 bit digit with all "1's"
# https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
    if( (cv.waitKey(20) & 0xFF) == ord('s') ) :
        break



video.release()
cv.destroyAllWindows()