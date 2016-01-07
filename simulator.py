# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import elevatorMove as move
import dataParsing




import threading

import elevatorMove as eleMove

import ThreadEli

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

global ui
global dasom
dasom =26
global dialog
global data

preDeparture1 = 1
preDeparture2 = 1
preDeparture3 = 1
preDeparture4 = 1

class Ui_MainWindow(object):
    #def __init__(self, parent=None):
        #self.thread = GUIThread()
        #self.thread.start()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1603, 905)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.timeSlider = QtGui.QSlider(self.centralwidget)
        self.timeSlider.setGeometry(QtCore.QRect(120, 50, 581, 22))
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName(_fromUtf8("timeSlider"))
        self.chartLine = QtGui.QFrame(self.centralwidget)
        self.chartLine.setGeometry(QtCore.QRect(0, 40, 20, 681))
        self.chartLine.setFrameShape(QtGui.QFrame.VLine)
        self.chartLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.chartLine.setObjectName(_fromUtf8("chartLine"))
        self.line_h_1 = QtGui.QFrame(self.centralwidget)
        self.line_h_1.setGeometry(QtCore.QRect(10, 710, 771, 21))
        self.line_h_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_1.setObjectName(_fromUtf8("line_h_1"))
        self.OKButton = QtGui.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(680, 20, 51, 21))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.humanTable = QtGui.QTableWidget(self.centralwidget)
        self.humanTable.setGeometry(QtCore.QRect(60, 120, 101, 601))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humanTable.sizePolicy().hasHeightForWidth())
        self.humanTable.setSizePolicy(sizePolicy)
        self.humanTable.setAutoFillBackground(False)
        self.humanTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.humanTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.humanTable.setObjectName(_fromUtf8("humanTable"))
        self.humanTable.setColumnCount(1)
        self.humanTable.setRowCount(20)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setVerticalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable.setItem(0, 0, item)
        self.humanTable.horizontalHeader().setVisible(False)
        self.humanTable.horizontalHeader().setHighlightSections(False)
        self.humanTable.verticalHeader().setVisible(False)
        self.humanTable.verticalHeader().setHighlightSections(False)
        self.human = QtGui.QLabel(self.centralwidget)
        self.human.setGeometry(QtCore.QRect(100, 100, 31, 16))
        self.human.setObjectName(_fromUtf8("human"))
        self.Car1 = QtGui.QLabel(self.centralwidget)
        self.Car1.setGeometry(QtCore.QRect(250, 720, 31, 16))
        self.Car1.setObjectName(_fromUtf8("Car1"))
        self.Car2 = QtGui.QLabel(self.centralwidget)
        self.Car2.setGeometry(QtCore.QRect(390, 720, 31, 16))
        self.Car2.setObjectName(_fromUtf8("Car2"))
        self.Car3 = QtGui.QLabel(self.centralwidget)
        self.Car3.setGeometry(QtCore.QRect(530, 720, 31, 21))
        self.Car3.setObjectName(_fromUtf8("Car3"))
        self.Car4 = QtGui.QLabel(self.centralwidget)
        self.Car4.setGeometry(QtCore.QRect(670, 720, 31, 16))
        self.Car4.setObjectName(_fromUtf8("Car4"))
        self.line_v_1 = QtGui.QFrame(self.centralwidget)
        self.line_v_1.setGeometry(QtCore.QRect(190, 120, 20, 721))
        self.line_v_1.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_1.setObjectName(_fromUtf8("line_v_1"))
        self.line_v_2 = QtGui.QFrame(self.centralwidget)
        self.line_v_2.setGeometry(QtCore.QRect(330, 120, 20, 711))
        self.line_v_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_2.setObjectName(_fromUtf8("line_v_2"))
        self.line_v_3 = QtGui.QFrame(self.centralwidget)
        self.line_v_3.setGeometry(QtCore.QRect(470, 120, 20, 721))
        self.line_v_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_3.setObjectName(_fromUtf8("line_v_3"))
        self.line_v_4 = QtGui.QFrame(self.centralwidget)
        self.line_v_4.setGeometry(QtCore.QRect(610, 120, 20, 721))
        self.line_v_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_4.setObjectName(_fromUtf8("line_v_4"))
        self.elevator1 = QtGui.QPushButton(self.centralwidget)
        self.elevator1.setGeometry(QtCore.QRect(200, 690, 21, 31))
        self.elevator1.setObjectName(_fromUtf8("elevator1"))
        self.elevator1.setEnabled(False)
        self.elevator2 = QtGui.QPushButton(self.centralwidget)
        self.elevator2.setGeometry(QtCore.QRect(340, 690, 21, 31))
        self.elevator2.setObjectName(_fromUtf8("elevator2"))
        self.elevator2.setEnabled(False)
        self.elevator3 = QtGui.QPushButton(self.centralwidget)
        self.elevator3.setGeometry(QtCore.QRect(480, 690, 21, 31))
        self.elevator3.setObjectName(_fromUtf8("elevator3"))
        self.elevator3.setEnabled(False)
        self.elevator4 = QtGui.QPushButton(self.centralwidget)
        self.elevator4.setGeometry(QtCore.QRect(620, 690, 21, 31))
        self.elevator4.setObjectName(_fromUtf8("elevator4"))
        self.elevator4.setEnabled(False)
        self.line_h_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_2.setGeometry(QtCore.QRect(200, 680, 541, 21))
        self.line_h_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_2.setObjectName(_fromUtf8("line_h_2"))
        self.line_h_3 = QtGui.QFrame(self.centralwidget)
        self.line_h_3.setGeometry(QtCore.QRect(200, 650, 541, 21))
        self.line_h_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_3.setObjectName(_fromUtf8("line_h_3"))
        self.line_h_4 = QtGui.QFrame(self.centralwidget)
        self.line_h_4.setGeometry(QtCore.QRect(200, 620, 541, 21))
        self.line_h_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_4.setObjectName(_fromUtf8("line_h_4"))
        self.line_h_5 = QtGui.QFrame(self.centralwidget)
        self.line_h_5.setGeometry(QtCore.QRect(200, 590, 541, 21))
        self.line_h_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_5.setObjectName(_fromUtf8("line_h_5"))
        self.line_h_6 = QtGui.QFrame(self.centralwidget)
        self.line_h_6.setGeometry(QtCore.QRect(200, 560, 541, 21))
        self.line_h_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_6.setObjectName(_fromUtf8("line_h_6"))
        self.line_h_7 = QtGui.QFrame(self.centralwidget)
        self.line_h_7.setGeometry(QtCore.QRect(200, 530, 541, 21))
        self.line_h_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_7.setObjectName(_fromUtf8("line_h_7"))
        self.line_h_8 = QtGui.QFrame(self.centralwidget)
        self.line_h_8.setGeometry(QtCore.QRect(200, 500, 541, 21))
        self.line_h_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_8.setObjectName(_fromUtf8("line_h_8"))
        self.line_h_9 = QtGui.QFrame(self.centralwidget)
        self.line_h_9.setGeometry(QtCore.QRect(200, 470, 541, 21))
        self.line_h_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_9.setObjectName(_fromUtf8("line_h_9"))
        self.line_h_10 = QtGui.QFrame(self.centralwidget)
        self.line_h_10.setGeometry(QtCore.QRect(200, 440, 541, 21))
        self.line_h_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_10.setObjectName(_fromUtf8("line_h_10"))
        self.line_h_11 = QtGui.QFrame(self.centralwidget)
        self.line_h_11.setGeometry(QtCore.QRect(200, 410, 541, 21))
        self.line_h_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_11.setObjectName(_fromUtf8("line_h_11"))
        self.line_h_12 = QtGui.QFrame(self.centralwidget)
        self.line_h_12.setGeometry(QtCore.QRect(200, 380, 541, 21))
        self.line_h_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_12.setObjectName(_fromUtf8("line_h_12"))
        self.line_h_13 = QtGui.QFrame(self.centralwidget)
        self.line_h_13.setGeometry(QtCore.QRect(200, 350, 541, 21))
        self.line_h_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_13.setObjectName(_fromUtf8("line_h_13"))
        self.line_h_14 = QtGui.QFrame(self.centralwidget)
        self.line_h_14.setGeometry(QtCore.QRect(200, 320, 541, 21))
        self.line_h_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_14.setObjectName(_fromUtf8("line_h_14"))
        self.line_h_15 = QtGui.QFrame(self.centralwidget)
        self.line_h_15.setGeometry(QtCore.QRect(200, 290, 541, 21))
        self.line_h_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_15.setObjectName(_fromUtf8("line_h_15"))
        self.line_h_16 = QtGui.QFrame(self.centralwidget)
        self.line_h_16.setGeometry(QtCore.QRect(200, 260, 541, 21))
        self.line_h_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_16.setObjectName(_fromUtf8("line_h_16"))
        self.line_h_17 = QtGui.QFrame(self.centralwidget)
        self.line_h_17.setGeometry(QtCore.QRect(200, 230, 541, 21))
        self.line_h_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_17.setObjectName(_fromUtf8("line_h_17"))
        self.line_h_18 = QtGui.QFrame(self.centralwidget)
        self.line_h_18.setGeometry(QtCore.QRect(200, 200, 541, 21))
        self.line_h_18.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_18.setObjectName(_fromUtf8("line_h_18"))
        self.line_h_19 = QtGui.QFrame(self.centralwidget)
        self.line_h_19.setGeometry(QtCore.QRect(200, 170, 541, 21))
        self.line_h_19.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_19.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_19.setObjectName(_fromUtf8("line_h_19"))
        self.line_h_20 = QtGui.QFrame(self.centralwidget)
        self.line_h_20.setGeometry(QtCore.QRect(200, 140, 541, 21))
        self.line_h_20.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_20.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_20.setObjectName(_fromUtf8("line_h_20"))
        self.timeSliderValue24 = QtGui.QLabel(self.centralwidget)
        self.timeSliderValue24.setGeometry(QtCore.QRect(690, 70, 31, 16))
        self.timeSliderValue24.setObjectName(_fromUtf8("timeSliderValue24"))
        self.timeSliderValue12 = QtGui.QLabel(self.centralwidget)
        self.timeSliderValue12.setGeometry(QtCore.QRect(420, 70, 31, 16))
        self.timeSliderValue12.setObjectName(_fromUtf8("timeSliderValue12"))
        self.waitingtime1 = QtGui.QLabel(self.centralwidget)
        self.waitingtime1.setGeometry(QtCore.QRect(200, 750, 71, 20))
        self.waitingtime1.setObjectName(_fromUtf8("waitingtime1"))
        self.startfloor1 = QtGui.QLabel(self.centralwidget)
        self.startfloor1.setGeometry(QtCore.QRect(210, 780, 61, 21))
        self.startfloor1.setObjectName(_fromUtf8("startfloor1"))
        self.destination1 = QtGui.QLabel(self.centralwidget)
        self.destination1.setGeometry(QtCore.QRect(210, 810, 61, 20))
        self.destination1.setObjectName(_fromUtf8("destination1"))
        self.waitingtimeText = QtGui.QLabel(self.centralwidget)
        self.waitingtimeText.setGeometry(QtCore.QRect(300, 750, 53, 19))
        self.waitingtimeText.setObjectName(_fromUtf8("waitingtimeText"))
        self.textEdit_7 = QtGui.QLabel(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(300, 780, 53, 19))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.destinationText = QtGui.QLabel(self.centralwidget)
        self.destinationText.setGeometry(QtCore.QRect(300, 810, 53, 19))
        self.destinationText.setObjectName(_fromUtf8("destinationText"))
        self.hallcall = QtGui.QPushButton(self.centralwidget)
        self.hallcall.setGeometry(QtCore.QRect(160, 690, 21, 31))
        self.hallcall.setObjectName(_fromUtf8("hallcall"))
        self.hallcall.setEnabled(False)
        self.startfloor2 = QtGui.QLabel(self.centralwidget)
        self.startfloor2.setGeometry(QtCore.QRect(350, 780, 61, 21))
        self.startfloor2.setObjectName(_fromUtf8("startfloor2"))
        self.textEdit_9 = QtGui.QLabel(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(440, 750, 53, 19))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.destination2 = QtGui.QLabel(self.centralwidget)
        self.destination2.setGeometry(QtCore.QRect(350, 810, 61, 20))
        self.destination2.setObjectName(_fromUtf8("destination2"))
        self.textEdit_10 = QtGui.QLabel(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(440, 810, 53, 19))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.waitingtime2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime2.setGeometry(QtCore.QRect(340, 750, 71, 20))
        self.waitingtime2.setObjectName(_fromUtf8("waitingtime2"))
        self.textEdit_11 = QtGui.QLabel(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(440, 780, 53, 19))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.textEdit_12 = QtGui.QLabel(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(580, 750, 53, 19))
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.destination3 = QtGui.QLabel(self.centralwidget)
        self.destination3.setGeometry(QtCore.QRect(490, 810, 61, 20))
        self.destination3.setObjectName(_fromUtf8("destination3"))
        self.textEdit_13 = QtGui.QLabel(self.centralwidget)
        self.textEdit_13.setGeometry(QtCore.QRect(580, 810, 53, 19))
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
        self.textEdit_14 = QtGui.QLabel(self.centralwidget)
        self.textEdit_14.setGeometry(QtCore.QRect(580, 780, 53, 19))
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.startfloor3 = QtGui.QLabel(self.centralwidget)
        self.startfloor3.setGeometry(QtCore.QRect(490, 780, 61, 21))
        self.startfloor3.setObjectName(_fromUtf8("startfloor3"))
        self.waitingtime3 = QtGui.QLabel(self.centralwidget)
        self.waitingtime3.setGeometry(QtCore.QRect(480, 750, 71, 20))
        self.waitingtime3.setObjectName(_fromUtf8("waitingtime3"))
        self.textEdit_15 = QtGui.QLabel(self.centralwidget)
        self.textEdit_15.setGeometry(QtCore.QRect(720, 750, 53, 19))
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.destination4 = QtGui.QLabel(self.centralwidget)
        self.destination4.setGeometry(QtCore.QRect(630, 810, 61, 20))
        self.destination4.setObjectName(_fromUtf8("destination4"))
        self.textEdit_16 = QtGui.QLabel(self.centralwidget)
        self.textEdit_16.setGeometry(QtCore.QRect(720, 810, 53, 19))
        self.textEdit_16.setObjectName(_fromUtf8("textEdit_16"))
        self.textEdit_17 = QtGui.QLabel(self.centralwidget)
        self.textEdit_17.setGeometry(QtCore.QRect(720, 780, 53, 19))
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.startfloor4 = QtGui.QLabel(self.centralwidget)
        self.startfloor4.setGeometry(QtCore.QRect(630, 780, 61, 21))
        self.startfloor4.setObjectName(_fromUtf8("startfloor4"))
        self.waitingtime3_2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime3_2.setGeometry(QtCore.QRect(620, 750, 71, 20))
        self.waitingtime3_2.setObjectName(_fromUtf8("waitingtime3_2"))
        self.line_51 = QtGui.QFrame(self.centralwidget)
        self.line_51.setGeometry(QtCore.QRect(790, 0, 20, 881))
        self.line_51.setFrameShape(QtGui.QFrame.VLine)
        self.line_51.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_51.setObjectName(_fromUtf8("line_51"))
        self.yearText = QtGui.QTextEdit(self.centralwidget)
        self.yearText.setGeometry(QtCore.QRect(110, 20, 71, 21))
        self.yearText.setObjectName(_fromUtf8("yearText"))
        self.date = QtGui.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(80, 20, 31, 21))
        self.date.setObjectName(_fromUtf8("date"))
        self.year = QtGui.QLabel(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(180, 20, 16, 21))
        self.year.setObjectName(_fromUtf8("year"))
        self.monthText = QtGui.QTextEdit(self.centralwidget)
        self.monthText.setGeometry(QtCore.QRect(200, 20, 71, 21))
        self.monthText.setObjectName(_fromUtf8("monthText"))
        self.month = QtGui.QLabel(self.centralwidget)
        self.month.setGeometry(QtCore.QRect(270, 20, 31, 21))
        self.month.setObjectName(_fromUtf8("month"))
        self.dayText = QtGui.QTextEdit(self.centralwidget)
        self.dayText.setGeometry(QtCore.QRect(290, 20, 71, 21))
        self.dayText.setObjectName(_fromUtf8("dayText"))
        self.day = QtGui.QLabel(self.centralwidget)
        self.day.setGeometry(QtCore.QRect(360, 20, 16, 21))
        self.day.setObjectName(_fromUtf8("day"))
        self.time = QtGui.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(380, 20, 31, 21))
        self.time.setObjectName(_fromUtf8("time"))
        self.minute = QtGui.QLabel(self.centralwidget)
        self.minute.setGeometry(QtCore.QRect(570, 20, 16, 21))
        self.minute.setObjectName(_fromUtf8("minute"))
        self.hourText = QtGui.QTextEdit(self.centralwidget)
        self.hourText.setGeometry(QtCore.QRect(410, 20, 71, 21))
        self.hourText.setObjectName(_fromUtf8("hourText"))
        self.minuteText = QtGui.QTextEdit(self.centralwidget)
        self.minuteText.setGeometry(QtCore.QRect(500, 20, 71, 21))
        self.minuteText.setObjectName(_fromUtf8("minuteText"))
        self.hour = QtGui.QLabel(self.centralwidget)
        self.hour.setGeometry(QtCore.QRect(480, 20, 16, 21))
        self.hour.setObjectName(_fromUtf8("hour"))
        self.line_v_4_2 = QtGui.QFrame(self.centralwidget)
        self.line_v_4_2.setGeometry(QtCore.QRect(1440, 140, 20, 721))
        self.line_v_4_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_4_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_4_2.setObjectName(_fromUtf8("line_v_4_2"))
        self.line_h_13_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_13_2.setGeometry(QtCore.QRect(1030, 370, 541, 21))
        self.line_h_13_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_13_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_13_2.setObjectName(_fromUtf8("line_h_13_2"))
        self.elevator1_2 = QtGui.QPushButton(self.centralwidget)
        self.elevator1_2.setGeometry(QtCore.QRect(1030, 470, 21, 31))
        self.elevator1_2.setObjectName(_fromUtf8("elevator1_2"))
        self.line_h_14_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_14_2.setGeometry(QtCore.QRect(1030, 340, 541, 21))
        self.line_h_14_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_14_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_14_2.setObjectName(_fromUtf8("line_h_14_2"))
        self.waitingtime2_2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime2_2.setGeometry(QtCore.QRect(1170, 770, 71, 20))
        self.waitingtime2_2.setObjectName(_fromUtf8("waitingtime2_2"))
        self.hallcall_2 = QtGui.QPushButton(self.centralwidget)
        self.hallcall_2.setGeometry(QtCore.QRect(160, 690, 21, 31))
        self.hallcall_2.setObjectName(_fromUtf8("hallcall_2"))
        self.hallcall_2.setEnabled(False)
        self.textEdit_18 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_18.setGeometry(QtCore.QRect(1250, 830, 53, 19))
        self.textEdit_18.setObjectName(_fromUtf8("textEdit_18"))
        self.minute_2 = QtGui.QLabel(self.centralwidget)
        self.minute_2.setGeometry(QtCore.QRect(1400, 40, 16, 21))
        self.minute_2.setObjectName(_fromUtf8("minute_2"))
        self.minuteText_2 = QtGui.QTextEdit(self.centralwidget)
        self.minuteText_2.setGeometry(QtCore.QRect(1330, 40, 71, 21))
        self.minuteText_2.setObjectName(_fromUtf8("minuteText_2"))
        self.textEdit_19 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_19.setGeometry(QtCore.QRect(1390, 770, 53, 19))
        self.textEdit_19.setObjectName(_fromUtf8("textEdit_19"))
        self.elevator4_2 = QtGui.QPushButton(self.centralwidget)
        self.elevator4_2.setGeometry(QtCore.QRect(1450, 320, 21, 31))
        self.elevator4_2.setObjectName(_fromUtf8("elevator4_2"))
        self.startfloor4_2 = QtGui.QLabel(self.centralwidget)
        self.startfloor4_2.setGeometry(QtCore.QRect(1460, 800, 61, 21))
        self.startfloor4_2.setObjectName(_fromUtf8("startfloor4_2"))
        self.line_h_18_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_18_2.setGeometry(QtCore.QRect(1030, 220, 541, 21))
        self.line_h_18_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_18_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_18_2.setObjectName(_fromUtf8("line_h_18_2"))
        self.textEdit_20 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_20.setGeometry(QtCore.QRect(1530, 830, 53, 19))
        self.textEdit_20.setObjectName(_fromUtf8("textEdit_20"))
        self.line_h_5_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_5_2.setGeometry(QtCore.QRect(1030, 610, 541, 21))
        self.line_h_5_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_5_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_5_2.setObjectName(_fromUtf8("line_h_5_2"))
        self.dayText_2 = QtGui.QTextEdit(self.centralwidget)
        self.dayText_2.setGeometry(QtCore.QRect(1120, 40, 71, 21))
        self.dayText_2.setObjectName(_fromUtf8("dayText_2"))
        self.hour_2 = QtGui.QLabel(self.centralwidget)
        self.hour_2.setGeometry(QtCore.QRect(1310, 40, 16, 21))
        self.hour_2.setObjectName(_fromUtf8("hour_2"))
        self.line_h_10_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_10_2.setGeometry(QtCore.QRect(1030, 460, 541, 21))
        self.line_h_10_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_10_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_10_2.setObjectName(_fromUtf8("line_h_10_2"))
        self.destination1_2 = QtGui.QLabel(self.centralwidget)
        self.destination1_2.setGeometry(QtCore.QRect(1040, 830, 61, 20))
        self.destination1_2.setObjectName(_fromUtf8("destination1_2"))
        self.startfloor3_2 = QtGui.QLabel(self.centralwidget)
        self.startfloor3_2.setGeometry(QtCore.QRect(1320, 800, 61, 21))
        self.startfloor3_2.setObjectName(_fromUtf8("startfloor3_2"))
        self.destinationText_2 = QtGui.QTextEdit(self.centralwidget)
        self.destinationText_2.setGeometry(QtCore.QRect(1110, 830, 53, 19))
        self.destinationText_2.setObjectName(_fromUtf8("destinationText_2"))
        self.line_v_3_2 = QtGui.QFrame(self.centralwidget)
        self.line_v_3_2.setGeometry(QtCore.QRect(1300, 140, 20, 721))
        self.line_v_3_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_3_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_3_2.setObjectName(_fromUtf8("line_v_3_2"))
        self.destination2_2 = QtGui.QLabel(self.centralwidget)
        self.destination2_2.setGeometry(QtCore.QRect(1180, 830, 61, 20))
        self.destination2_2.setObjectName(_fromUtf8("destination2_2"))
        self.textEdit_21 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_21.setGeometry(QtCore.QRect(1250, 770, 53, 19))
        self.textEdit_21.setObjectName(_fromUtf8("textEdit_21"))
        self.line_h_6_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_6_2.setGeometry(QtCore.QRect(1030, 580, 541, 21))
        self.line_h_6_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_6_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_6_2.setObjectName(_fromUtf8("line_h_6_2"))
        self.Car3_2 = QtGui.QLabel(self.centralwidget)
        self.Car3_2.setGeometry(QtCore.QRect(1360, 740, 31, 21))
        self.Car3_2.setObjectName(_fromUtf8("Car3_2"))
        self.destination4_2 = QtGui.QLabel(self.centralwidget)
        self.destination4_2.setGeometry(QtCore.QRect(1460, 830, 61, 20))
        self.destination4_2.setObjectName(_fromUtf8("destination4_2"))
        self.textEdit_22 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_22.setGeometry(QtCore.QRect(1530, 770, 53, 19))
        self.textEdit_22.setObjectName(_fromUtf8("textEdit_22"))
        self.textEdit_23 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_23.setGeometry(QtCore.QRect(1250, 800, 53, 19))
        self.textEdit_23.setObjectName(_fromUtf8("textEdit_23"))
        self.waitingtime1_2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime1_2.setGeometry(QtCore.QRect(1030, 770, 71, 20))
        self.waitingtime1_2.setObjectName(_fromUtf8("waitingtime1_2"))
        self.line_h_11_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_11_2.setGeometry(QtCore.QRect(1030, 430, 541, 21))
        self.line_h_11_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_11_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_11_2.setObjectName(_fromUtf8("line_h_11_2"))
        self.textEdit_8 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(1110, 800, 53, 19))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.startfloor1_2 = QtGui.QLabel(self.centralwidget)
        self.startfloor1_2.setGeometry(QtCore.QRect(1040, 800, 61, 21))
        self.startfloor1_2.setObjectName(_fromUtf8("startfloor1_2"))
        self.month_2 = QtGui.QLabel(self.centralwidget)
        self.month_2.setGeometry(QtCore.QRect(1100, 40, 31, 21))
        self.month_2.setObjectName(_fromUtf8("month_2"))
        self.Car2_2 = QtGui.QLabel(self.centralwidget)
        self.Car2_2.setGeometry(QtCore.QRect(1220, 740, 31, 16))
        self.Car2_2.setObjectName(_fromUtf8("Car2_2"))
        self.line_h_9_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_9_2.setGeometry(QtCore.QRect(1030, 490, 541, 21))
        self.line_h_9_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_9_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_9_2.setObjectName(_fromUtf8("line_h_9_2"))
        self.yearText_2 = QtGui.QTextEdit(self.centralwidget)
        self.yearText_2.setGeometry(QtCore.QRect(940, 40, 71, 21))
        self.yearText_2.setObjectName(_fromUtf8("yearText_2"))
        self.day_2 = QtGui.QLabel(self.centralwidget)
        self.day_2.setGeometry(QtCore.QRect(1190, 40, 16, 21))
        self.day_2.setObjectName(_fromUtf8("day_2"))
        self.line_v_1_2 = QtGui.QFrame(self.centralwidget)
        self.line_v_1_2.setGeometry(QtCore.QRect(1020, 140, 20, 721))
        self.line_v_1_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_1_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_1_2.setObjectName(_fromUtf8("line_v_1_2"))
        self.date_2 = QtGui.QLabel(self.centralwidget)
        self.date_2.setGeometry(QtCore.QRect(910, 40, 31, 21))
        self.date_2.setObjectName(_fromUtf8("date_2"))
        self.human_2 = QtGui.QLabel(self.centralwidget)
        self.human_2.setGeometry(QtCore.QRect(930, 120, 31, 16))
        self.human_2.setObjectName(_fromUtf8("human_2"))
        self.line_h_19_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_19_2.setGeometry(QtCore.QRect(1030, 190, 541, 21))
        self.line_h_19_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_19_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_19_2.setObjectName(_fromUtf8("line_h_19_2"))
        self.line_h_3_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_3_2.setGeometry(QtCore.QRect(1030, 670, 541, 21))
        self.line_h_3_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_3_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_3_2.setObjectName(_fromUtf8("line_h_3_2"))
        self.textEdit_24 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_24.setGeometry(QtCore.QRect(1390, 800, 53, 19))
        self.textEdit_24.setObjectName(_fromUtf8("textEdit_24"))
        self.OKButton_2 = QtGui.QPushButton(self.centralwidget)
        self.OKButton_2.setGeometry(QtCore.QRect(1510, 40, 51, 21))
        self.OKButton_2.setObjectName(_fromUtf8("OKButton_2"))
        self.time_2 = QtGui.QLabel(self.centralwidget)
        self.time_2.setGeometry(QtCore.QRect(1210, 40, 31, 21))
        self.time_2.setObjectName(_fromUtf8("time_2"))
        self.line_h_15_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_15_2.setGeometry(QtCore.QRect(1030, 310, 541, 21))
        self.line_h_15_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_15_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_15_2.setObjectName(_fromUtf8("line_h_15_2"))
        self.elevator2_2 = QtGui.QPushButton(self.centralwidget)
        self.elevator2_2.setGeometry(QtCore.QRect(1170, 260, 21, 31))
        self.elevator2_2.setObjectName(_fromUtf8("elevator2_2"))
        self.line_h_1_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_1_2.setGeometry(QtCore.QRect(840, 730, 771, 21))
        self.line_h_1_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_1_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_1_2.setObjectName(_fromUtf8("line_h_1_2"))
        self.line_h_7_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_7_2.setGeometry(QtCore.QRect(1030, 550, 541, 21))
        self.line_h_7_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_7_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_7_2.setObjectName(_fromUtf8("line_h_7_2"))
        self.line_h_17_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_17_2.setGeometry(QtCore.QRect(1030, 250, 541, 21))
        self.line_h_17_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_17_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_17_2.setObjectName(_fromUtf8("line_h_17_2"))
        self.elevator3_2 = QtGui.QPushButton(self.centralwidget)
        self.elevator3_2.setGeometry(QtCore.QRect(1310, 290, 21, 31))
        self.elevator3_2.setObjectName(_fromUtf8("elevator3_2"))
        self.destination3_2 = QtGui.QLabel(self.centralwidget)
        self.destination3_2.setGeometry(QtCore.QRect(1320, 830, 61, 20))
        self.destination3_2.setObjectName(_fromUtf8("destination3_2"))
        self.monthText_2 = QtGui.QTextEdit(self.centralwidget)
        self.monthText_2.setGeometry(QtCore.QRect(1030, 40, 71, 21))
        self.monthText_2.setObjectName(_fromUtf8("monthText_2"))
        self.startfloor2_2 = QtGui.QLabel(self.centralwidget)
        self.startfloor2_2.setGeometry(QtCore.QRect(1180, 800, 61, 21))
        self.startfloor2_2.setObjectName(_fromUtf8("startfloor2_2"))
        self.line_v_2_2 = QtGui.QFrame(self.centralwidget)
        self.line_v_2_2.setGeometry(QtCore.QRect(1160, 140, 20, 711))
        self.line_v_2_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_v_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_v_2_2.setObjectName(_fromUtf8("line_v_2_2"))
        self.timeSliderValue12_2 = QtGui.QLabel(self.centralwidget)
        self.timeSliderValue12_2.setGeometry(QtCore.QRect(1250, 90, 31, 16))
        self.timeSliderValue12_2.setObjectName(_fromUtf8("timeSliderValue12_2"))
        self.chartLine_2 = QtGui.QFrame(self.centralwidget)
        self.chartLine_2.setGeometry(QtCore.QRect(830, 60, 20, 681))
        self.chartLine_2.setFrameShape(QtGui.QFrame.VLine)
        self.chartLine_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.chartLine_2.setObjectName(_fromUtf8("chartLine_2"))
        self.line_h_8_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_8_2.setGeometry(QtCore.QRect(1030, 520, 541, 21))
        self.line_h_8_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_8_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_8_2.setObjectName(_fromUtf8("line_h_8_2"))
        self.year_2 = QtGui.QLabel(self.centralwidget)
        self.year_2.setGeometry(QtCore.QRect(1010, 40, 16, 21))
        self.year_2.setObjectName(_fromUtf8("year_2"))
        self.waitingtime3__2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime3__2.setGeometry(QtCore.QRect(1310, 770, 71, 20))
        self.waitingtime3__2.setObjectName(_fromUtf8("waitingtime3__2"))
        self.textEdit_25 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_25.setGeometry(QtCore.QRect(1530, 800, 53, 19))
        self.textEdit_25.setObjectName(_fromUtf8("textEdit_25"))
        self.hourText_2 = QtGui.QTextEdit(self.centralwidget)
        self.hourText_2.setGeometry(QtCore.QRect(1240, 40, 71, 21))
        self.hourText_2.setObjectName(_fromUtf8("hourText_2"))
        self.Car1_2 = QtGui.QLabel(self.centralwidget)
        self.Car1_2.setGeometry(QtCore.QRect(1080, 740, 31, 16))
        self.Car1_2.setObjectName(_fromUtf8("Car1_2"))
        self.timeSlider_2 = QtGui.QSlider(self.centralwidget)
        self.timeSlider_2.setGeometry(QtCore.QRect(950, 70, 581, 22))
        self.timeSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider_2.setObjectName(_fromUtf8("timeSlider_2"))
        self.line_h_16_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_16_2.setGeometry(QtCore.QRect(1030, 280, 541, 21))
        self.line_h_16_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_16_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_16_2.setObjectName(_fromUtf8("line_h_16_2"))
        self.Car4_2 = QtGui.QLabel(self.centralwidget)
        self.Car4_2.setGeometry(QtCore.QRect(1500, 740, 31, 16))
        self.Car4_2.setObjectName(_fromUtf8("Car4_2"))
        self.line_h_12_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_12_2.setGeometry(QtCore.QRect(1030, 400, 541, 21))
        self.line_h_12_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_12_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_12_2.setObjectName(_fromUtf8("line_h_12_2"))
        self.timeSliderValue24_2 = QtGui.QLabel(self.centralwidget)
        self.timeSliderValue24_2.setGeometry(QtCore.QRect(1520, 90, 31, 16))
        self.timeSliderValue24_2.setObjectName(_fromUtf8("timeSliderValue24_2"))
        self.humanTable_2 = QtGui.QTableWidget(self.centralwidget)
        self.humanTable_2.setGeometry(QtCore.QRect(890, 140, 101, 601))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.humanTable_2.sizePolicy().hasHeightForWidth())
        self.humanTable_2.setSizePolicy(sizePolicy)
        self.humanTable_2.setAutoFillBackground(False)
        self.humanTable_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.humanTable_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.humanTable_2.setObjectName(_fromUtf8("humanTable_2"))
        self.humanTable_2.setColumnCount(1)
        self.humanTable_2.setRowCount(20)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(15, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(16, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(17, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(18, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setVerticalHeaderItem(19, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.humanTable_2.setItem(0, 0, item)
        self.humanTable_2.horizontalHeader().setVisible(False)
        self.humanTable_2.horizontalHeader().setHighlightSections(False)
        self.humanTable_2.verticalHeader().setVisible(False)
        self.humanTable_2.verticalHeader().setHighlightSections(False)
        self.waitingtimeText_2 = QtGui.QTextEdit(self.centralwidget)
        self.waitingtimeText_2.setGeometry(QtCore.QRect(1110, 770, 53, 19))
        self.waitingtimeText_2.setObjectName(_fromUtf8("waitingtimeText_2"))
        self.waitingtime4_2 = QtGui.QLabel(self.centralwidget)
        self.waitingtime4_2.setGeometry(QtCore.QRect(1450, 770, 71, 20))
        self.waitingtime4_2.setObjectName(_fromUtf8("waitingtime4_2"))
        self.textEdit_26 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_26.setGeometry(QtCore.QRect(1390, 830, 53, 19))
        self.textEdit_26.setObjectName(_fromUtf8("textEdit_26"))
        self.line_h_20_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_20_2.setGeometry(QtCore.QRect(1030, 160, 541, 21))
        self.line_h_20_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_20_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_20_2.setObjectName(_fromUtf8("line_h_20_2"))
        self.line_h_2_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_2_2.setGeometry(QtCore.QRect(1030, 700, 541, 21))
        self.line_h_2_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_2_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_2_2.setObjectName(_fromUtf8("line_h_2_2"))
        self.line_h_4_2 = QtGui.QFrame(self.centralwidget)
        self.line_h_4_2.setGeometry(QtCore.QRect(1030, 640, 541, 21))
        self.line_h_4_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_h_4_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_h_4_2.setObjectName(_fromUtf8("line_h_4_2"))

        self.hallcall_4 = QtGui.QPushButton(self.centralwidget)
        self.hallcall_4.setGeometry(QtCore.QRect(160, 690, 21, 31))
        self.hallcall_4.setObjectName(_fromUtf8("hallcall_4"))
        self.hallcall_4.setEnabled(False)

        self.hallcall_3 = QtGui.QPushButton(self.centralwidget)
        self.hallcall_3.setGeometry(QtCore.QRect(160, 690, 21, 31))
        self.hallcall_3.setObjectName(_fromUtf8("hallcall_4"))
        self.hallcall_3.setEnabled(False)

        self.secondText = QtGui.QTextEdit(self.centralwidget)
        self.secondText.setGeometry(QtCore.QRect(590, 20, 71, 21))
        self.secondText.setObjectName(_fromUtf8("secondText"))
        self.second = QtGui.QLabel(self.centralwidget)
        self.second.setGeometry(QtCore.QRect(660, 20, 16, 21))
        self.second.setObjectName(_fromUtf8("second"))
        self.second_2 = QtGui.QLabel(self.centralwidget)
        self.second_2.setGeometry(QtCore.QRect(1490, 40, 16, 21))
        self.second_2.setObjectName(_fromUtf8("second_2"))
        self.secondText_2 = QtGui.QTextEdit(self.centralwidget)
        self.secondText_2.setGeometry(QtCore.QRect(1420, 40, 71, 21))
        self.secondText_2.setObjectName(_fromUtf8("secondText_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1603, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.OKButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.abc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getUI(self):
        return ui;

    def toggle(self):





        self.elevator1.setEnabled(True)
        self.elevator2.setEnabled(True)
        self.elevator3.setEnabled(True)
        self.elevator4.setEnabled(True)



        #데이터 불러온 변수를 넣어주는 곳
        """
        self.waitingtimeText.setText("15")
        self.textEdit_9.setText("4")
        self.textEdit_12.setText("10")

        self.textEdit_7.setText("5")
        self.textEdit_11.setText("17")
        self.textEdit_14.setText("13")

        self.destinationText.setText("9")
        self.textEdit_10.setText("16")
        self.textEdit_13.setText("15")
        """

    """
    def locatedHallCall1(self, departure, destination, waiting_time, one):

        self.hallcall.setEnabled(True)

        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)
        one = int(one)

        if one > departure:
            self.hallcall.move(self.hallcall.x(),self.hallcall.y()+self.hallcall.width()*(one-departure+1)+10*(one-departure+1))
        if one < departure:
            self.hallcall.move(self.hallcall.x(),self.hallcall.y()-self.hallcall.width()*(departure-one)-10*(departure-one))
        if one == departure:
            self.hallcall.move(self.hallcall.x(),self.hallcall.y())

        #destinatoin 넣기
        self.destinationText.setText(str(destination))
        self.waitingtimeText.setText(str(waiting_time))
        self.textEdit_7.setText(str(departure))



    def locatedHallCall2(self, departure, destination, waiting_time, two):
        self.hallcall_2.setEnabled(True)

        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)
        two = int(two)


        if two > departure:
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()+self.hallcall_2.width()*(two-departure+1)+10*(two-departure+1))
        if two < departure:
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()-self.hallcall_2.width()*(departure-two)-10*(departure-two))
        if two == departure:
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y())

        #destinatoin 넣기
        self.textEdit_10.setText(str(destination))
        self.textEdit_9.setText(str(waiting_time))
        self.textEdit_11.setText(str(departure))


    def locatedHallCall3(self, departure, destination, waiting_time, three):
        self.hallcall_3.setEnabled(True)

        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)
        three = int(three)

        if three > departure:
            self.hallcall_3.move(self.hallcall_3.x(),self.hallcall_3.y()+self.hallcall_3.width()*(three-departure+1)+10*(three-departure+1))
        if three < departure:
            self.hallcall_3.move(self.hallcall_3.x(),self.hallcall_3.y()-self.hallcall_3.width()*(departure-three)-10*(departure-three))
        if three == departure:
            self.hallcall_3.move(self.hallcall_3.x(),self.hallcall_3.y())

        #destinatoin 넣기
        self.textEdit_13.setText(str(destination))
        self.textEdit_12.setText(str(waiting_time))
        self.textEdit_14.setText(str(departure))





    def locatedHallCall4(self, departure, destination, waiting_time, four):
        self.hallcall_4.setEnabled(True)


        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)
        four = int(four)

        if four > departure:
            self.hallcall_4.move(self.hallcall_4.x(), self.hallcall_4.y() + self.hallcall_4.width()*(four-departure+1)+10*(four-departure+1))
        if four < departure:
            self.hallcall_4.move(self.hallcall_4.x() , self.hallcall_4.y() - self.hallcall_4.width() * (departure-four)-10*(departure-four))
        if four == departure:
            self.hallcall_4.move(self.hallcall_4.x(),self.hallcall_4.y())

        self.textEdit_16.setText(str(destination))
        self.textEdit_15.setText(str(waiting_time))
        self.textEdit_17.setText(str(departure))
    """




    def locatedHallCall1(self, departure, destination, waiting_time):

        self.hallcall.setEnabled(True)

        global preDeparture1


        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)


        if int(preDeparture1) > int(departure):
            self.hallcall.move(self.hallcall.x(),self.hallcall.y()+self.hallcall.width()*(preDeparture1-departure+1)+10*(preDeparture1-departure+1))
        if int(preDeparture1) < int(departure):
            self.hallcall.move(self.hallcall.x(),self.hallcall.y()-self.hallcall.width()*(departure-preDeparture1)-10*(departure-preDeparture1))


        #destinatoin 넣기
        self.destinationText.setText(str(destination))
        self.waitingtimeText.setText(str(waiting_time))
        self.textEdit_7.setText(str(departure))

        preDeparture1 = departure



    def locatedHallCall2(self, departure, destination, waiting_time):
        self.hallcall_2.setEnabled(True)


        global preDeparture2

        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)


        """
        if two > departure:
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()+self.hallcall_2.width()*(two-departure+1))
        if two < departure :
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()-self.hallcall_2.width()*(departure-two))
        """
        if int(preDeparture2) > int(departure):
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()+self.hallcall_2.width()*(preDeparture2-departure+1)+10*(preDeparture2-departure+1))
        if int(preDeparture2) < int(departure):
            self.hallcall_2.move(self.hallcall_2.x(),self.hallcall_2.y()-self.hallcall_2.width()*(departure-preDeparture2)-10*(departure-preDeparture2))

        #destinatoin 넣기
        self.textEdit_10.setText(str(destination))
        self.textEdit_9.setText(str(waiting_time))
        self.textEdit_11.setText(str(departure))

        preDeparture2 = departure


    def locatedHallCall3(self, departure, destination, waiting_time):
        self.hallcall_3.setEnabled(True)

        global preDeparture3
        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)


        if int(preDeparture3) > int(departure):
            self.hallcall_3.move(self.hallcall_3.x(),self.hallcall_3.y()+self.hallcall_3.width()*(preDeparture3-departure+1)+10*(preDeparture3-departure+1))
        if int(preDeparture3) < int(departure):
            self.hallcall_3.move(self.hallcall_3.x(),self.hallcall_3.y()-self.hallcall_3.width()*(departure-preDeparture3)-10*(departure-preDeparture3))


        #destinatoin 넣기
        self.textEdit_13.setText(str(destination))
        self.textEdit_12.setText(str(waiting_time))
        self.textEdit_14.setText(str(departure))

        preDeparture3 = departure





    def locatedHallCall4(self, departure, destination, waiting_time):
        self.hallcall_4.setEnabled(True)
        global preDeparture4
        departure = int(departure)
        destination = int(destination)
        #waiting_time = int(waiting_time)

        if int(preDeparture4) > int(departure):
            self.hallcall_4.move(self.hallcall_4.x(), self.hallcall_4.y() + (self.hallcall_4.width()*(preDeparture4-departure+1))+10*(preDeparture4-departure+1))
        if int(preDeparture4) < int(departure):
            self.hallcall_4.move(self.hallcall_4.x() , self.hallcall_4.y() - (self.hallcall_4.width() * (departure-preDeparture4))-10*(departure-preDeparture4))



        self.textEdit_16.setText(str(destination))
        self.textEdit_15.setText(str(waiting_time))
        self.textEdit_17.setText(str(departure))

        preDeparture4 = departure






    def abc(self):

        data = dataParsing.generateData(ui)

        dialog.timer[0] = int(self.hourText.toPlainText())
        dialog.timer[1] = int(self.minuteText.toPlainText())
        dialog.timer[2] = int(self.secondText.toPlainText())-1

        stopwatch = StopWatch()
        stopwatch.start()

        print(data)

        self.toggle()
        t1 = ThreadEli.ElavatorThread2()
        t1.setUI(ui)
        t1.setDasom(data)
        t1.setDialog(dialog)


        t2 = ThreadEli.ElavatorThread1()
        t2.setDialog(dialog)
        t2.setUI(ui)
        t2.setDasom(data)



        t3 = ThreadEli.ElavatorThread3()
        t3.setUI(ui)
        t3.setDasom(data)
        t3.setDialog(dialog)


        t4 = ThreadEli.ElavatorThread4()
        t4.setUI(ui)
        t4.setDasom(data)
        t4.setDialog(dialog)


        t1.start()
        t2.start()
        t3.start()
        t4.start()


        #eleIdCheck.ele(data)

        # #eleThread1 = ElavatorThread1()
        #eleThread1.start()


    def up(self, eleNum):
        if eleNum == 1:
            self.elevator1.move(self.elevator1.x(),self.elevator1.y()-self.elevator1.height())
        if eleNum == 2:
            self.elevator2.move(self.elevator2.x(),self.elevator2.y()-self.elevator2.height())
        if eleNum == 3:
            self.elevator3.move(self.elevator3.x(),self.elevator3.y()-self.elevator3.height())
        if eleNum == 4:
            self.elevator4.move(self.elevator4.x(),self.elevator4.y()-self.elevator4.height())

    def down(self,eleNum):
        if eleNum == 1:
            self.elevator1.move(self.elevator1.x(),self.elevator1.y()+self.elevator1.height())
        if eleNum == 2:
            self.elevator2.move(self.elevator2.x(),self.elevator2.y()+self.elevator2.height())
        if eleNum == 3:
            self.elevator3.move(self.elevator3.x(),self.elevator3.y()+self.elevator3.height())
        if eleNum == 4:
            self.elevator4.move(self.elevator4.x(),self.elevator4.y()+self.elevator4.height())



    #def abc2(self):
        #self.elevator1.move(self.elevator1.x(),self.elevator1.y()+10)
        #self.elevator3.move(self.elevator3.x(),self.elevator3.y()+10)



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.OKButton.setText(_translate("MainWindow", "OK", None))
        item = self.humanTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "새 행", None))
        __sortingEnabled = self.humanTable.isSortingEnabled()
        self.humanTable.setSortingEnabled(False)
        self.humanTable.setSortingEnabled(__sortingEnabled)
        self.human.setText(_translate("MainWindow", "사람", None))
        self.Car1.setText(_translate("MainWindow", "Car1", None))
        self.Car2.setText(_translate("MainWindow", "Car2", None))
        self.Car3.setText(_translate("MainWindow", "Car3", None))
        self.Car4.setText(_translate("MainWindow", "Car4", None))
        self.elevator1.setText(_translate("MainWindow", "▼", None))
        self.elevator2.setText(_translate("MainWindow", "▼", None))
        self.elevator3.setText(_translate("MainWindow", "▲", None))
        self.elevator4.setText(_translate("MainWindow", "▼", None))
        self.timeSliderValue24.setText(_translate("MainWindow", "24시", None))
        self.timeSliderValue12.setText(_translate("MainWindow", "12시", None))
        self.waitingtime1.setText(_translate("MainWindow", "waiting time", None))
        self.startfloor1.setText(_translate("MainWindow", "start floor", None))
        self.destination1.setText(_translate("MainWindow", "destination", None))
        self.waitingtimeText.setText(_translate("MainWindow", "0", None))
        self.textEdit_7.setText(_translate("MainWindow", "0", None))
        self.destinationText.setText(_translate("MainWindow", "0", None))

        self.hallcall.setText(_translate("MainWindow", "H1", None))
        self.startfloor2.setText(_translate("MainWindow", "start floor", None))
        self.textEdit_9.setText(_translate("MainWindow", "0", None))
        self.destination2.setText(_translate("MainWindow", "destination", None))
        self.textEdit_10.setText(_translate("MainWindow", "0", None))
        self.waitingtime2.setText(_translate("MainWindow", "waiting time", None))
        self.textEdit_11.setText(_translate("MainWindow", "0", None))
        self.textEdit_12.setText(_translate("MainWindow", "0", None))
        self.destination3.setText(_translate("MainWindow", "destination", None))
        self.textEdit_13.setText(_translate("MainWindow", "0", None))
        self.textEdit_14.setText(_translate("MainWindow", "0", None))
        self.startfloor3.setText(_translate("MainWindow", "start floor", None))
        self.waitingtime3.setText(_translate("MainWindow", "waiting time", None))
        self.textEdit_15.setText(_translate("MainWindow", "0", None))
        self.destination4.setText(_translate("MainWindow", "destination", None))
        self.textEdit_16.setText(_translate("MainWindow", "0", None))
        self.textEdit_17.setText(_translate("MainWindow", "0", None))
        self.startfloor4.setText(_translate("MainWindow", "start floor", None))
        self.waitingtime3_2.setText(_translate("MainWindow", "waiting time", None))
        self.date.setText(_translate("MainWindow", "날짜 :", None))
        self.year.setText(_translate("MainWindow", "년", None))
        self.month.setText(_translate("MainWindow", "월", None))
        self.day.setText(_translate("MainWindow", "일", None))
        self.time.setText(_translate("MainWindow", "시간", None))
        self.minute.setText(_translate("MainWindow", "분", None))
        self.hour.setText(_translate("MainWindow", "시", None))
        self.elevator1_2.setText(_translate("MainWindow", "▼", None))
        self.waitingtime2_2.setText(_translate("MainWindow", "waiting time", None))
        self.hallcall_2.setText(_translate("MainWindow", "H2", None))
        self.hallcall_3.setText(_translate("MainWindow", "H3", None))
        self.textEdit_18.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.minute_2.setText(_translate("MainWindow", "분", None))
        self.textEdit_19.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.elevator4_2.setText(_translate("MainWindow", "▼", None))
        self.startfloor4_2.setText(_translate("MainWindow", "start floor", None))
        self.textEdit_20.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.hour_2.setText(_translate("MainWindow", "시", None))
        self.destination1_2.setText(_translate("MainWindow", "destination", None))
        self.startfloor3_2.setText(_translate("MainWindow", "start floor", None))
        self.destinationText_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.destination2_2.setText(_translate("MainWindow", "destination", None))
        self.textEdit_21.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.Car3_2.setText(_translate("MainWindow", "Car3", None))
        self.destination4_2.setText(_translate("MainWindow", "destination", None))
        self.textEdit_22.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.textEdit_23.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.waitingtime1_2.setText(_translate("MainWindow", "waiting time", None))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.startfloor1_2.setText(_translate("MainWindow", "start floor", None))
        self.month_2.setText(_translate("MainWindow", "월", None))
        self.Car2_2.setText(_translate("MainWindow", "Car2", None))
        self.day_2.setText(_translate("MainWindow", "일", None))
        self.date_2.setText(_translate("MainWindow", "날짜 :", None))
        self.human_2.setText(_translate("MainWindow", "사람", None))
        self.textEdit_24.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.OKButton_2.setText(_translate("MainWindow", "OK", None))
        self.time_2.setText(_translate("MainWindow", "시간", None))
        self.elevator2_2.setText(_translate("MainWindow", "▼", None))
        self.elevator3_2.setText(_translate("MainWindow", "▲", None))
        self.destination3_2.setText(_translate("MainWindow", "destination", None))
        self.startfloor2_2.setText(_translate("MainWindow", "start floor", None))
        self.timeSliderValue12_2.setText(_translate("MainWindow", "12시", None))
        self.year_2.setText(_translate("MainWindow", "년", None))
        self.waitingtime3__2.setText(_translate("MainWindow", "waiting time", None))
        self.textEdit_25.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.Car1_2.setText(_translate("MainWindow", "Car1", None))
        self.Car4_2.setText(_translate("MainWindow", "Car4", None))
        self.timeSliderValue24_2.setText(_translate("MainWindow", "24시", None))
        item = self.humanTable_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "새 열", None))
        item = self.humanTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "새 행", None))
        __sortingEnabled = self.humanTable_2.isSortingEnabled()
        self.humanTable_2.setSortingEnabled(False)
        self.humanTable_2.setSortingEnabled(__sortingEnabled)
        self.waitingtimeText_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))
        self.waitingtime4_2.setText(_translate("MainWindow", "waiting time", None))
        self.textEdit_26.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1</p></body></html>", None))

        self.hallcall_4.setText(_translate("MainWindow", "H4", None))
        self.second.setText(_translate("MainWindow", "초", None))
        self.second_2.setText(_translate("MainWindow", "초", None))


"""
class GUIThread(QtCore.QThread):
    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)
        self.value = 0
        self.alive = 1
        self.running = 0


    def run(self):
        while self.alive:
            while self.running:
                try :
                    #print 'exit'
                    #ui.abc2()

                    #startj(0,0)

                    time.sleep(1)


                except :
                    print 'exit from Joy mode'
"""






class StopWatch(threading.Thread):
    def __init__(self, parent = None):
        threading.Thread.__init__(self)



    def run(self):
        while(1):
            dialog.update_timeText()

            time.sleep(1)








class Ui_Dialog(object):
    pattern = '{0:02d} : {1:02d} : {2:02d}'

    timer = [0, 0, 0]
    state = True
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 361, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pause)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "00 : 00 : 00", None))


    def update_timeText(self):

        if(self.state):


            # Every time this function is called,
            # we will increment 1 centisecond (1/100 of a second)
            self.timer[2] += 1

            # Every 100 centisecond is equal to 1 second
            if (self.timer[2] >= 60):
                self.timer[2] = 0
                self.timer[1] += 1
            # Every 60 seconds is equal to 1 min
            if (self.timer[1] >= 60):
                self.timer[0] += 1
                self.timer[1] = 0
            # We create our time string here
            timeString = self.pattern.format(self.timer[0], self.timer[1], self.timer[2])
            # Update the timeText Label box with the current time
            #self.label.configure(text=timeString)
            self.label.setText(timeString)
            # Call the update_timeText() function after 1 centisecond



    # To start the kitchen timer
    def start(self):
        self.state = True

    # To pause the kitchen timer
    def pause(self):

        self.state = False





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()

    Dialog = QtGui.QDialog()
    dialog = Ui_Dialog()
    dialog.setupUi(Dialog)
    Dialog.show()


    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


