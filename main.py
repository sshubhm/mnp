import cv2, thread, time
from selenium import webdriver
from pyvirtualdisplay import Display
import os.path
import os

clear = lambda: os.system('clear')

def fetchimg():
    browser = webdriver.Firefox()
    browser.get('https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
    browser.save_screenshot('screenie.png')
    browser.quit()


def showimg():
    while not os.access('screenie.png',os.W_OK):
        print "fetching image"
        time.sleep(0.5)
        clear()
        print "fetching image."
        time.sleep(0.5)
        clear()
        print "fetching image.."
        time.sleep(0.5)
        clear()
        print "fetching image..."
        time.sleep(0.5)
        clear()
    if os.access('screenie.png', os.W_OK):
        img = cv2.imread('screenie.png', 1)
        cv2.imshow('image', img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()


thread.start_new_thread(fetchimg, ())
thread.start_new_thread(showimg,())
while 1:
    pass