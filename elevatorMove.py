# -*- coding:cp949 -*-
# -*- coding: utf-8 -*-

import dataParsing as data
import time

# 1.  ��� ���������Ϳ��� ��� �������� �̵�
# (��������) 1,2,3,4ȣ�� �����
one = 1
two = 1
three = 1
four = 1

def first_ele(row,ui):

    #1. ��������� �̵���Ű��

    print "one -> departure"

    global one
    departure = int(data.dataSet[row][1])  # departure
    destination = data.dataSet[row][2]  # destination
    waiting_time_split= data.dataSet[row][4] #waitingtime �߶�ߵ�

    waiting_time_split2 = waiting_time_split.split(':') #�ڸ�
    waiting_time = waiting_time_split2[2]   #waitingtime
    move_times = abs(int(one)-int(departure)) #  ������ Ƚ�� : �ݿø�

    #print("_____waiting time____")
    #print(waiting_time)
    sleeptime = float(waiting_time)/float(move_times) # sleep time

    #print("_____sleeptime____")
    #print(sleeptime)

    ui.locatedHallCall1(departure, destination, waiting_time)

    for i in range(0, move_times):
        if int(departure) > int(one):
            print "up"
            ui.up(1)
            time.sleep(round(sleeptime))
        elif int(departure) < int(one):
            print("down")
            ui.down(1)
            time.sleep(round(sleeptime))



    print "departure -> desti"

    #2. ���� ��������� ����������
    # departure -> destination
    #    ridingtime = 00:00:42.8

    dataSplit1 = data.dataSet[row][5].split(':')
    ridingtime = dataSplit1[2]

    move_times = abs(int(destination)-int(departure))
    sleeptime = float(ridingtime)/float(move_times)

    for i in range(0,move_times):

        if int(departure)>int(destination):
            print "down"
            ui.down(1)
            time.sleep(round(sleeptime))

        elif int(departure) < int(destination):
            print "up"
            ui.up(1)
            time.sleep(round(sleeptime))





    #3.
    one = destination


def second_ele(row,ui):

    #1. ��������� �̵���Ű��

    print "two -> departure"

    global two
    departure = int(data.dataSet[row][1])  # departure
    destination = data.dataSet[row][2]  # destination
    waiting_time_split= data.dataSet[row][4] #waitingtime �߶�ߵ�

    waiting_time_split2 = waiting_time_split.split(':') #�ڸ�
    waiting_time = waiting_time_split2[2]   #waitingtime
    move_times = abs(int(two)-int(departure)) #  ������ Ƚ�� : �ݿø�

    #print("_____waiting time____")
    #print(waiting_time)
    sleeptime = float(waiting_time)/float(move_times) # sleep time

    #print("_____sleeptime____")
    #print(sleeptime)

    ui.locatedHallCall2(departure, destination, waiting_time)

    for i in range(0, move_times):
        if int(departure) > int(two):
            print "up"
            ui.up(2)
            time.sleep(round(sleeptime))
        elif int(departure) < int(two):
            print("down")
            ui.down(2)
            time.sleep(round(sleeptime))



    print "departure -> desti"

    #2. ���� ��������� ����������
    # departure -> destination
    #    ridingtime = 00:00:42.8

    dataSplit1 = data.dataSet[row][5].split(':')
    ridingtime = dataSplit1[2]

    move_times = abs(int(destination)-int(departure))
    sleeptime = float(ridingtime)/float(move_times)

    for i in range(0,move_times):

        if int(departure)>int(destination):
            print "down"
            ui.down(2)
            time.sleep(round(sleeptime))

        elif int(departure) < int(destination):
            print "up"
            ui.up(2)
            time.sleep(round(sleeptime))





    #3.
    two = destination



def third_ele(row,ui):



    #1. ��������� �̵���Ű��

    print "three -> departure"

    global three
    departure = int(data.dataSet[row][1])  # departure
    destination = data.dataSet[row][2]  # destination
    waiting_time_split= data.dataSet[row][4] #waitingtime �߶�ߵ�

    waiting_time_split2 = waiting_time_split.split(':') #�ڸ�
    waiting_time = waiting_time_split2[2]   #waitingtime
    move_times = abs(int(three)-int(departure)) #  ������ Ƚ�� : �ݿø�

    #print("_____waiting time____")
    #print(waiting_time)
    sleeptime = float(waiting_time)/float(move_times) # sleep time

    #print("_____sleeptime____")
    #print(sleeptime)

    ui.locatedHallCall3(departure, destination, waiting_time)

    for i in range(0, move_times):
        if int(departure) > int(three):
            print "up"
            ui.up(3)
            time.sleep(round(sleeptime))
        elif int(departure) < int(three):
            print("down")
            ui.down(3)
            time.sleep(round(sleeptime))



    print "departure -> desti"

    #2. ���� ��������� ����������
    # departure -> destination
    #    ridingtime = 00:00:42.8

    dataSplit1 = data.dataSet[row][5].split(':')
    ridingtime = dataSplit1[2]

    move_times = abs(int(destination)-int(departure))
    sleeptime = float(ridingtime)/float(move_times)

    for i in range(0,move_times):

        if int(departure)>int(destination):
            print "down"
            ui.down(3)
            time.sleep(round(sleeptime))

        elif int(departure) < int(destination):
            print "up"
            ui.up(3)
            time.sleep(round(sleeptime))





    #3.
    three = destination
    print "three global~~~~~~~~~~~~~~~~~", three



def fourth_ele(row,ui):

    #1. ��������� �̵���Ű��

    print "four -> departure"

    global four
    departure = int(data.dataSet[row][1])  # departure
    destination = data.dataSet[row][2]  # destination
    waiting_time_split= data.dataSet[row][4] #waitingtime �߶�ߵ�

    waiting_time_split2 = waiting_time_split.split(':') #�ڸ�
    waiting_time = waiting_time_split2[2]   #waitingtime
    move_times = abs(int(four)-int(departure)) #  ������ Ƚ�� : �ݿø�

    #print("_____waiting time____")
    #print(waiting_time)
    sleeptime = float(waiting_time)/float(move_times) # sleep time

    #print("_____sleeptime____")
    #print(sleeptime)
    ui.locatedHallCall4(departure, destination, waiting_time)

    for i in range(0, move_times):
        if int(departure) > int(four):
            print "up"
            ui.up(4)
            time.sleep(round(sleeptime))
        elif int(departure) < int(four):
            print("down")
            ui.down(4)
            time.sleep(round(sleeptime))



    print "departure -> desti"

    #2. ���� ��������� ����������
    # departure -> destination
    #    ridingtime = 00:00:42.8

    dataSplit1 = data.dataSet[row][5].split(':')
    ridingtime = dataSplit1[2]

    move_times = abs(int(destination)-int(departure))
    sleeptime = float(ridingtime)/float(move_times)

    for i in range(0,move_times):

        if int(departure) > int(destination):
            print "down"
            ui.down(4)
            time.sleep(round(sleeptime))
        elif int(departure) < int(destination):
            print "up"
            ui.up(4)
            time.sleep(round(sleeptime))




    #3.
    four = destination