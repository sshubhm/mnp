#Crossing Class
import cv2
from selenium import webdriver
import numpy as np
from Road import *

def color(a):
    if np.array_equal(a, [80, 202, 132]):
        return "green"
    elif np.array_equal(a, [2, 125, 240]):
        return "orange"
    elif np.array_equal(a, [0, 0, 230]):
        return "red"
    elif np.array_equal(a, [19, 19, 158]):
        return "maroon"
    else:
        return a

class crossing:
    #init method to set name and url of crossing
    def __init__(self,name, url):
        self.name = name
        self.url = url
    #getUpdate to get the latest image from Google Maps
    def getUpdate(self):
        browser = webdriver.Firefox()
        browser.maximize_window()
        browser.set_window_size(1366, 768)
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
        rLeft.setColor(color(img[259,641]))
        rTop.setColor(color(img[346,767]))
        rRight.setColor(color(img[393,740]))
        rBottom.setColor(color(img[321,628]))
        rLeft.getColor()
        rTop.getColor()
        rRight.getColor()
        rBottom.getColor()
    def getName(self):
        print self.name
