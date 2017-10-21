import cv2, thread, time	
from selenium import webdriver
import os.path
import os
import numpy as np
from crossing import *


cr1 = crossing("Maharaja",'https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
#cr1.getUpdate()
cr1.fetch()



cv2.waitKey(0)
cv2.destroyAllWindows()
