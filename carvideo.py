import cv2


vid = cv2.VideoCapture('D:\\NEU\\OpenCV\\test_videos\\car.mp4')
car_cascade = cv2.CascadeClassifier('D:\\NEU\\OpenCV\\haarCascade\\car.xml')

while True:
    ret,frame = vid.read()
    frame = cv2.resize(frame, (480 ,360))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.imshow('video',frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()
