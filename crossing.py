#Crossing Class
import cv2, thread, time
from selenium import webdriver
import os.path
import os
import numpy as np

from Road import *


class crossing:

    #init method to set name and url of crossing
    def __init__(self,name, url):
        self.name = name
        self.url = url

    #getUpdate to get the latest image from Google Maps
    def getUpdate(self):
        browser = webdriver.Firefox()
        browser.get(self.url)
        browser.save_screenshot(self.name+".png")
        browser.quit()

    #fetch method to fetch the image
    def fetch(self):
        img = cv2.imread(self.name+".png")
        rLeft = Road()
        rTop = Road()
        rRight = Road()
        rBottom = Road()

        rLeft.setColor(str(img[268,654]))
        rTop.setColor(str(img[346,767]))
        rRight.setColor(str(img[393,740]))
        rBottom.setColor(str(img[321,628]))

	#to rotate the image by 40 degrees counterclockwise
	#rows,cols,channels = img.shape
	#M = cv2.getRotationMatrix2D((cols/2,rows/2),40,1)
	#dst = cv2.warpAffine(img,M,(cols,rows))
	
	#to print the color value in given pixel region
	#road1 = img[350:650, 620:630]	
	#print road1

        
    def getName(self):
        print self.name
