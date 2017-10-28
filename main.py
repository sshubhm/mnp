from crossing import *
from CrossingGUI import *

cr1 = crossing("Maharaja",'https://www.google.co.in/maps/@28.7195088,77.0684701,19.25z/data=!5m1!1e1')
cr1.openFirefox()
cr1.getUpdate()

while 1:
    img = cr1.fetch()

    rLeft = Road()
    rTop = Road()
    rRight = Road()
    rBottom = Road()

    #my coordinates comment them if you want to use yours, don't delete
    #rLeft.setColor(color(img[256,634]))
    #rTop.setColor(color(img[338,774]))
    #rRight.setColor(color(img[408,759]))
    #rBottom.setColor(color(img[334,617]))

    # jatin's coordinates
    rLeft.setColor(color(img[258,587]))
    rTop.setColor(color(img[351,743]))
    rRight.setColor(color(img[411,710]))
    rBottom.setColor(color(img[336,594]))

    #rLeft.setColor(color("green"))
    #rTop.setColor(color("green"))
    #rRight.setColor(color("green"))
    #rBottom.setColor(color("green"))


    #creating the board
    board = Draw(rLeft,rRight,rTop,rBottom)
    rLeft.createLight(260,270,270,280,260,290,270,300,board.C)
    rTop.createLight(320,260,330,270,300,260,310,270,board.C)
    rRight.createLight(330,300,340,310,330, 320, 340, 330,board.C)
    rBottom.createLight(270,330,280,340,290, 330, 300, 340,board.C)


    #round robin scheduling
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

    # board.top.after(rLeft.tLight.getTime()*1000,board.glow,rLeft.tLight,roads)
    # board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()),board.glow,rTop.tLight,roads)
    # board.top.after(1000*(rTop.tLight.getTime()+rLeft.tLight.getTime()+rRight.tLight.getTime()),board.glow,rRight.tLight,roads)
    # board.top.after(1000*(rLeft.tLight.getTime()+rTop.tLight.getTime()+rRight.tLight.getTime()+rBottom.tLight.getTime()),board.glow,rBottom.tLight,roads)


    itr = 0
    for road in roads:
        itr = itr + 1
        if road == rLeft:
            board.glow(road.tLight,roads)
            oldTime = road.tLight.getTime()
            continue
        print(oldTime)
        if(itr == 4):
            board.top.after((oldTime) * 1000, cr1.getUpdate)
        board.top.after((oldTime)*1000, board.glow,road.tLight,roads)

        oldTime = oldTime + road.tLight.getTime()

    board.top.after(oldTime*1000, board.glow,roads[0].tLight,roads)

    board.top.after(oldTime*1000, board.quit)

    board.top.mainloop()

