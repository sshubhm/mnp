#class TrafficLight

class TrafficLight:
    color = 'red'
    def __init__(self, a, b, c, d, e, f, g, h, C):

        #Straight
        self.oval = C.create_oval(a, b, c, d, fill=self.color)

        #Right Turn
        self.oval = C.create_oval(e,f,g,h, fill = self.color)

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def getTLColor(self):
        return self.color

    def setTLColor(self, color):
        self.color = color

    def toggle(self,C):
        c = self.getTLColor()
        print(c)
        if c == 'red':
            c = 'green'
            self.setTLColor(c)
        else:
            c = 'red'
            self.setTLColor(c)
        C.itemconfig(self.oval, fill=c);