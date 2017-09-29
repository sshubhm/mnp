import cv2, thread, time
from selenium import webdriver
import os.path
import os
import numpy as np

class crossing:
    def __init__(self,name, url):
        self.name = name
        self.url = url

    def getUpdate(self):
        browser = webdriver.Firefox()
        browser.get(self.url)
        browser.save_screenshot(self.name+".png")
        browser.quit()

    def fetch(self):
        img = cv2.imread(self.name+".png")
	
	#to rotate the image by 40 degrees counterclockwise
	rows,cols,channels = img.shape
	M = cv2.getRotationMatrix2D((cols/2,rows/2),40,1)
	dst = cv2.warpAffine(img,M,(cols,rows))
	
	#to print the color value in given pixel region
	road1 = img[350:650, 620:630]	
	print road1

        hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
        lower = np.array([6, 100, 100])
        upper = np.array([26, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(dst, dst, mask=mask)

        #cv2.imshow('frame', img)
	cv2.imshow('rotated', dst)
        #cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    def getName(self):
        print self.name
