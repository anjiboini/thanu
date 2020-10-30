import cv2
import numpy as np

#img = cv2.imread("thanu.jpg")
#print(img.shape)
#imgResize = cv2.resize(img,(500,400))
#cv2.imshow("Image",imgResize)
##imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
##imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
##imgCanny = cv2.Canny(imgResize,100,100)
##cv2.imshow("Gray Image",imgGray)
##cv2.imshow("Blur Image",imgBlur)
##cv2.imshow("canny Image",imgCanny)
##cv2.waitKey(0)##


#img = cv2.imread("thanu.jpg")
##pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
#pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
#matrix = cv2.getPerspectiveTransform(pts1,pts2)
#imgOutput = cv2.warpPerspective(img,matrix,(width,height))

#cv2.imshow("Image",img)
#cv2.imshow("Output",imgOutput)
#cv2.waitKey(0)

img = cv2.imread("thanu.jpg")
imgResize = cv2.resize(img,(500,400))
imgHor = np.hstack((imgResize,imgResize))
imgVer = np.vstack((imgResize,imgResize))

cv2.imshow("HoriZontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)

