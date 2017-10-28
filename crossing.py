#Crossing Class
import cv2
from selenium import webdriver
import numpy as np
from Road import *

class crossing:
    #init method to set name and url of crossing

    def __init__(self,name, url):
        self.name = name
        self.url = url
        self.browser = webdriver.Firefox()

    #opening firefox
    def openFirefox(self):
        self.browser.maximize_window()
        self.browser.set_window_size(1366, 768)

    #getUpdate to get the latest image from Google Maps

    def getUpdate(self):
        self.browser.get(self.url)
        self.browser.save_screenshot(self.name+".png")
    #fetch method to fetch the image
    def fetch(self):
        img = cv2.imread(self.name+".png")
        return img

    def getName(self):
        print self.name
