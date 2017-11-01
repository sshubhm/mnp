from Road import *
from map import *
class crossing:
    def __init__(self, name, url):
        self.mapc = map(name, url)
        self.mapc.getUpdate()
        self.img = self.mapc.fetch()
        self.name = name
        #self.createRoad(xl,yl,xt,yt,xr,yr,xb,yb,C)
        self.delay = 0

    def createRoad(self,xl,yl,xt,yt,xr,yr,xb,yb,C):
        self.rLeft = Road(xl,yl,C)
        self.rRight = Road(xt,yt,C)
        self.rTop = Road(xr,yr,C)
        self.rBottom = Road(xb,yb,C)
