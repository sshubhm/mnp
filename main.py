import numpy as np
import cv2
from selenium import webdriver
from pyvirtualdisplay import Display
from showImgTest import showImg
#creating hidden display
display = Display(visible=0, size=(1920, 1080))
display.start()
print('display created')

#opening webpage in display and saving the screenshot
browser = webdriver.Firefox()
browser.get('https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
browser.save_screenshot('screenie1.png')
browser.quit()
#loading the image

showImg()