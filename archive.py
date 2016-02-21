class archive():
    """archive of the results"""

    def __init__(self):
        self.t = []
        self.X1 = []
        self.Y1 = []
        self.X2 = []
        self.Y2 = []
        self.th1 = []
        self.th2 = []

    def getLen(self):
        return len(self.t)

    def addData(self, result):
        self.t.append(result[0])
        self.X1.append(result[1])
        self.Y1.append(result[2])
        self.X2.append(result[3])
        self.Y2.append(result[4])
        self.th1.append(result[5])
        self.th2.append(result[6])

