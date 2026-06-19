from pysimverse import Drone
from cvzone.ColorModule import ColorFinder
import cv2
import cvzone
import time 


# --------------------------------
# DRONE
# --------------------------------

drone = Drone()

drone.connect()
drone.streamon()
drone.take_off(takeoff_height=25)


# Color detection setup
#

myColorFinder = ColorFinder(trackBar=False)
hsvVals ={"hmin":0 , "smin":113, "vmin":73, "hmax":10,"smax":229,"vmax":255}

deadband_px =2

yaw_power= 0.4


while True:
    frame,ok = drone.get_frame()

    if not ok:
        continue

    # dtect line 

    imgLine,mask = myColorFinder.update(frame,hsvVals)

    imgContours, conFound = cvzone.findContours(frame, mask)


    yaw =0

    if conFound:
        center_x = frame.shape[1] // 2
        cx = conFound[0]['center'][0]

        error = center_x - cx


        if abs(error)<deadband_px:

            yaw =0
        elif error <0:
            yaw=+ yaw_power

        else:
            yaw =- yaw_power


    drone.send_rc_control(0,20,0,yaw)


    #Display

    imgStack = cvzone.stackImages([frame,imgLine,mask,imgContours],2,0.6)

    cv2.imshow("Images Stack",imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

