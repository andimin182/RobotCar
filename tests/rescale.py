import cv2



cap = cv2.VideoCapture(0)



def rescale_frame(frame, percent=75):

    width = int(frame.shape[1] * percent/ 100)

    height = int(frame.shape[0] * percent/ 100)

    dim = (width, height)

    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

def increase_brightness(img, value=30):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)



    lim = 255 - value

    v[v > lim] = 255

    v[v <= lim] += value



    final_hsv = cv2.merge((h, s, v))

    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    return img

while True:

    rect, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  #  frame75 = rescale_frame(frame, percent=75)

 #   cv2.imshow('frame75', frame75)

    frame_rgb_20 = rescale_frame(frame_rgb, percent=20)
    frame_light = increase_brightness(frame_rgb_20, 20)

    cv2.imshow('frame20', frame_light)
    key = cv2.waitKey(1)
    if key ==27:
       break
   

cap.release()

cv2.destroyAllWindows()
