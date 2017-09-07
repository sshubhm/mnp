import numpy as np
import cv2

color = np.uint8([[[9,129,240]]])
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
print hsv