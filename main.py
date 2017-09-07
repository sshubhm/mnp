import cv2, thread, time
from selenium import webdriver
from pyvirtualdisplay import Display
import os.path
import os

def fetchimg():
    browser = webdriver.Firefox()
    browser.get('https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
    browser.save_screenshot('screenie.png')
    browser.quit()
    thread.start_new_thread(showimg, ())


def showimg():
    while not os.access('screenie.png',os.W_OK):
        pass
    img = cv2.imread('screenie.png', 1)
    cv2.imshow('image', img)




thread.start_new_thread(fetchimg, ())

while 1:
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass
