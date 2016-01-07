# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-


import threading


from numpy import genfromtxt


import datetime


#Open csv file and read in data
#csvFile = "filename.csv"
csvFile = "bulding-seoul-mytest.csv"
my_data = genfromtxt(csvFile, delimiter=';', skip_header=1)
#skip_header : int, optional-The number of lines to skip at the beginning of the file.
# my_data.shape[0] = 99(행수)
#repr : 숫자를 문자열로
tupleNum = my_data.shape[0] # Number of data samples
print tupleNum #99

############################






with open('bulding-seoul-mytest.csv', 'rb') as csvfile:

    #속성 배열
    attrArr = []

    #registertime
    #departurefloor
    #destinationfloor
    #el_idatfield
    #waitingtime
    #ridingtime
    #servicetime
    #registertime_year
    #registertime_quarter
    #registertime_month
    #registertime_day
    #registertime_hour
    #registertime_dayofweek
    #iserroroccured
    #isup
    #registertime_30min
    #registertime_15min
    #registertime_5min


    attrRow = csvfile.readline().replace('"','').split(';')
    for attr in attrRow:
        print attr
        attrArr.append(attr)
        #attrRow[0~17]

    ###########################################
    #속성 배열 만들기 끝
    ###########################################






    #data 배열
    dataSet = [[0 for col in range(len(attrArr))] for row in range(tupleNum)]


    #tuple길이 배열
    for i in range(0,tupleNum):
        nowRow = csvfile.readline().replace('"','').split(';')

        #속성크기만큼 for
        for j in range(0,len(attrArr)):
            dataSet[i][j] = nowRow[j]






def generateData(ui):

    da = 0

    #tuple길이 배열
    for i in range(0,tupleNum):
        # milisecond 버리기
        dateSplit = dataSet[i][0].split('.')
        print dateSplit[0]

        registertime = datetime.datetime.strptime(dateSplit[0], "%Y-%m-%d %H:%M:%S")

        if registertime.year == int(ui.yearText.toPlainText()) and registertime.month == int(ui.monthText.toPlainText()) and registertime.day == int(ui.dayText.toPlainText()) and registertime.hour == int(ui.hourText.toPlainText()) and registertime.minute == int(ui.minuteText.toPlainText()) and registertime.second == int(ui.secondText.toPlainText()):
            da = i

    return da





"""
class DataThread(threading.Thread):
    def __init__(self, parent = None):
        threading.Thread.__init__(self)



    def run(self):
        generateData()








datathread = DataThread()
datathread.start()

"""





