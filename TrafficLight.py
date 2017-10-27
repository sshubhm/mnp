#class TrafficLight

class TrafficLight:
    def __init__(self, a, b, c, d, C):
        ovalB = C.create_oval(a, b, c, d, fill="green")

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getTLcolor(self):
        return self.color

    def setTLColor(self, color):
        self.color = color