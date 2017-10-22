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
        return img

    def getName(self):
        print self.name
