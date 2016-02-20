from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

class MyMplCanvas(FigureCanvas):
    """Embed the matplotlib into the Qt"""
    def __init__(self, parent=None, width=5, height=4, dpi=100, Ndim=1):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        # self.axes.hold(False)

        self.NLine = Ndim           # Number of lines in this plot
        self.lines = []
        self.xdata = []
        self.ydata = []
        for i in range(self.NLine):
            self.xdata.append([])
            self.ydata.append([])
            line, = self.axes.plot([], [])
            self.lines.append(line)

        self.axes.set_xlim(-1, 3)
        self.axes.set_ylim(-1, 3)

        #
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        # FigureCanvas.setSizePolicy(self,
        #   QtGui.QSizePolicy.Expanding,
        #   QtGui.QSizePolicy.Expanding)

        # FigureCanvas.updateGeometry(self)

    def updateFig(self, data):
        # add the new data points and update the plot
        for i in range(self.NLine):
            self.xdata[i].append(data[i][0])
            self.ydata[i].append(data[i][1])
            self.lines[i].set_data(self.xdata[i], self.ydata[i])
        
        # Update the figure canvas
        self.updateAxisRange()
        self.draw()

    def updateAxisRange(self):
        xlim_min, xlim_max = self.axes.get_xlim()
        ylim_min, ylim_max = self.axes.get_ylim()
        Xmax = np.amax(self.xdata, axis=0)[-1]
        Xmin = np.amin(self.xdata, axis=0)[-1]
        Ymax = np.amax(self.ydata, axis=0)[-1]
        Ymin = np.amin(self.ydata, axis=0)[-1]

        # X limit
        if Xmin < xlim_min:
            if Xmin > 0:
                xlim_min = Xmin/2.0
            else:
                xlim_min = Xmin*2.0

        if Xmax > xlim_max:
            if Xmax > 0:
                xlim_max = Xmax*2.0
            else:
                xlim_max = Xmax/2.0

        # Y limit
        if Ymin < ylim_min:
            if Ymin > 0:
                ylim_min = Ymin/2.0
            else:
                ylim_min = Ymin*2.0

        if Ymax > ylim_max:
            if Ymax > 0:
                ylim_max = Ymax*2.0
            else:
                ylim_max = Ymax/2.0


        self.axes.set_xlim(xlim_min, xlim_max)
        self.axes.set_ylim(ylim_min, ylim_max)  

    def clearAxia(self):
        self.axes.cla()

        self.lines = []
        self.xdata = []
        self.ydata = []
        for i in range(self.NLine):
            self.xdata.append([])
            self.ydata.append([])
            line, = self.axes.plot([], [])
            self.lines.append(line)

        self.axes.set_xlim(-1, 3)
        self.axes.set_ylim(-1, 3)

        self.draw()