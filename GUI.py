# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
import vtk
import numpy as np
from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from double_pendulum import DoublePendulum
from MyMplCanvas import MyMplCanvas


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    """ The main window class"""

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # member variables definition
        self.M1 = 0.0
        self.M2 = 0.0
        self.L1 = 0.0
        self.L2 = 0.0

        self.th1 = 0.0
        self.th2 = 0.0
        self.w1 = 0.0
        self.w2 = 0.0

        self.ts = 0.0
        self.te = 0.0
        self.dt = 0.0

        # setup timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.timerCallback)
        self.timer_count = 0
        self.current_time = 0.0

        # dimension of the vtk view 
        self.len_convert_factor = 100.0   # length convert factor 1m = 100 pixels
        self.X_lim = 500.0
        self.Y_lim = 300.0

        # Setup UI widgets
        self.setupUi(self)

    def setupUi(self, MainWindow):
        # mainwindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1203, 694)

        # centralWidget
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        MainWindow.setCentralWidget(self.centralWidget)

        # left setting panel

        # frame
        self.settingFrame = QtGui.QFrame(self.centralWidget)
        self.settingFrame.setGeometry(QtCore.QRect(10, 10, 301, 581))
        self.settingFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.settingFrame.setObjectName(_fromUtf8("settingFrame"))

        # system parameter group
        self.groupBox_system = QtGui.QGroupBox(self.settingFrame)
        self.groupBox_system.setGeometry(QtCore.QRect(20, 20, 261, 121))
        self.groupBox_system.setStyleSheet(_fromUtf8("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}+ QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0px 3px 0 3px}"))
        self.groupBox_system.setObjectName(_fromUtf8("groupBox_system"))
        self.label_M1 = QtGui.QLabel(self.groupBox_system)
        self.label_M1.setGeometry(QtCore.QRect(10, 40, 21, 17))
        self.label_M1.setObjectName(_fromUtf8("label_M1"))
        self.label_M2 = QtGui.QLabel(self.groupBox_system)
        self.label_M2.setGeometry(QtCore.QRect(140, 40, 21, 17))
        self.label_M2.setObjectName(_fromUtf8("label_M2"))
        self.label_L1 = QtGui.QLabel(self.groupBox_system)
        self.label_L1.setGeometry(QtCore.QRect(10, 90, 21, 17))
        self.label_L1.setObjectName(_fromUtf8("label_L1"))
        self.label_L2 = QtGui.QLabel(self.groupBox_system)
        self.label_L2.setGeometry(QtCore.QRect(140, 90, 21, 17))
        self.label_L2.setObjectName(_fromUtf8("label_L2"))
        self.lineEdit_M1 = QtGui.QLineEdit(self.groupBox_system)
        self.lineEdit_M1.setGeometry(QtCore.QRect(40, 30, 71, 27))
        self.lineEdit_M1.setObjectName(_fromUtf8("lineEdit_M1"))
        self.lineEdit_M2 = QtGui.QLineEdit(self.groupBox_system)
        self.lineEdit_M2.setGeometry(QtCore.QRect(170, 30, 71, 27))
        self.lineEdit_M2.setObjectName(_fromUtf8("lineEdit_M2"))
        self.lineEdit_L1 = QtGui.QLineEdit(self.groupBox_system)
        self.lineEdit_L1.setGeometry(QtCore.QRect(40, 80, 71, 27))
        self.lineEdit_L1.setObjectName(_fromUtf8("lineEdit_L1"))
        self.lineEdit_L2 = QtGui.QLineEdit(self.groupBox_system)
        self.lineEdit_L2.setGeometry(QtCore.QRect(170, 80, 71, 27))
        self.lineEdit_L2.setObjectName(_fromUtf8("lineEdit_L2"))

        # initial condition group
        self.groupBox_init = QtGui.QGroupBox(self.settingFrame)
        self.groupBox_init.setGeometry(QtCore.QRect(20, 170, 261, 121))
        self.groupBox_init.setStyleSheet(_fromUtf8("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}+ QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0px 3px 0 3px}"))
        self.groupBox_init.setObjectName(_fromUtf8("groupBox_init"))
        self.label_th1 = QtGui.QLabel(self.groupBox_init)
        self.label_th1.setGeometry(QtCore.QRect(10, 40, 31, 17))
        self.label_th1.setObjectName(_fromUtf8("label_th1"))
        self.label_th2 = QtGui.QLabel(self.groupBox_init)
        self.label_th2.setGeometry(QtCore.QRect(140, 40, 31, 17))
        self.label_th2.setObjectName(_fromUtf8("label_th2"))
        self.label_w1 = QtGui.QLabel(self.groupBox_init)
        self.label_w1.setGeometry(QtCore.QRect(10, 90, 21, 17))
        self.label_w1.setObjectName(_fromUtf8("label_w1"))
        self.label_w2 = QtGui.QLabel(self.groupBox_init)
        self.label_w2.setGeometry(QtCore.QRect(140, 90, 21, 17))
        self.label_w2.setObjectName(_fromUtf8("label_w2"))
        self.lineEdit_th1 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_th1.setGeometry(QtCore.QRect(40, 30, 71, 27))
        self.lineEdit_th1.setObjectName(_fromUtf8("lineEdit_th1"))
        self.lineEdit_w1 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_w1.setGeometry(QtCore.QRect(40, 80, 71, 27))
        self.lineEdit_w1.setObjectName(_fromUtf8("lineEdit_w1"))
        self.lineEdit_th2 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_th2.setGeometry(QtCore.QRect(170, 30, 71, 27))
        self.lineEdit_th2.setObjectName(_fromUtf8("lineEdit_th2"))
        self.lineEdit_w2 = QtGui.QLineEdit(self.groupBox_init)
        self.lineEdit_w2.setGeometry(QtCore.QRect(170, 80, 71, 27))
        self.lineEdit_w2.setObjectName(_fromUtf8("lineEdit_w2"))

        # time setting group
        self.groupBox_time = QtGui.QGroupBox(self.settingFrame)
        self.groupBox_time.setGeometry(QtCore.QRect(20, 310, 261, 131))
        self.groupBox_time.setStyleSheet(_fromUtf8("QGroupBox{border: 1px solid rgb(192, 192, 192); border-radius:9px; font: bold}+ QGroupBox::title{subcontrol-origin: margin; left: 10px; padding: 0px 3px 0 3px}"))
        self.groupBox_time.setObjectName(_fromUtf8("groupBox_time"))
        self.label_ts = QtGui.QLabel(self.groupBox_time)
        self.label_ts.setGeometry(QtCore.QRect(20, 40, 41, 17))
        self.label_ts.setObjectName(_fromUtf8("label_ts"))
        self.label_te = QtGui.QLabel(self.groupBox_time)
        self.label_te.setGeometry(QtCore.QRect(20, 70, 41, 17))
        self.label_te.setObjectName(_fromUtf8("label_te"))
        self.label_dt = QtGui.QLabel(self.groupBox_time)
        self.label_dt.setGeometry(QtCore.QRect(20, 100, 41, 17))
        self.label_dt.setObjectName(_fromUtf8("label_dt"))
        self.lineEdit_ts = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_ts.setGeometry(QtCore.QRect(70, 30, 71, 27))
        self.lineEdit_ts.setObjectName(_fromUtf8("lineEdit_ts"))
        self.lineEdit_te = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_te.setGeometry(QtCore.QRect(70, 60, 71, 27))
        self.lineEdit_te.setObjectName(_fromUtf8("lineEdit_te"))
        self.lineEdit_dt = QtGui.QLineEdit(self.groupBox_time)
        self.lineEdit_dt.setGeometry(QtCore.QRect(70, 90, 71, 27))
        self.lineEdit_dt.setObjectName(_fromUtf8("lineEdit_dt"))

        # pushButton
        self.pushButton_clear = QtGui.QPushButton(self.settingFrame)
        self.pushButton_clear.setGeometry(QtCore.QRect(60, 480, 99, 27))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            _fromUtf8("Icon/clear.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon)
        self.pushButton_clear.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_init = QtGui.QPushButton(self.settingFrame)
        self.pushButton_init.setGeometry(QtCore.QRect(180, 480, 99, 27))
        self.pushButton_init.setObjectName(_fromUtf8("pushButton_init"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            _fromUtf8("Icon/init.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_init.setIcon(icon)
        self.pushButton_init.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_simulate = QtGui.QPushButton(self.settingFrame)
        self.pushButton_simulate.setGeometry(QtCore.QRect(180, 520, 99, 27))
        self.pushButton_simulate.setObjectName(_fromUtf8("pushButton_simulate"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            _fromUtf8("Icon/tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_simulate.setIcon(icon)
        self.pushButton_simulate.setIconSize(QtCore.QSize(20, 20))

        # vtk widget
        self.vtk_widget = QVTKRenderWindowInteractor(self.centralWidget)
        self.vtk_widget.setGeometry(QtCore.QRect(320, 10, 431, 581))
        self.vtk_widget.setObjectName(_fromUtf8("vtk_widget"))
        self.setvtkWidget()


        # plot_widget
        # trajectory
        self.plot_trace = MyMplCanvas(
            self.centralWidget, width=1, height=1, dpi=50, Ndim=2)
        self.plot_trace.setGeometry(QtCore.QRect(760, 10, 431, 285))
        self.plot_trace.setObjectName(_fromUtf8("plot_trace"))
        self.plot_trace.axes.set_xlim(-5, 5)
        self.plot_trace.axes.set_ylim(0, 5)
        # self.plot_trace.lines[0].set_color('red')     # it doesn't work?
        # self.plot_trace.lines[1].set_color('blue')
        self.plot_trace.fig.legend((self.plot_trace.lines[0], self.plot_trace.lines[
                                   1]), ('upper', 'lower'), (0.15, 0.76))

        # phase angle
        self.plot_angle = MyMplCanvas(
            self.centralWidget, width=1, height=1, dpi=50, Ndim=2)
        self.plot_angle.setGeometry(QtCore.QRect(760, 306, 431, 285))
        self.plot_angle.setObjectName(_fromUtf8("plot_angle"))
        self.plot_angle.axes.set_xlim(0, 10)
        self.plot_angle.axes.set_ylim(-1.6, 1.6)


        # menuBar
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1203, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)

        # toolbar
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setIconSize(QtCore.QSize(50, 50))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.actionImport = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/import.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionImport.setIcon(icon)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))

        self.actionExport = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/export.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExport.setIcon(icon)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))

        self.actionInit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/init.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionInit.setIcon(icon)
        self.actionInit.setObjectName(_fromUtf8("actionInit"))

        self.actionSimulate = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSimulate.setIcon(icon)
        self.actionSimulate.setObjectName(_fromUtf8("actionSimulate"))

        self.actionStart = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStart.setIcon(icon)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        
        self.actionStop = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(
            "Icon/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStop.setIcon(icon)
        self.actionStop.setObjectName(_fromUtf8("actionStop"))

        self.actionSave = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(
            "Icon/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))

        self.actionInfo = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(
            "Icon/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionInfo.setIcon(icon)
        self.actionInfo.setObjectName(_fromUtf8("actionInfo"))
        
        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8("Icon/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.mainToolBar.addAction(self.actionImport)
        self.mainToolBar.addAction(self.actionExport)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionInit)
        self.mainToolBar.addAction(self.actionSimulate)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionStart)
        self.mainToolBar.addAction(self.actionStop)
        self.mainToolBar.addAction(self.actionSave)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionInfo)
        self.mainToolBar.addAction(self.actionExit)
        self.mainToolBar.addSeparator()

        # add lineText to the toolbar to display the current time
        self.label_currenttime = QtGui.QLabel(self.mainToolBar)
        self.label_currenttime.setGeometry(QtCore.QRect(800, 25, 60, 30))
        self.label_currenttime.setObjectName(_fromUtf8("label_currenttime"))
        self.label_currenttime.setStyleSheet(
            "QLabel{font-weight: bold; font-size: 22px}")

        self.lineEdit_timer = QtGui.QLineEdit(self.mainToolBar)
        self.lineEdit_timer.setGeometry(QtCore.QRect(870, 20, 100, 40))
        self.lineEdit_timer.setObjectName(_fromUtf8("lineEdit_timer"))
        self.lineEdit_timer.setReadOnly(True)
        self.lineEdit_timer.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

        # Layout management
        #self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        #self.gridLayout.setMargin(11)
        #self.gridLayout.setSpacing(6)
        #self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        #self.gridLayout.addWidget(self.settingFrame, 0, 0, 1, 1)
        #self.gridLayout.addWidget(self.vtk_widget, 0, 1, 1, 1)
        #self.gridLayout.addWidget(self.plot_widget, 0, 2, 1, 1)


        #
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # mainwindow
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

        # system parameter setting group
        self.groupBox_system.setTitle(_translate("MainWindow", "System parameters", None))
        self.label_M1.setText(_translate("MainWindow", "M1", None))
        self.label_M2.setText(_translate("MainWindow", "M2", None))
        self.label_L1.setText(_translate("MainWindow", "L1", None))
        self.label_L2.setText(_translate("MainWindow", "L2", None))

        # initial condition group
        self.groupBox_init.setTitle(_translate("MainWindow", "Initial conditions", None))
        self.label_th1.setText(_translate("MainWindow", "th1", None))
        self.label_th2.setText(_translate("MainWindow", "th2", None))
        self.label_w1.setText(_translate("MainWindow", "w1", None))
        self.label_w2.setText(_translate("MainWindow", "w2", None))

        # time advancement group
        self.groupBox_time.setTitle(_translate("MainWindow", "Time advancement", None))
        self.label_ts.setText(_translate("MainWindow", "tstart", None))
        self.label_te.setText(_translate("MainWindow", "tend", None))
        self.label_dt.setText(_translate("MainWindow", "tstep", None))

        # pushBotton
        self.pushButton_clear.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_init.setText(_translate("MainWindow", "Initialize", None))
        self.pushButton_simulate.setText(_translate("MainWindow", "Simulate", None))

        # toolbar
        self.actionImport.setText(_translate("MainWindow", "Import input", None))
        self.actionImport.setToolTip(_translate("MainWindow", "Import input", None))

        self.actionExport.setText(_translate("MainWindow", "Export input", None))
        self.actionExport.setToolTip(_translate("MainWindow", "Export input", None))

        self.actionInit.setText(_translate("MainWindow", "Initialize", None))
        self.actionInit.setToolTip(_translate("MainWindow", "Initialize", None))

        self.actionSimulate.setText(_translate("MainWindow", "Simulate", None))
        self.actionSimulate.setToolTip(_translate("MainWindow", "Simulate", None))

        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setToolTip(_translate("MainWindow", "Start", None))

        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop", None))

        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSave.setToolTip(_translate("MainWindow", "Save", None))

        self.actionInfo.setText(_translate("MainWindow", "Infomation", None))
        self.actionInfo.setToolTip(_translate("MainWindow", "Infomation", None))

        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))

        self.label_currenttime.setText(_translate("MainWindow", "Time:", None))


    # other class member function
    def setvtkWidget(self):
        """ setup the vtk widget"""
        # Create renderer
        self.ren = vtk.vtkRenderer()
        self.ren.SetBackground(0.1, 0.2, 0.3)
        self.vtk_widget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk_widget.GetRenderWindow().GetInteractor()

        # Two spheres' model
        # upper sphere
        # Create source
        self.sphereU = vtk.vtkSphereSource()
        self.sphereU.SetRadius(10)
        self.sphereU.SetCenter(-10, 250, 0)

        # Create a mapper
        sphereUMapper = vtk.vtkPolyDataMapper()
        sphereUMapper.SetInputConnection(self.sphereU.GetOutputPort())

        # Create an actor
        self.sphereUActor = vtk.vtkActor()
        self.sphereUActor.SetMapper(sphereUMapper)
        self.sphereUActor.GetProperty().SetColor(1.0, 0.2, 0.2)

        self.ren.AddActor(self.sphereUActor)

        # lower sphere
        # Create source
        self.sphereL = vtk.vtkSphereSource()
        self.sphereL.SetRadius(15)
        self.sphereL.SetCenter(50, 100, 0)

        # Create a mapper
        sphereLMapper = vtk.vtkPolyDataMapper()
        sphereLMapper.SetInputConnection(self.sphereL.GetOutputPort())

        # Create an actor
        self.sphereLActor = vtk.vtkActor()
        self.sphereLActor.SetMapper(sphereLMapper)
        self.sphereLActor.GetProperty().SetColor(0.0, 0.5, 1.0)

        self.ren.AddActor(self.sphereLActor)

        # two ropes connected to the spheres
        # upper rope
        self.RopeU = vtk.vtkLineSource()
        self.RopeU.SetPoint1(0, self.Y_lim, 0)
        self.RopeU.SetPoint2(-10, 250, 0)

        RopeUMapper = vtk.vtkPolyDataMapper()
        RopeUMapper.SetInput(self.RopeU.GetOutput())

        RopeUActor = vtk.vtkActor()
        RopeUActor.SetMapper(RopeUMapper)
        # RopeUActor.GetProperty().SetColor(1.0, 0.0, 0.0)
        RopeUActor.GetProperty().SetLineWidth(5)

        self.ren.AddActor(RopeUActor)

        # lower rope
        self.RopeL = vtk.vtkLineSource()
        self.RopeL.SetPoint1(-10, 250, 0)
        self.RopeL.SetPoint2(50, 100, 0)

        RopeLMapper = vtk.vtkPolyDataMapper()
        RopeLMapper.SetInput(self.RopeL.GetOutput())

        RopeLActor = vtk.vtkActor()
        RopeLActor.SetMapper(RopeLMapper)
        # RopeLActor.GetProperty().SetColor(1.0, 0.0, 0.0)
        RopeLActor.GetProperty().SetLineWidth(5)

        self.ren.AddActor(RopeLActor)

        # Create a camera
        camera = vtk.vtkCamera()
        self.ren.SetActiveCamera(camera)
        self.ren.GetActiveCamera().SetPosition(0, 150, 1000)
        self.ren.GetActiveCamera().SetFocalPoint(0, 150, 0)
        self.ren.GetActiveCamera().SetViewUp(0, 1, 0)
        self.ren.GetActiveCamera().UpdateViewport(self.ren)

    def get_input(self):
        """ get input data from the GUI """
        # system parameters
        self.M1 = self.lineEdit_M1.text().toDouble()[0]
        self.M2 = self.lineEdit_M2.text().toDouble()[0]
        self.L1 = self.lineEdit_L1.text().toDouble()[0]
        self.L2 = self.lineEdit_L2.text().toDouble()[0]

        # initial conditions
        self.th1 = self.lineEdit_th1.text().toDouble()[0]
        self.th2 = self.lineEdit_th2.text().toDouble()[0]
        self.w1 = self.lineEdit_w1.text().toDouble()[0]
        self.w2 = self.lineEdit_w2.text().toDouble()[0]

        # time advancement setting
        self.ts = self.lineEdit_ts.text().toDouble()[0]
        self.te = self.lineEdit_te.text().toDouble()[0]
        self.dt = self.lineEdit_dt.text().toDouble()[0]

    def set_input(self):
        # system parameters
        self.lineEdit_M1.setText(str(self.M1))
        self.lineEdit_M2.setText(str(self.M2))
        self.lineEdit_L1.setText(str(self.L1))
        self.lineEdit_L2.setText(str(self.L2))

        # initial conditions
        self.lineEdit_th1.setText(str(self.th1))
        self.lineEdit_th2.setText(str(self.th2))
        self.lineEdit_w1.setText(str(self.w1))
        self.lineEdit_w2.setText(str(self.w2))

        # time advancement setting
        self.lineEdit_ts.setText(str(self.ts))
        self.lineEdit_te.setText(str(self.te))
        self.lineEdit_dt.setText(str(self.dt))


    def timerCallback(self):
        """ timer callback function """
        # update and display the current time
        self.timer_count += 1
        self.current_time = self.timer_count*self.dt
        self.lineEdit_timer.setText(str(self.current_time))

        # terminate the simulation when reaching the preset stop time
        if self.current_time > self.te:
            self.timer.stop()
            return

        # solve the governing system of equations at the current timestep
        t = np.array([self.current_time, self.current_time+self.dt])
        result = self.pendulum.ode_solve(t)

        # update the vtk view to display the results
        X1, Y1, X2, Y2 = result

        # two spheres
        self.sphereU.SetCenter(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)
        self.sphereL.SetCenter(X2*self.len_convert_factor, self.Y_lim+Y2*self.len_convert_factor, 0.0)

        # two ropes
        self.RopeU.SetPoint1(0.0 , self.Y_lim, 0.0)
        self.RopeU.SetPoint2(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)

        self.RopeL.SetPoint1(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)
        self.RopeL.SetPoint2(X2*self.len_convert_factor, self.Y_lim+Y2*self.len_convert_factor, 0.0)

        # upate the vtk view
        self.iren.GetRenderWindow().Render()

    # toolbar slot function
    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionImport_triggered(self):
        """Toolbar import input button slot"""
        filename = QtGui.QFileDialog.getOpenFileName(self, "Open Input file", "input files/")
        if filename == "":
            return
        read_data = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                read_data.append(float(line.strip()))

        # system parameters
        self.M1 = read_data[0]
        self.L1 = read_data[1]
        self.M2 = read_data[2]
        self.L2 = read_data[3]
        # initial conditions
        self.th1 = read_data[4]
        self.th2 = read_data[5]
        self.w1 = read_data[6]
        self.w2 = read_data[7]
        # time advancement setting
        self.ts = read_data[8]
        self.te = read_data[9]
        self.dt = read_data[10]

        # update the GUI
        self.set_input()


    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionExport_triggered(self):
        """Toolbar export input button slot"""
        self.get_input()
        filename = QtGui.QFileDialog.getSaveFileName(self, "Export Input file", "input files/")
        if filename == "":
            return
        with open(filename, 'wb') as f:
            # system parameters
            f.write("%f\n"%self.M1)
            f.write("%f\n"%self.L1)
            f.write("%f\n"%self.M2)
            f.write("%f\n"%self.L2)
            # initial conditions
            f.write("%f\n"%self.th1)
            f.write("%f\n"%self.th2)
            f.write("%f\n"%self.w1)
            f.write("%f\n"%self.w2)
            # time advancement setting
            f.write("%f\n"%self.ts)
            f.write("%f\n"%self.te)
            f.write("%f\n"%self.dt)       

    
    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionInit_triggered(self):
        """Toolbar initialize button slot"""
        # get input data from the GUI
        self.get_input()

        # update the positions of the actors of the vtk based on the input
        X1 = self.L1*np.sin(self.th1)
        Y1 = -self.L1*np.cos(self.th1)
        X2 = X1 + self.L2*np.sin(self.th2)
        Y2 = Y1 - self.L2*np.cos(self.th2)

        # two spheres
        self.sphereU.SetCenter(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)
        self.sphereL.SetCenter(X2*self.len_convert_factor, self.Y_lim+Y2*self.len_convert_factor, 0.0)

        # two ropes
        self.RopeU.SetPoint1(0.0 , self.Y_lim, 0.0)
        self.RopeU.SetPoint2(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)

        self.RopeL.SetPoint1(X1*self.len_convert_factor, self.Y_lim+Y1*self.len_convert_factor, 0.0)
        self.RopeL.SetPoint2(X2*self.len_convert_factor, self.Y_lim+Y2*self.len_convert_factor, 0.0)

        # initialize the time setting
        self.timer_count = 0
        self.current_time = 0.0
        self.lineEdit_timer.setText(str(self.current_time))


        # upate the vtk view
        self.iren.GetRenderWindow().Render()



    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionSimulate_triggered(self):
        """Toolbar simulate button slot"""
        # initialize the simulation
        self.on_actionInit_triggered()

        # create pendulum object and initialize the state
        self.pendulum = DoublePendulum(self.M1, self.M2, self.L1, self.L2)
        self.pendulum.init_status = np.array([self.th1, self.th2, self.w1, self.w2])

        # start time advancement process
        self.timer.start(self.dt*1000.0)     # convert time unit from s to ms

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStart_triggered(self):
        """Toolbar start button slot"""
        self.timer.start(self.dt*1000.0)

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStop_triggered(self):
        """Toolbar stop button slot"""
        self.timer.stop()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionExit_triggered(self):
        """Toolbar exit button slot"""
        self.close()

    # pushbutton slots
    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_clear_clicked(self):
        """pushBotton clear function"""
        # system parameters
        self.lineEdit_M1.setText(str(""))
        self.lineEdit_M2.setText(str(""))
        self.lineEdit_L1.setText(str(""))
        self.lineEdit_L2.setText(str(""))

        # initial conditions
        self.lineEdit_th1.setText(str(""))
        self.lineEdit_th2.setText(str(""))
        self.lineEdit_w1.setText(str(""))
        self.lineEdit_w2.setText(str(""))

        # time advancement setting
        self.lineEdit_ts.setText(str(""))
        self.lineEdit_te.setText(str(""))
        self.lineEdit_dt.setText(str(""))

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_init_clicked(self):
        """pushBotton initialize function"""
        self.on_actionInit_triggered()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_pushButton_simulate_clicked(self):
        """pushBotton simulate function"""
        self.on_actionSimulate_triggered()




if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    window.iren.Initialize()

    sys.exit(app.exec_())