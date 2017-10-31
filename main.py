from crossing import *
from CrossingGUI import *

cr1 = crossing("New_Image",'https://www.google.co.in/maps/@28.6971866,77.1446998,15z/data=!5m1!1e1')
cr1.openFirefox()
cr1.getUpdate()
img = cr1.fetch()
img1 = cr1.cropImg(img,0,768,0,430)
# cv2.imshow("1", img1)
# cv2.imshow("2", cr1.cropImg(img,0,768,430,530))
# cv2.imshow("3", cr1.cropImg(img,0,768,530,650))
# cv2.imshow("4", cr1.cropImg(img,0,768,650,790))
# cv2.imshow("5", cr1.cropImg(img,0,768,790,1366))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
board = Draw(img1, cr1.cropImg(img,0,768,430,530), cr1.cropImg(img,0,768,530,650), cr1.cropImg(img,0,768,650,790), cr1.cropImg(img,0,768,790,1366))
board.top.mainloop()

# while 1:
#     img = cr1.fetch()
#
#     rLeft = Road()
#     rTop = Road()
#     rRight = Road()
#     rBottom = Road()
#
#     #Shubham's coordinates comment them if you want to use yours, don't delete
#     # rLeft.setColor(color(img[256,634]))
#     # rTop.setColor(color(img[338,774]))
#     # rRight.setColor(color(img[408,759]))
#     # rBottom.setColor(color(img[334,617]))
#
#     # #testing colors
#     # rLeft.setColor('red')
#     # rTop.setColor('green')
#     # rRight.setColor('green')
#     # rBottom.setColor('green')
#
#
#
#     # jatin's coordinates
#     rLeft.setColor(color(img[258,587]))
#     rTop.setColor(color(img[351,743]))
#     rRight.setColor(color(img[411,710]))
#     rBottom.setColor(color(img[336,594]))
#
#
#     #rLeft.setColor(color("green"))
#     #rTop.setColor(color("green"))
#     #rRight.setColor(color("green"))
#     #rBottom.setColor(color("green"))
#
#
#     #creating the board
#     board = Draw(rLeft,rRight,rTop,rBottom)
#     rLeft.createLight(260,270,270,280,260,290,270,300,board.C)
#     rTop.createLight(320,260,330,270,300,260,310,270,board.C)
#     rRight.createLight(330, 320, 340, 330, 330,300,340,310,board.C)
#     rBottom.createLight(270,330,280,340,290, 330, 300, 340,board.C)
#
#
#     #round robin scheduling
#     roads = [rLeft, rRight, rTop, rBottom]
#
#     for road in roads:
#         rColor = road.getColor()
#         if rColor == 'maroon':
#             road.tLight.setStTime(30)
#             road.tLight.setRtTime(15)
#         elif rColor == 'red':
#             road.tLight.setStTime(25)
#             road.tLight.setRtTime(15)
#
#         elif rColor == 'orange':
#             road.tLight.setStTime(20)
#             road.tLight.setRtTime(10)
#
#         elif rColor == 'green':
#             road.tLight.setStTime(15)
#             road.tLight.setRtTime(10)
#
#     # board.top.after(rLeft.tLight.getTime()*1000,board.glow,rLeft.tLight,roads)
#     # board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()),board.glow,rTop.tLight,roads)
#     # board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()+rRight.tLight.getTime()),board.glow,rRight.tLight,roads)
#     # board.top.after(1000*(rLeft.tLight.getTime()+rTop.tLight.getTime()+rRight.tLight.getTime()+rBottom.tLight.getTime()),board.glow,rBottom.tLight,roads)
#
#     #old algorithm
#     # itr = 0
#     # for road in roads:
#     #     itr = itr + 1
#     #     if road == rLeft:
#     #         board.glow(road.tLight,roads)
#     #         oldTime = road.tLight.getStTime()
#     #         continue
#     #     print(oldTime)
#     #     # if(itr == 4):
#     #         # board.top.after((oldTime) * 1000, cr1.getUpdate)
#     #     board.top.after((oldTime)*1000, board.glow,road.tLight,roads)
#     #
#     #     oldTime = oldTime + road.tLight.getStTime()
#     #
#     # board.top.after(oldTime*1000, board.glow,roads[0].tLight,roads)
#     #
#     # board.top.after(oldTime*1000, board.quit)
#
#
#     #new algorithm
#
#     #controling the horizontal road
#     #turning on both the rLeft
#     board.turnOn(rLeft.tLight.st)
#     board.turnOn(rLeft.tLight.rt)
#     delay = 0
#
#     #finding max congestion
#     #if right congestion is greater
#     if (rLeft.tLight.getStTime() < rRight.tLight.getStTime()):
#         delay = rLeft.tLight.getRtTime()
#
#         #turning off rLeft.rt
#         board.top.after(delay * 1000,board.turnOff,rLeft.tLight.rt)
#
#         #turning on rRight.st
#         board.top.after(delay * 1000, board.turnOn, rRight.tLight.st)
#         delay = rLeft.tLight.getStTime()
#
#         #turning off rLeft.st
#         board.top.after(delay * 1000, board.turnOff, rLeft.tLight.st)
#         #turning on rRight.rt
#         board.top.after(delay * 1000, board.turnOn, rRight.tLight.rt)
#
#         #turning off both right lights
#         delay = rRight.tLight.getStTime()
#         board.top.after(delay * 1000, board.turnOff, rRight.tLight.st)
#         board.top.after(delay * 1000, board.turnOff, rRight.tLight.rt)
#
#     else:
#         timeMax = rLeft.tLight.getStTime() - (rRight.tLight.getStTime() - rRight.tLight.getRtTime())
#         delay = timeMax
#
#         #turning off rLeft.rt
#         board.top.after(delay * 1000, board.turnOff, rLeft.tLight.rt)
#         #turning on rRight.st
#         board.top.after(delay * 1000, board.turnOn, rRight.tLight.st)
#
#         #turning off rLeft.st
#         delay = rLeft.tLight.getStTime()
#         board.top.after(delay * 1000, board.turnOff, rLeft.tLight.st)
#         #turning on rRight.rt
#         board.top.after(delay * 1000, board.turnOn, rRight.tLight.rt)
#
#         #turning off both right lights
#         delay = rRight.tLight.getStTime() +timeMax
#         board.top.after(delay * 1000, board.turnOff, rRight.tLight.st)
#         board.top.after(delay * 1000, board.turnOff, rRight.tLight.rt)
#
#     #controling the vertical road
#     #turning on both the rTop
#     time = delay
#     board.top.after(time * 1000,board.turnOn,rTop.tLight.st)
#     board.top.after(time * 1000,board.turnOn,rTop.tLight.rt)
#
#     #finding max congestion
#
#     #if Bottom congestion is greater
#     if (rTop.tLight.getStTime() < rBottom.tLight.getStTime()):
#         delay = rTop.tLight.getRtTime() + time
#
#         #turning off rTop.rt
#         board.top.after(delay * 1000,board.turnOff,rTop.tLight.rt)
#
#         #turning on rBottom.st
#         board.top.after(delay * 1000, board.turnOn, rBottom.tLight.st)
#         delay = rTop.tLight.getStTime() + time
#
#         #turning off rTop.st
#         board.top.after(delay * 1000, board.turnOff, rTop.tLight.st)
#         #turning on rBottom.rt
#         board.top.after(delay * 1000, board.turnOn, rBottom.tLight.rt)
#
#         #turning off both Bottom lights
#         delay = rBottom.tLight.getStTime() + time
#         board.top.after(delay * 1000, board.turnOff, rBottom.tLight.st)
#         board.top.after(delay * 1000, board.turnOff, rBottom.tLight.rt)
#
#     else:
#         timeMax = rTop.tLight.getStTime() - (rBottom.tLight.getStTime() - rBottom.tLight.getRtTime())
#         delay = timeMax + time
#
#         #turning off rTop.rt
#         board.top.after(delay * 1000, board.turnOff, rTop.tLight.rt)
#         #turning on rBottom.st
#         board.top.after(delay * 1000, board.turnOn, rBottom.tLight.st)
#
#
#
#         #turning off rTop.st
#         delay = rTop.tLight.getStTime() + time
#         board.top.after(delay * 1000, board.turnOff, rTop.tLight.st)
#         #turning on rBottom.rt
#         board.top.after(delay * 1000, board.turnOn, rBottom.tLight.rt)
#         # fetching the update map
#         board.top.after(delay * 1000, cr1.getUpdate)
#         #turning off both Bottom lights
#         delay = rBottom.tLight.getStTime() +timeMax + time
#         board.top.after(delay * 1000, board.turnOff, rBottom.tLight.st)
#         board.top.after(delay * 1000, board.turnOff, rBottom.tLight.rt)
#     board.top.after(delay * 1000, board.quit)
#     board.top.mainloop()
#
