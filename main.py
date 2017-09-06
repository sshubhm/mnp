import numpy as np
import cv2
from selenium import webdriver

from pyvirtualdisplay import Display


display = Display(visible=0, size=(1920, 1080))
display.start()

browser = webdriver.Firefox()
browser.get('https://www.google.co.in/maps/@28.7190605,77.068675,16.75z/data=!5m1!1e1')
browser.save_screenshot('screenie.png')
browser.quit()
