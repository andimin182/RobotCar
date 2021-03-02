import numpy as np 
import cv2 as cv 


def exctract_blu_color(im):
    
    hsv_im = cv.cvtColor(im, cv.COLOR_RGB2HSV)
    lower_red = np.array([160, 160, 200])
    upper_red = np.array([180, 255, 255])
    
    mask0 = cv.inRange(hsv_im, lower_red, upper_red)
    
    lower_red = np.array([0, 200, 200])
    upper_red = np.array([20, 255, 255])
    
    mask1 = cv.inRange(hsv_im, lower_red, upper_red)
    mask = mask0+mask1
    
    res = cv.bitwise_and(im,im,mask)
    mask3 = np.repeat(mask[:,:,np.newaxis], 3, axis=2)/255
    
    masked_im = im*mask3/255.
    return mask, masked_im

stream = 0
cap = cv.VideoCapture(stream)

while True:
    _, frame = cap.read()

    # Detect the blu color
    mask, masked_im = exctract_blu_color(frame)

    # Draw a rectangle around the biggest blu object
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = lambda x: cv.contourArea(x), reverse=True)
    
    if len(contours):
            
            for c in contours:
                (x, y, w, h) = cv.boundingRect(c)

                cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                x_med = int((x+ x+ w)/2)
                y_med = int((y+ y+ h)/2)
                cv.circle(frame, (x_med,y_med), 2, (0,255,0), 2)
                break

    cv.imshow('Blu Detection', frame)
    #cv.imshow("Blu Filtering", masked_im)

    key = cv.waitKey(5) & 0xFF

    if key == 27:
        break

cap.release()
cv.destroyAllWindows()