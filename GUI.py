# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Setup UI widgets
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1203, 694)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.vtk_widget = QtGui.QWidget(self.centralWidget)
        self.vtk_widget.setGeometry(QtCore.QRect(320, 10, 431, 581))
        self.vtk_widget.setObjectName(_fromUtf8("vtk_widget"))
        self.settingFrame = QtGui.QFrame(self.centralWidget)
        self.settingFrame.setGeometry(QtCore.QRect(10, 10, 301, 581))
        self.settingFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.settingFrame.setObjectName(_fromUtf8("settingFrame"))
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
        self.pushButton_clear = QtGui.QPushButton(self.settingFrame)
        self.pushButton_clear.setGeometry(QtCore.QRect(60, 480, 99, 27))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.pushButton_start = QtGui.QPushButton(self.settingFrame)
        self.pushButton_start.setGeometry(QtCore.QRect(180, 480, 99, 27))
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.plot_widget = QtGui.QWidget(self.centralWidget)
        self.plot_widget.setGeometry(QtCore.QRect(760, 10, 421, 581))
        self.plot_widget.setObjectName(_fromUtf8("plot_widget"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1203, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setIconSize(QtCore.QSize(50, 50))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.actionStart = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icon/start.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionStart.setIcon(icon)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.mainToolBar.addAction(self.actionStart)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_system.setTitle(_translate("MainWindow", "System parameters", None))
        self.label_M1.setText(_translate("MainWindow", "M1", None))
        self.label_M2.setText(_translate("MainWindow", "M2", None))
        self.label_L1.setText(_translate("MainWindow", "L1", None))
        self.label_L2.setText(_translate("MainWindow", "L2", None))
        self.groupBox_init.setTitle(_translate("MainWindow", "Initial conditions", None))
        self.label_th1.setText(_translate("MainWindow", "th1", None))
        self.label_th2.setText(_translate("MainWindow", "th2", None))
        self.label_w1.setText(_translate("MainWindow", "w1", None))
        self.label_w2.setText(_translate("MainWindow", "w2", None))
        self.groupBox_time.setTitle(_translate("MainWindow", "Time advancement", None))
        self.label_ts.setText(_translate("MainWindow", "tstart", None))
        self.label_te.setText(_translate("MainWindow", "tend", None))
        self.label_dt.setText(_translate("MainWindow", "tstep", None))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_start.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionStart.setToolTip(_translate("MainWindow", "Start", None))


if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
 
    window = Ui_MainWindow()

    window.show()

    #window.iren.Initialize()

    sys.exit(app.exec_())