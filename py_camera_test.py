#Import modules
import picamera
import picamera.array
import time
import cv2

#Initialize camera
camera = picamera.PiCamera()
camera.resolution = (640,480)
rawCapture = picamera.array.PiRGBArray(camera)
#Let camera warm up
time.sleep(0.1)

#Capture image
camera.capture(rawCapture, format="bgr")
img = rawCapture.array

cv2.imshow("picamera test", img)
cv2.waitKey(0)

