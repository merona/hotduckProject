#-*- coding:cp949 -*-


import dataParsing as data
import elevatorMove as move


##############################
# (��������) 1,2,3,4ȣ�� �����
global one
global two
global three
global four
one = 1
two = 1
three = 1
four = 1
##############################
#��ü Ʃ�� ��
print data.tupleNum
##############################
#�ټ��̰� ������ ������ ��°
#�̰� ���ĺ��� �˻�
#dasom = 3
##############################
#Ʃ��99�� : �迭�� ������ [0~98]
#�ټ� 3�� ������ - ��ǻ� �������� 4��°
#������ ������ 4��° 99��°
#�迭�� ������ [3~98] : (98-3+1) ���� for��
# 99-�ټ��̰� �����ذ�
#for�� ������ Ƚ��

##############################


def ele(dasom):

    forNum = int(data.tupleNum)-int(dasom)

    for i in range(0,forNum):
        #�°��� ȣ��
        elID = data.dataSet[i+dasom][3]
        #print elID

        if elID=="1":
            move.first_ele(i+dasom)
            print "1elve"
        elif elID=="2":
            move.second_ele(i+dasom)
            print "2elve"
        elif elID=="3":
            print "3elve"
        elif elID=="4":
            print "4elve"