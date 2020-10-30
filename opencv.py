import cv2

#img = cv2.imread("thanu.jpg")
#cv2.imshow("Output",img)
#cv2.waitKey(0)

cap = cv2.VideoCapture("dark.mkv")
cap.set(3,1000)
cap.set(4,1000)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
      break

