import cv2 as cv
import numpy as np

drawing = False
mode = True
ix, iy = -1,-1

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x,y), (0,255,0), -1)
            else:
                cv.circle(img,(x,y), 5, (0,0,255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, (ix,iy), (x,y),(0,255,0), -1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('colmeia')
cv.setMouseCallback('colmeia', draw_circle)

while True:
    cv.imshow('colmeia', img)
    k = cv.waitKey(1)
    
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()