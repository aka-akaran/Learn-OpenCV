import cv2 as cv

def rescaleFrame( frame, scale = 0.75 ) :
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos
video = cv.VideoCapture('Media/Videos/1.mp4')

while True :
    isTrue, frame = video.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Original', frame)
    cv.imshow('Resized By Scale = 0.75', frame_resized)

    if( (cv.waitKey(20) & 0xFF) == ord('s') ) :
        break

video.release()
cv.destroyAllWindows