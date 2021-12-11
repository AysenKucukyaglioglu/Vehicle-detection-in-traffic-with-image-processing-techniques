import cv2
import numpy as np

vid = cv2.VideoCapture('D:\\NEU\\OpenCV\\test_videos\\car.mp4')
car_cascade = cv2.CascadeClassifier('D:\\NEU\\OpenCV\\car_cascade\\car_cascade.xml')

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = vid.read()
    Arka_Silinmis_Kare = fgbg.apply(frame)

    
    frame = cv2.resize(frame, (480 ,360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow('video',frame)
    cv2.imshow('Arka_Silinmis_Kare',Arka_Silinmis_Kare)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
