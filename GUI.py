# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
from double_pendulum import DoublePendulum


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


        self.pushButton_start = QtGui.QPushButton(self.settingFrame)
        self.pushButton_start.setGeometry(QtCore.QRect(180, 480, 99, 27))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            _fromUtf8("Icon/tick.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(20, 20))

        # vtk widget
        self.vtk_widget = QtGui.QWidget(self.centralWidget)
        self.vtk_widget.setGeometry(QtCore.QRect(320, 10, 431, 581))
        self.vtk_widget.setObjectName(_fromUtf8("vtk_widget"))


        # plot_widget
        self.plot_widget = QtGui.QWidget(self.centralWidget)
        self.plot_widget.setGeometry(QtCore.QRect(760, 10, 421, 581))
        self.plot_widget.setObjectName(_fromUtf8("plot_widget"))   

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
        
        self.actionExit = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(_fromUtf8("Icon/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        self.mainToolBar.addAction(self.actionStart)
        self.mainToolBar.addAction(self.actionStop)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.actionExit)
        self.mainToolBar.addSeparator()

        # display the current time
        self.label_currenttime = QtGui.QLabel(self.mainToolBar)
        self.label_currenttime.setGeometry(QtCore.QRect(1000, 25, 60, 30))
        self.label_currenttime.setObjectName(_fromUtf8("label_currenttime"))
        self.label_currenttime.setStyleSheet(
            "QLabel{font-weight: bold; font-size: 22px}")

        self.lineEdit_timer = QtGui.QLineEdit(self.mainToolBar)
        self.lineEdit_timer.setGeometry(QtCore.QRect(1070, 20, 100, 40))
        self.lineEdit_timer.setObjectName(_fromUtf8("lineEdit_timer"))
        self.lineEdit_timer.setReadOnly(True)
        self.lineEdit_timer.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))

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
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))

        # toolbar
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setToolTip(_translate("MainWindow", "Start", None))

        self.actionStop.setText(_translate("MainWindow", "Stop", None))
        self.actionStop.setToolTip(_translate("MainWindow", "Stop", None))

        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit", None))

        self.label_currenttime.setText(_translate("MainWindow", "Time:", None))


    # other class member function
    def get_input(self):
        """ get input data from the GUI """
        self.M1 = self.lineEdit_M1.text().toDouble()[0]
        self.M2 = self.lineEdit_M2.text().toDouble()[0]
        self.L1 = self.lineEdit_L1.text().toDouble()[0]
        self.L2 = self.lineEdit_L2.text().toDouble()[0]

        self.th1 = self.lineEdit_th1.text().toDouble()[0]
        self.th2 = self.lineEdit_th2.text().toDouble()[0]
        self.w1 = self.lineEdit_w1.text().toDouble()[0]
        self.w2 = self.lineEdit_w2.text().toDouble()[0]

        self.ts = self.lineEdit_ts.text().toDouble()[0]
        self.te = self.lineEdit_te.text().toDouble()[0]
        self.dt = self.lineEdit_dt.text().toDouble()[0]

    def timerCallback(self):
        """ timer callback function """
        # update and display the current time
        self.timer_count += 1
        self.current_time = self.timer_count*self.dt
        self.lineEdit_timer.setText(str(self.current_time))


    # toolbar slot function
    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStart_triggered(self):
        """Toolbar start button slot"""
        # get input data from the GUI
        self.get_input()

        # create pendulum object
        self.pendulum = DoublePendulum(self.M1, self.M2, self.L1, self.L2)

        # start time advancement process
        self.timer.start(self.dt*1000.0)     # convert time unit from s to ms

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionStop_triggered(self):
        """Toolbar stop button slot"""
        self.timer.stop()

    @QtCore.pyqtSlot() # signal with no arguments
    def on_actionExit_triggered(self):
        """Toolbar exit button slot"""
        self.close()


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    #window.iren.Initialize()

    sys.exit(app.exec_())