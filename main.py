from map import *
from CrossingGUI import *
from crossing import *
import thread
import time
import Image

#cr1 = map("New_Image",'https://www.google.co.in/maps/@28.6971866,77.1446998,15z/data=!5m1!1e1')
#cr1.openFirefox()
#cr1.getUpdate()
# pil_im = Image.fromarray(img1)
# cv2.imshow("1", img1)
# cv2.imshow("2", cr1.cropImg(img,0,768,430,530))
# cv2.imshow("3", cr1.cropImg(img,0,768,530,650))
# cv2.imshow("4", cr1.cropImg(img,0,768,650,790))
# cv2.imshow("5", cr1.cropImg(img,0,768,790,1366))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#board = Draw(pil_im, cr1.cropImg(img,0,768,430,530), cr1.cropImg(img,0,768,530,650), cr1.cropImg(img,0,768,650,790), cr1.cropImg(img,0,768,790,1366))


#creating crossings
c1 = crossing('c1', 'https://www.google.co.in/maps/@28.7037435,77.1313585,19z/data=!5m1!1e1')
c2 = crossing('c2', 'https://www.google.co.in/maps/@28.7006228,77.1358411,21z/data=!5m1!1e1')
c3 = crossing('c3', 'https://www.google.co.in/maps/@28.6988657,77.1383807,18.5z/data=!5m1!1e1')
c4 = crossing('c4', 'https://www.google.co.in/maps/@28.6953937,77.1465191,19.5z/data=!5m1!1e1')
c5 = crossing('c5', 'https://www.google.co.in/maps/@28.6942465,77.1500341,18.5z/data=!5m1!1e1')

y=150

board = Draw(c1,c2,c3,c4,c5)
c1.createRoad(145, 143+y, 255, 258+y, 255, 143+y, 145, 258+y, board.C)
c2.createRoad(345, 143+y, 455, 258+y, 0, 0, 345, 258+y, board.C)
c3.createRoad(545, 143+y, 655, 258+y, 655, 143+y, 545, 258+y, board.C)
c4.createRoad(745, 143+y, 855, 258+y, 0, 0, 745, 258+y, board.C)
c5.createRoad(945, 143+y, 1055, 258+y, 1055, 143+y, 0, 0, board.C)

#1st crossing
c1.rLeft.createLight(150, 170+y, 160, 180+y, 150, 190+y, 160, 200+y, board.C)
c1.rTop.createLight(220, 150+y, 230, 160+y, 200, 150+y, 210, 160+y, board.C)
c1.rRight.createLight(240, 220+y, 250, 230+y, 240, 200+y, 250, 210+y, board.C)
c1.rBottom.createLight(170, 240+y, 180, 250+y, 190, 240+y, 200, 250+y, board.C)

#2nd T point
c2.rLeft.createLight(350, 170+y, 360, 180+y, 350, 190+y, 360, 200+y, board.C)
c2.rTop.createLight(0, 0, 0, 0, 0, 0, 0, 0, board.C)
c2.rRight.createLight(440, 220+y, 450, 230+y, 440, 200+y, 450, 210+y, board.C)
c2.rBottom.createLight(0, 0, 0, 0, 390, 240+y, 400, 250+y, board.C)

#3rd Crossing
c3.rLeft.createLight(550, 170+y, 560, 180+y, 550, 190+y, 560, 200+y, board.C)
c3.rTop.createLight(620, 150+y, 630, 160+y, 600, 150+y, 610, 160+y, board.C)
c3.rRight.createLight(640, 220+y, 650, 230+y, 640, 200+y, 650, 210+y, board.C)
c3.rBottom.createLight(570, 240+y, 580, 250+y, 590, 240+y, 600, 250+y, board.C)

#4th T Point
c4.rLeft.createLight(750, 170+y, 760, 180+y, 750, 190+y, 760, 200+y, board.C)
c4.rTop.createLight(0, 0, 0, 0, 0, 0, 0, 0, board.C)
c4.rRight.createLight(840, 220+y, 850, 230+y, 840, 200+y, 850, 210+y, board.C)
c4.rBottom.createLight(0, 0, 0, 0, 790, 240+y, 800, 250+y, board.C)

#5th T Point
c5.rLeft.createLight(950, 170+y, 960, 180+y, 950, 190+y, 960, 200+y, board.C)
c5.rTop.createLight(0, 0, 0, 0, 1000, 150+y, 1010, 160+y, board.C)
c5.rRight.createLight(1040, 220+y, 1050, 230+y, 1040, 200+y, 1050, 210+y, board.C)
c5.rBottom.createLight(0, 0, 0, 0, 0, 0, 0, 0, board.C)


def controlLight(crossing, xL, yL, xT, yT, xR, yR, xB, yB):
    while 1:
        crossing.rLeft.setColor(color(crossing.img[xL,yL]))
        crossing.rTop.setColor(color(crossing.img[xT,yT]))
        crossing.rRight.setColor(color(crossing.img[xR,yR]))
        crossing.rBottom.setColor(color(crossing.img[xB,yB]))


        roads = [crossing.rLeft, crossing.rRight, crossing.rTop, crossing.rBottom]

        for road in roads:
            rColor = road.getColor()
            if rColor == 'maroon':
                road.tLight.setStTime(30)
                road.tLight.setRtTime(15)
            elif rColor == 'red':
                road.tLight.setStTime(25)
                road.tLight.setRtTime(15)
            elif rColor == 'orange':
                road.tLight.setStTime(20)
                road.tLight.setRtTime(10)
            elif rColor == 'green':
                road.tLight.setStTime(15)
                road.tLight.setRtTime(10)
            elif rColor == 'white':
                print('white color')
                road.tLight.setStTime(0)
                road.tLight.setRtTime(0)
        #turning on both rLeft lights
        print('itr')
        board.turnOn(crossing.rLeft.tLight.st)
        board.turnOn(crossing.rLeft.tLight.rt)
        #starting the timer
        thread.start_new_thread(crossing.rLeft.startTimer,(board.C, crossing.rLeft.tLight.getStTime()))


        #controlling the horizontal lights
        #checking for max congestion
        if crossing.rLeft.tLight.getStTime() > crossing.rRight.tLight.getStTime():
            print ('if')
            # finding time for rLeft rt
            timeRt = crossing.rLeft.tLight.getStTime() - (crossing.rRight.tLight.getStTime() - crossing.rRight.tLight.getRtTime())
            time.sleep(timeRt)
            #turning off rt
            board.turnOff(crossing.rLeft.tLight.rt)
            #turning on rRight st
            board.turnOn(crossing.rRight.tLight.st)

            #starting right timer
            thread.start_new_thread(crossing.rRight.startTimer,(board.C, crossing.rRight.tLight.getStTime()))

            #finding time to turn off rLeft st
            timest = crossing.rLeft.tLight.getStTime() - timeRt
            time.sleep(timest)

            #turning off rLeft st
            board.turnOff(crossing.rLeft.tLight.st)
            #turning on rRight rt
            board.turnOn(crossing.rRight.tLight.rt)
            #finding time to turn off rRight lights
            timest = crossing.rRight.tLight.getStTime() - timest
            time.sleep(timest)
            board.turnOff(crossing.rRight.tLight.st)
            board.turnOff(crossing.rRight.tLight.rt)

        else:
            # finding time for rLeft rt
            timeRt = crossing.rLeft.tLight.getRtTime()
            time.sleep(timeRt)
            # turning off rt
            board.turnOff(crossing.rLeft.tLight.rt)
            # turning on rRight st
            board.turnOn(crossing.rRight.tLight.st)
            #starting timer
            thread.start_new_thread(crossing.rRight.startTimer,(board.C, crossing.rRight.tLight.getStTime()))
            # finding time to turn off rLeft st
            timest = crossing.rLeft.tLight.getStTime() - timeRt
            time.sleep(timest)
            # turning off rLeft st
            board.turnOff(crossing.rLeft.tLight.st)
            # turning on rRight rt
            board.turnOn(crossing.rRight.tLight.rt)

            #finding time to turn off both rRight
            timeRt = crossing.rRight.tLight.getStTime() - timest
            time.sleep(timeRt)
            board.turnOff(crossing.rRight.tLight.st)
            board.turnOff(crossing.rRight.tLight.rt)

        # controlling the vertical lights

        board.turnOn(crossing.rTop.tLight.st)
        board.turnOn(crossing.rTop.tLight.rt)
        #setting timer
        thread.start_new_thread(crossing.rTop.startTimer,(board.C, crossing.rTop.tLight.getStTime()))
        # checking for max congestion
        if(crossing.rTop.tLight.getStTime() == 0):
            board.turnOn(crossing.rBottom.tLight.rt)
        if crossing.rTop.tLight.getStTime() > crossing.rBottom.tLight.getStTime():
            print ('if')
            # finding time for rLeft rt
            timeRt = crossing.rTop.tLight.getStTime() - (crossing.rBottom.tLight.getStTime() - crossing.rBottom.tLight.getRtTime())
            time.sleep(timeRt)
            # turning off rt
            board.turnOff(crossing.rTop.tLight.rt)
            # turning on rRight st
            board.turnOn(crossing.rBottom.tLight.st)
            #starting timer
            thread.start_new_thread(crossing.rBottom.startTimer,(board.C,crossing.rBottom.tLight.getStTime()))
            #getting update
            crossing.mapc.getUpdate()
            crossing.img = crossing.mapc.fetch()
            # finding time to turn off rLeft st
            timest = crossing.rTop.tLight.getStTime() - timeRt
            time.sleep(timest)
            # turning off rLeft st
            board.turnOff(crossing.rTop.tLight.st)
            # turning on rRight rt
            board.turnOn(crossing.rBottom.tLight.rt)
            # finding time to turn off rRight lights
            timest = crossing.rBottom.tLight.getStTime() - timest
            time.sleep(timest)
            board.turnOff(crossing.rBottom.tLight.st)
            board.turnOff(crossing.rBottom.tLight.rt)
        else:
            # finding time for rLeft rt
            timeRt = crossing.rTop.tLight.getRtTime()
            time.sleep(timeRt)
            # turning off rt
            board.turnOff(crossing.rTop.tLight.rt)
            # turning on rRight st
            board.turnOn(crossing.rBottom.tLight.st)
            #starting timer
            thread.start_new_thread(crossing.rBottom.startTimer, (board.C, crossing.rBottom.tLight.getStTime()))

            # getting update
            crossing.mapc.getUpdate()
            crossing.img = crossing.mapc.fetch()
            # finding time to turn off rLeft st
            timest = crossing.rBottom.tLight.getStTime() - timeRt
            time.sleep(timest)
            # turning off rLeft st
            board.turnOff(crossing.rTop.tLight.st)
            # turning on rRight rt
            board.turnOn(crossing.rBottom.tLight.rt)

            # finding time to turn off both rRight
            timeRt = crossing.rBottom.tLight.getStTime() - timest
            time.sleep(timeRt)
            board.turnOff(crossing.rBottom.tLight.st)
            board.turnOff(crossing.rBottom.tLight.rt)


#controlling the lights
#use your own coordinates comment mine
thread.start_new_thread(controlLight, (c1, 78, 496, 14, 774, 361, 748, 256, 483))
thread.start_new_thread(controlLight, (c2, 13, 670, 0, 0, 362, 772, 412, 406))
thread.start_new_thread(controlLight, (c3, 282, 720, 285, 796, 353, 758, 343, 702))
thread.start_new_thread(controlLight, (c4, 282, 707, 0, 0, 390, 797, 411, 710))
thread.start_new_thread(controlLight, (c5, 259, 568, 260, 706, 376, 811, 0, 0))
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
