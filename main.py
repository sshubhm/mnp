from crossing import *
from TrafficLight import *

cr1 = crossing("Maharaja",'https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
cr1.getUpdate()
img = cr1.fetch()

global rLeft
global rTop
global rBottom
global rRight

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

tLeft = TrafficLight()
tTop = TrafficLight()
tRight = TrafficLight()
tBottom = TrafficLight()

cv2.waitKey(0)
cv2.destroyAllWindows()
