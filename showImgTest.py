import cv2

def showImg():

    img = cv2.imread('screenie.png',0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
