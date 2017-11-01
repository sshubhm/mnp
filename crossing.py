from Road import *
from map import *
class crossing:
    def __init__(self, name, url):
        self.mapc = map(name, url)
        self.mapc.getUpdate()
        self.img = self.mapc.fetch()
        self.name = name
        self.createRoad()
        self.delay = 0

    def createRoad(self):
        self.rLeft = Road()
        self.rRight = Road()
        self.rTop = Road()
        self.rBottom = Road()