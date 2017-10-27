from crossing import *
from TrafficLight import *
from CrossingGUI import *

cr1 = crossing("Maharaja",'https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
#cr1.getUpdate()
img = cr1.fetch()



rLeft = Road()
rTop = Road()
rRight = Road()
rBottom = Road()


#my coordinates comment them if you want to use yours, don't delete
rLeft.setColor(color(img[256,634]))
rTop.setColor(color(img[338,774]))
rRight.setColor(color(img[408,759]))
rBottom.setColor(color(img[334,617]))

# rLeft.setColor("green")
# rTop.setColor("red")
# rRight.setColor("maroon")
# rBottom.setColor("orange")



#creating the board
board = Draw(rLeft,rRight,rTop,rBottom)


cv2.waitKey(0)
cv2.destroyAllWindows()
