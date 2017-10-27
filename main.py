import time

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
rLeft.createLight(270,290,290,310,board.C)
rTop.createLight(290,270,310,290,board.C)
rRight.createLight(310, 290, 330, 310,board.C)
rBottom.createLight(290, 310, 310, 330,board.C)
roads = [rLeft, rTop, rRight, rBottom]

for road in roads:
    rColor = road.getColor()
    if rColor == 'maroon':
        road.tLight.setTime(30)
    elif rColor == 'red':
        road.tLight.setTime(25)
    elif rColor == 'orange':
        road.tLight.setTime(20)
    elif rColor == 'green':
        road.tLight.setTime(15)
    print(rColor)
board.top.after(rLeft.tLight.getTime()*1000,board.glow,rLeft.tLight,roads)
board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()),board.glow,rTop.tLight,roads)
board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()+rRight.tLight.getTime()),board.glow,rRight.tLight,roads)
board.top.after(1000*(rLeft.tLight.getTime()+rTop.tLight.getTime()+rRight.tLight.getTime()+rBottom.tLight.getTime()),board.glow,rBottom.tLight,roads)


board.top.mainloop()
