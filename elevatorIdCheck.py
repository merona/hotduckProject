#-*- coding:cp949 -*-


import dataParsing as data
import elevatorMove as move


##############################
# (전역변수) 1,2,3,4호기 대기층
global one
global two
global three
global four
one = 1
two = 1
three = 1
four = 1
##############################
#전체 튜플 수
print data.tupleNum
##############################
#다솜이가 보내준 데이터 번째
#이거 이후부터 검색
#dasom = 3
##############################
#튜플99개 : 배열로 따지면 [0~98]
#다솜 3을 보내줌 - 사실상 엑셀에서 4번째
#엑셀로 따지면 4번째 99번째
#배열로 따지면 [3~98] : (98-3+1) 번의 for문
# 99-다솜이가 보내준거
#for문 돌리는 횟수

##############################


def ele(dasom):

    forNum = int(data.tupleNum)-int(dasom)

    for i in range(0,forNum):
        #승강기 호수
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