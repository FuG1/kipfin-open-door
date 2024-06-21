import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype="uint8")
# photo[:] = 255, 0, 0
cv2.circle(photo, (175, 150), 50 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (270, 150), 50 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (190, 175), 50 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (250, 175), 50 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (205, 220), 25 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (235, 220), 25 , (0,0,255), thickness=cv2.FILLED)
cv2.circle(photo, (225, 230), 25 , (0,0,255), thickness=cv2.FILLED)
cv2.putText(photo, "Mashiky", (155,280), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
cv2.imshow('Photo', photo)
cv2.waitKey(0)
