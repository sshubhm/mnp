from Road import *

class crossing:
    def __init__(self, name):
        self.name = name
        self.createRoad()
        self.delay = 0

    def createRoad(self):
        self.rLeft = Road()
        self.rRight = Road()
        self.rTop = Road()
        self.rBottom = Road()