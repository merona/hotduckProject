# -*- coding: utf-8 -*-
import threading
import dataParsing as data
import elevatorMove as move
import simulator
import time



class ElavatorThread1(threading.Thread):

    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()

    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom


    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self,uiDialog):
        self.dialog = uiDialog


    def run(self):
        while(1):
            ######
            ## 스탑워치시간이 변하면.. 데이터를 하나 읽는다. 만약에 호수 가 맞고 시간이 맞으면 움직인다.
            ## 스탑워치 시간을 가져온다 레지스터타임과 엘베번호를 비교

            # (엘베번호, 시간)
            # (o,o) - 일 시키고 dasom +=1
            # (o,x) - dasom 그대로
            # (x,o) - dasom +=1
            # (x,x) - dasom +=1

            #승강기 호수
            elID = data.dataSet[self.dasom][3]

            # 시간 잘라내기
            #print dataSet[0][0] #2015-09-10 18:57:55.5
            # milisecond 버리기
            dateSplit = data.dataSet[self.dasom][0].split('.')
            registertime = data.datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")






            if elID == "1":

                #승강기 번호가 맞는데 시간이 맞으면

                if self.dialog.timer[2] == registertime.second:
                    if self.dialog.timer[1] == registertime.minute:
                        if self.dialog.timer[0] == registertime.hour:
                            #일을 시킨다
                            print "ele1_start"
                            #홀콜위치랑
                            move.first_ele(self.dasom,self.ui)
                            self.dasom += 1

                #승강기 번호가 맞는데 시간이 아직이면
                #else: dasom 그대로

            else :
                self.dasom +=1








class ElavatorThread2(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()
    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog

    def run(self):
        while(1):
            ######
            ## 스탑워치시간이 변하면.. 데이터를 하나 읽는다. 만약에 호수 가 맞고 시간이 맞으면 움직인다.
            ## 스탑워치 시간을 가져온다 레지스터타임과 엘베번호를 비교

            # (엘베번호, 시간)
            # (o,o) - 일 시키고 dasom +=1
            # (o,x) - dasom 그대로
            # (x,o) - dasom +=1
            # (x,x) - dasom +=1

            #승강기 호수
            elID = data.dataSet[self.dasom][3]

            # 시간 잘라내기
            #print dataSet[0][0] #2015-09-10 18:57:55.5
            # milisecond 버리기
            dateSplit = data.dataSet[self.dasom][0].split('.')
            registertime = data.datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")






            if elID == "2":

                #승강기 번호가 맞는데 시간이 맞으면

                if self.dialog.timer[2] == registertime.second:
                    if self.dialog.timer[1] == registertime.minute:
                        if self.dialog.timer[0] == registertime.hour:
                            #일을 시킨다
                            print "ele2_start"
                            move.second_ele(self.dasom,self.ui)
                            self.dasom += 1
                #승강기 번호가 맞는데 시간이 아직이면
                #else: dasom 그대로

            else :
                self.dasom +=1


class ElavatorThread3(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()

    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog

    def run(self):
        while(1):
            ######
            ## 스탑워치시간이 변하면.. 데이터를 하나 읽는다. 만약에 호수 가 맞고 시간이 맞으면 움직인다.
            ## 스탑워치 시간을 가져온다 레지스터타임과 엘베번호를 비교

            # (엘베번호, 시간)
            # (o,o) - 일 시키고 dasom +=1
            # (o,x) - dasom 그대로
            # (x,o) - dasom +=1
            # (x,x) - dasom +=1

            #승강기 호수
            elID = data.dataSet[self.dasom][3]

            # 시간 잘라내기
            #print dataSet[0][0] #2015-09-10 18:57:55.5
            # milisecond 버리기
            dateSplit = data.dataSet[self.dasom][0].split('.')
            registertime = data.datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")






            if elID == "3":

                #승강기 번호가 맞는데 시간이 맞으면

                if self.dialog.timer[2] == registertime.second:
                    if self.dialog.timer[1] == registertime.minute:
                        if self.dialog.timer[0] == registertime.hour:
                            #일을 시킨다
                            print "ele3_start"
                            move.third_ele(self.dasom,self.ui)
                            self.dasom += 1
                #승강기 번호가 맞는데 시간이 아직이면
                #else: dasom 그대로

            else :
                self.dasom +=1




class ElavatorThread4(threading.Thread):
    dasom = 23
    ui = simulator.Ui_MainWindow()
    dialog = simulator.Ui_Dialog()
    def __init__(self, parent = None):
        threading.Thread.__init__(self)

    def setDasom(self, uidasom):
        self.dasom =uidasom

    def getDasom(self):
        return self.dasom

    def setUI(self, uiUI):
        self.ui =uiUI

    def getUI(self):
        return self.ui

    def setDialog(self, uidialog):
        self.dialog = uidialog

    def run(self):
        while(1):
            ######
            ## 스탑워치시간이 변하면.. 데이터를 하나 읽는다. 만약에 호수 가 맞고 시간이 맞으면 움직인다.
            ## 스탑워치 시간을 가져온다 레지스터타임과 엘베번호를 비교

            # (엘베번호, 시간)
            # (o,o) - 일 시키고 dasom +=1
            # (o,x) - dasom 그대로
            # (x,o) - dasom +=1
            # (x,x) - dasom +=1

            #승강기 호수
            elID = data.dataSet[self.dasom][3]

            # 시간 잘라내기
            #print dataSet[0][0] #2015-09-10 18:57:55.5
            # milisecond 버리기
            dateSplit = data.dataSet[self.dasom][0].split('.')
            registertime = data.datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")






            if elID == "4":

                #승강기 번호가 맞는데 시간이 맞으면

                if self.dialog.timer[2] == registertime.second:
                    if self.dialog.timer[1] == registertime.minute:
                        if self.dialog.timer[0] == registertime.hour:
                            #일을 시킨다
                            print "ele4_start"
                            move.fourth_ele(self.dasom,self.ui)
                            self.dasom += 1
                #승강기 번호가 맞는데 시간이 아직이면
                #else: dasom 그대로

            else :
                self.dasom +=1



