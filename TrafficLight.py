#class TrafficLight

class TrafficLight:
    stColor = 'red'
    rtColor = 'red'
    def __init__(self, a, b, c, d, e, f, g, h, C):

        #Straight
        self.st = C.create_oval(a, b, c, d, fill=self.stColor)

        #Right Turn
        self.rt = C.create_oval(e,f,g,h, fill = self.rtColor)

    def getStTime(self):
        return self.stTime

    def getRtTime(self):
        return self.rtTime

    def setStTime(self, time):
        self.stTime = time

    def setRtTime(self, time):
        self.rtTime = time

    def getStColor(self):
        return self.stColor

    def getRtColor(self):
        return  self.rtColor

    def setStColor(self, color):
        self.stColor = color

    def setRtColor(self, color):
        self.rtColor = color