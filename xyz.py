# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'python.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_TempService(object):
    def setupUi(self, TempService):
        TempService.setObjectName("TempService")
        TempService.resize(924, 600)
        self.centralwidget = QtWidgets.QWidget(TempService)
        self.centralwidget.setObjectName("centralwidget")
        self.shutDown = QtWidgets.QPushButton(self.centralwidget)
        self.shutDown.setGeometry(QtCore.QRect(90, 430, 131, 81))
        self.shutDown.setObjectName("shutDown")
        self.reboot = QtWidgets.QPushButton(self.centralwidget)
        self.reboot.setGeometry(QtCore.QRect(260, 430, 131, 81))
        self.reboot.setObjectName("reboot")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(420, 430, 131, 81))
        self.exit.setObjectName("exit")
        self.Temp = QtWidgets.QLCDNumber(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(580, 40, 321, 81))
        self.Temp.setObjectName("Temp")
        self.Humid = QtWidgets.QLCDNumber(self.centralwidget)
        self.Humid.setGeometry(QtCore.QRect(580, 160, 321, 81))
        self.Humid.setObjectName("Humid")
        self.TempImg = QtWidgets.QLabel(self.centralwidget)
        self.TempImg.setGeometry(QtCore.QRect(520, 60, 50, 50))
        self.TempImg.setText("")
        self.TempImg.setPixmap(QtGui.QPixmap("../Pictures/temp.jpg"))
        self.TempImg.setObjectName("TempImg")
        self.HumidImg = QtWidgets.QLabel(self.centralwidget)
        self.HumidImg.setGeometry(QtCore.QRect(520, 180, 50, 50))
        self.HumidImg.setText("")
        self.HumidImg.setPixmap(QtGui.QPixmap("../Pictures/humid.jpeg"))
        self.HumidImg.setObjectName("HumidImg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 60, 151, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 151, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 151, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, 230, 151, 151))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 230, 151, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 230, 151, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Pictures/server.png"))
        self.label_6.setObjectName("label_6")
        TempService.setCentralWidget(self.centralwidget)
        self.TempServ = QtWidgets.QMenuBar(TempService)
        self.TempServ.setGeometry(QtCore.QRect(0, 0, 924, 19))
        self.TempServ.setObjectName("TempServ")
        TempService.setMenuBar(self.TempServ)
        self.statusbar = QtWidgets.QStatusBar(TempService)
        self.statusbar.setObjectName("statusbar")
        TempService.setStatusBar(self.statusbar)

        self.retranslateUi(TempService)
        QtCore.QMetaObject.connectSlotsByName(TempService)

    def retranslateUi(self, TempService):
        _translate = QtCore.QCoreApplication.translate
        TempService.setWindowTitle(_translate("TempService", "MainWindow"))
        self.shutDown.setText(_translate("TempService", "Shut Down"))
        self.reboot.setText(_translate("TempService", "reboot"))
        self.exit.setText(_translate("TempService", "Exit"))

def run():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.show()

    app.exec()
    
run()