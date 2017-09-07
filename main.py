import cv2, thread, time
from selenium import webdriver
from pyvirtualdisplay import Display
import os.path
import os
import numpy as np

def fetchimg():
    browser = webdriver.Firefox()
    browser.get('https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
    browser.save_screenshot('screenie.png')
    browser.quit()


def showimg():
    while not os.access('screenie.png',os.W_OK):
        pass
    img = cv2.imread('screenie.png', 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([6,100,100])
    upper = np.array([26,255,255])
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img, img, mask= mask)
    cv2.imshow('frame',img)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


fetchimg()
showimg()
cv2.waitKey(0)
cv2.destroyAllWindows()
