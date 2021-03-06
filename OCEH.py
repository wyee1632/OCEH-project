############################################################ 설명 ############################################################ 

#학생의 수업 입장을 도와주는 프로그램입니다.
#자세한 내용은 readme.txt 참고
#github : https://github.com/wyee1632/OCEH-project/tree/master

############################################################ 모듈 import ############################################################ 

from re import M, S
import webbrowser
from time import sleep
import time
import os
from datetime import datetime
import schedule
import ctypes

############################################################ 실행, 종료 ############################################################ 

# 프로그램 시작
def ProgramStart():
    print("--------------------------------")
    print("OCEH 프로그램이 실행되었습니다.")
    print("이 서비스를 실행하기 위해 인터넷이 설치되어 있어야만 합니다.")
    print('또한 이 프로그램은 학습을 "도와주는" 역할입니다. ')
    print("용도 외의 목적으로 사용하지 말아주세요.")
    print("긍정은 y, 부정은 n을 입력해 주시기 바랍니다.")
    print("OCEH 서비스를 실행하시겠습니까? (y/n)")
    print("--------------------------------")
    ServiceStart = input(">")
    if ServiceStart == "y" or ServiceStart == "Y":
        os.system('cls')
        Baduse()
    elif ServiceStart == "n" or ServiceStart == "N":
        print("프로그램을 3초 후에 종료합니다")
        sleep(3)
        quit()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(1)
        os.system('cls')
        ProgramStart()

#프로그램 종료
def CloseProgram():
    print("----------------------------------------")
    print("OCEH 프로그램이 종료되었습니다.")
    print("OCEH 프로그램을 이용해 주셔서 감사합니다.")
    print("오늘 하루도 수고하셨습니다.")
    print("<이 창은 5초 후에 자동으로 닫힙니다.")
    print("----------------------------------------")
    sleep(5)
    exit()

#에러메시지
def error():
    print("예기치 못한 오류!")
    print("프로그램 실행중 예기치 못한 오류가 발생하였습니다.")
    print("실행 도중 입력값을 잘못 입력하였거나, 프로그램 자체의 문제가 있을수도 있습니다.")
    print("프로그램을 다시 실행해 주십시오.")
    print("이런 문제가 계속된다면 'wyee3546@gmail.com' 으로 문의해주시기 바랍니다")
    print("이 창은 10초 후에 닫힙니다")
    sleep(10)
    exit()

############################################################ 사용 안내 ############################################################ 

#프로그램 사용 확인
def Baduse():
    global baduse
    print("<악의적 사용이란?>")
    print("1 : 프로그램을 이용해 수업에 참여하지 않고 다른 활동을 함")
    print("2 : 이 외의 프로그램의 제작 취지 (학습) 외로 사용하는 기타 모든 행위")
    print("--------------------------------------------------------------------")
    baduse = input("프로그램을 악의적으로 사용하지 않을것에 동의합니까? :  ")
    if baduse == "y" or baduse == "Y":
        print("악의적 사용 방지 동의 | ", baduse)
        sleep(1)
        os.system('cls')
        errormsg()
    elif baduse == "n" or baduse == "N":
        print("악의적 사용 방지 동의 | ", baduse)
        sleep(1)
        print("<<악의적 사용 방지 규칙을 비동의하셨습니다. 프로그램이 3초후 종료됩니다.")
        sleep(3)
        os.system('cls')
        CloseProgram()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(2)
        os.system('cls')
        Baduse()

def errormsg():
    print("만약 프로그램 실행 도중 '예기치 못한 오류!' 화면이 나오거나")
    print("프로그램이 아무 이유 없이 종료되는 현상이 발생하면, 프로그램을 다시 실행하여 주시기 바랍니다.")
    print("만약 이 현상이 자주 발생한다면 'wyee3546@gmail.com'으로 문의해주시기 바랍나다.")
    errormsgok = input(">")
    if errormsgok == "y" or errormsgok == "Y":
        sleep(1)
        os.system('cls')
        Myprogram()
    elif baduse == "n" or baduse == "N":
        sleep(1)
        print("위 메시지를 읽어주시기 바랍니다.")
        sleep(3)
        os.system('cls')
        errormsg()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(2)
        os.system('cls')
        errormsg()

#사용규약 확인
def Myprogram():
    global myprogram
    print("--------------------------------------------------------------------")
    print("<사용규약>")
    print("본 프로그램은 GNU General Public License version 3.0 (GPLv3) 라이선스를 따릅니다.")
    print("본 라이선스의 내용을 대략적으로 나열합니다")
    print("이 프로그램을 어떠한 목적이로든지 사용할 수 있습니다")
    print("소스코드를 임의로 변경할 수 있습니다.")
    print("이 라이선스 프로그램을 판매/배포시 소스코드도 요청시 함께 제공하여야 합니다.")
    print("변경된 프로그램 역시 위와 같게 소스코드 제공 의무가 있습니다.")
    print("변경된 프로그램 역시 똑같은 라이선스가 적용됩니다")
    print("또한 이 프로그램의 제작자는 이 프로그램의 보증, 책임 의무로부터 자유롭습니다.")
    print("--------------------------------------------------------------------")
    myprogram = input("이 프로그램의 사용규약 및 프로그램 정보 를 읽었으며 이에 동의하십니까? :  ")
    if myprogram == "y" or myprogram == "Y":
        print("사용규약 동의 | ", myprogram)
        os.system('cls')
        HowManyClassToday()
    elif myprogram == "n" or myprogram == "N":
        print("사용규약 동의 | ", myprogram)
        print("'사용규약'에 비동의하셨습니다. 프로그램을 이용하시려면 사용규약을 동의해 주세요.")
        print("3초뒤에 프로그램이 종료됩니다.")
        sleep(3)
        os.system('cls')
        CloseProgram()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(2)
        os.system('cls')
        Myprogram()

############################################################ 수업 일정 확인 ############################################################ 

#교시수 확인
def HowManyClassToday():
    global classcount
    classcount = input("오늘의 교시수를 입력해주십시오.(예: 7) :  ")
    if classcount == "1" or classcount == "2" or classcount == "3" or classcount == "4" \
        or classcount == "5" or classcount == "6" or classcount == "7":
        HowManyClassToday2()
    else: 
        print("1~7 사이의 정수를 입력해 주십시오.")
        sleep(2)
        os.system('cls')
        HowManyClassToday()

#이미 들은 수업 확인
def HowManyClassToday2():
    global classcount2
    print("")
    print("이미 들은 교시수를 입력해주십시오.")
    print("예) 3교시 수업을 이미 들었고 다음 수업이 4교시 라면 '3' (아직 오늘 수업이 시작하지 않았다면 0)")
    classcount2 = int(input(">"))
    if classcount2 == 0 or classcount2 == 1 or classcount2 == 2 or classcount2 == 3 or classcount2 == 4 \
        or classcount2 == 5 or classcount2 == 6 or classcount2 == 7:
        Check1()
    else: 
        print("1~7 사이의 정수를 입력해 주십시오.")
        sleep(2)
        os.system('cls')
        HowManyClassToday2()

############################################################ 기타 옵션 ############################################################ 

#입력값 재확인
def Check1():
    print("아래의 값이 맞는지 확인해주십시오.")
    print("-------------------------------")
    sleep(0.5)
    print("악의적 사용 방지        | ", baduse)
    sleep(0.5)
    print("프로그램 사용 규약      | ", myprogram)
    sleep(0.5)
    print("교시수                  | ", classcount)
    sleep(0.5)
    print("들은교시수              | ", classcount2)
    print("-------------------------------")
    print("위 값이 맞다면 y를 맞지 않다면 n 을 눌러 다시 설정해주십시오.")
    check1 = input(">")
    if check1 == "y" or check1 =="Y":
        os.system('cls')
        SCD()
    elif check1 == "n" or check1 =="N":
        print("설정을 다시 시작합니다.")
        sleep(1)
        os.system('cls')
        Baduse()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(1)
        os.system('cls')
        Check1()

#시간표 조정(설정)
def SCD():
    print("이 프로그램은 표준적인 시간표로 운영됩니다.")
    print("만약 여러분의 시간표가 아래와 다르다면, 아래의 옵션들을 이용해 보정해주십시오.")
    print("---------------------------------------------------------------------------")
    print("아침조회 | 9:00")
    print("1교시    | 9:15")
    print("2교시    | 10:10")
    print("3교시    | 11:05")
    print("4교시    | 12:00")
    print("점심시간 | 12:00 ~ 13:35")
    print("5교시    | 13:35 ~ 14:20")
    print("6교시    | 14:30 ~ 15:15")
    print("7교시    | 15:25 ~ 16:10")
    print("---------------------------------------------------------------------------")
    print("위는 통상적인 학교의 시간표입니다, 만약 여러분의 시긴표가 위와 다르다면 오차가 있을 수 있습니다. 시간표를 확인하셨습니까?")
    print("만약 점심시간이 5분 더 길다면 u 또는 U 를 입력해주세요.")
    NextSetting = input(">")
    if NextSetting == "y" or NextSetting == "Y":
        print("시간표를 확인하셨습니다.")
        os.system('cls')
        Msgbox()
    elif NextSetting == "n" or NextSetting == "N":
        print("시간표를 확인해 주세요.")
        os.system('cls')
        SCD()
    elif NextSetting == "u" or NextSetting == "U":
        print("시간표를 확인하였습니다")
        global Un 
        Un = 1
        os.system('cls')
        Msgbox()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(2)
        os.system('cls')
        SCD()

#메시지 박스 설정
def Msgbox():
    print("-----------------------------------------------------------")
    print("컨텐츠 또는 미정 시간에 띄울 알림을 설정합니다.")
    print("< 옵션 >")
    print("1. 컨텐츠 알림 (o), 미정 알림 (o) <권장>")
    print("2. 컨텐츠 알림 (x), 미정 알림 (o) <권장>")
    print("3. 컨텐츠 알림 (o), 미정 알림 (X) <권장하지 않음>")
    print("4. 알림을 띄우지 않음 <권장하지 않음>")
    print("-----------------------------------------------------------")
    global msgbox
    msgbox = input(">")
    if msgbox == "1" or msgbox =="2" or msgbox =="3" or msgbox =="4":
        os.system('cls')
        ClassSetInfo()
    else:
        print("1~4 의 정수로 대답해 주십시오.")
        sleep(1)
        os.system('cls')
        Msgbox()

#수업 설정방법 설명
def ClassSetInfo():
    print("----------------------------------------------------------")
    print("이 다음 과정에 나올 수업 설정의 예시를 설명합니다.")
    print("만약 잘못된 정보를 입력하실 경우에 프로그램이 오작동할 수 있습니다.")
    print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
    print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
    print("예시 : 수학 1 www.~~~~.com")
    print("예시2(컨텐츠, 미정) : 수학 2(3) x")
    print("----------------------------------------------------------")
    NextSetting = input(">")
    if NextSetting == "y" or NextSetting == "Y":
        os.system('cls')
        ClassSet()
    elif NextSetting == "n" or NextSetting == "N":
        print("위 내용을 정독해 주시기 바랍니다")
        sleep(2)
        ClassSetInfo()
    else:
        print("y 또는 n 으로 대답해주십시오.")
        sleep(1)
        os.system('cls')
        ClassSetInfo()

############################################################ 교시수 설정 ############################################################ 

#수업설정
def ClassSet():
    global fullclass
    if classcount == "7":
        fullclass = "1234567"
    elif classcount == "6":
        fullclass = "123456"
    elif classcount == "5":
        fullclass = "12345"
    elif classcount == "4":
        fullclass = "1234"
    elif classcount == "3":
        fullclass = "123"
    elif classcount == "2":
        fullclass = "12"
    elif classcount == "1":
        fullclass = "1"
    ClassOP1()

############################################################ 수업 정보 받기 ############################################################ 

#1교시
def ClassOP1():
    global cls1, a1, b1, c1
    if "1" in fullclass:
        if classcount2 >= 1:
            ClassOP2()
        try:
            cls1 = 1
            print("-----------------------------------------------")
            print("1교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a1, b1, c1 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b1 != 1 and b1 != 2 and b1 != 3:
            #     print("실시간 수업 여부는 정확히 입력해 주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP1()
            ClassOP2()
        except ValueError:
            print("잘못된 값이 입력되었습니다. 다시 입력해주세요")
            sleep(2)
            os.system('cls')
            ClassOP1()
    else:
        cls1 = 2
        os.system('cls')
        CloseProgram()

#2교시
def ClassOP2():
    global cls2, a2, b2, c2
    if "2" in fullclass:
        if classcount2 >= 2:
            ClassOP3()
        try:
            cls2 = 1
            print("-----------------------------------------------")
            print("2교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a2, b2, c2 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b2 != 1 and b2 != 2 and b2 != 3:
            #     print("실시간 수업 여부는 정확히 입력해 주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP2()
            ClassOP3()
        except ValueError:
            print("잘못된 값이 입력되었습니다. 다시 입력해주세요")
            sleep(2)
            os.system('cls')
            ClassOP2()
    else:
        cls2 = 2
        os.system('cls')
        setting()

#3교시
def ClassOP3():
    global cls3, a3, b3, c3
    if "3" in fullclass:
        if classcount2 >= 3:
            ClassOP4()
        try:
            cls3 = 1
            print("-----------------------------------------------")
            print("3교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a3, b3, c3 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b3 != 1 and b3 != 2 and b3 != 3:
            #     print("실시간 수업 여부는 정확히 입력해 주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP3()
            ClassOP4()
        except ValueError:
            print("잘못된 값이 입력되었습니다. 다시 입력해주세요")
            sleep(2)
            os.system('cls')
            ClassOP3()
    else:
        cls3 = 2
        os.system('cls')
        setting()

#4교시
def ClassOP4():
    if "4" in fullclass:
        if classcount2 >= 4:
            ClassOP5()
        global cls4, a4, b4, c4
        try:
            cls4 = 1
            print("-----------------------------------------------")
            print("4교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a4, b4, c4 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b4 != 1 and b4 != 2 and b4 != 3:
            #     print("실시간 수업 여부는 정확히 입력해주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP4()
            ClassOP5()
        except ValueError:
            print("잘못된 값이 입력되었습니다 다시 입력해주세요.")
            sleep(2)
            os.system('cls')
            ClassOP4()
    else:
        cls4 = 2
        os.system('cls')
        setting()

#5교시
def ClassOP5():
    global cls5, a5, b5, c5
    if "5" in fullclass:
        if classcount2 >= 5:
            ClassOP6()
        try:
            cls5 = 1
            print("-----------------------------------------------")
            print("5교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a5, b5, c5 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b5 != 1 and b5 != 2 and b5 != 3:
            #     print("실시간 수업 여부는 정확히 입력해주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP5()
            ClassOP6()
        except ValueError:
            print("잘못된 값이 입력되었습니다 다시 입력해주세요.")
            sleep(2)
            os.system('cls')
            ClassOP5()
    else:
        cls5 = 2
        os.system('cls')
        setting()

#6교시
def ClassOP6():
    global cls6, a6, b6, c6
    if "6" in fullclass:
        if classcount2 >= 6:
            ClassOP7()
        try:
            cls6 = 1
            print("-----------------------------------------------")
            print("6교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a6, b6, c6 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b6 != 1 and b6 != 2 and b6 != 3:
            #     print("실시간 수업 여부는 정확히 입력해주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            #     ClassOP6()
            ClassOP7()
        except ValueError:
            print("잘못된 값이 입력되었습니다 다시 입력해주세요.")
            sleep(2)
            os.system('cls')
            ClassOP6()
    else:
        cls6 = 2
        os.system('cls')
        setting()

#7교시
def ClassOP7():
    global cls7, a7, b7, c7
    if "7" in fullclass:
        try:
            cls7 = 1
            print("-----------------------------------------------")
            print("7교시 수업의 정보를 아래 형식에 맞추어 입력해주시기 바랍니다.")
            print("수업명 실시간여부 수업주소(실시간이 없으면 x)")
            print("실시간 여부 | 1 : 실시간 , 2 : 컨텐츠 , 3 : 미정")
            print("예시 : 수학 1 www.~~~~.com")
            print("-----------------------------------------------")
            a7, b7, c7 = input('정보를 입력하세요. : ').split()
            os.system('cls')
            # if b7 != 1 and b7 != 2 and b7 != 3:
            #     print("실시간 수업 여부는 정확히 입력해주셔야 합니다. 다시 입력해 주세요.")
            #     sleep(2)
            #     os.system('cls')
            # ClassOP6()
            setting()
        except ValueError:
            print("잘못된 값이 입력되었습니다 다시 입력해주세요.")
            sleep(2)
            os.system('cls')
            ClassOP6()
        setting()
    else:
        cls7 = 2
        os.system('cls')
        setting()

############################################################ 버그수정 ############################################################ 

#버그수정용으로 만들어 놓은 함수 
def setting():
    int(classcount)
    class1()

############################################################ 수업시간 감지 ############################################################ 

#1교시 수업 시간 감지
def class1():
    if cls1 == 1:
        if classcount2 >= 1:
            class2()
        else:
            print("-----------------")
            print("1교시 " , a1 , "수업시간까지 대기중입니다.")
            print("수업시간이 되면 자동으로 이동합니다.")
            print("-----------------")
            schedule.every().day.at("09:15").do(CS1)
    elif cls1 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
        sleep(30)
        os.system('cls')
    else:
        error()

#2교시 수업 시간 감지
def class2():
    if cls2 == 1:
        if classcount2 >= 1:
            class2()
        else:
            print("-----------------")
            print("2교시 " , a2 , "수업시간까지 대기중입니다.")
            print("수업시간이 되면 자동으로 이동합니다.")
            print("-----------------")
            schedule.every().day.at("10:10").do(CS2)
    elif cls2 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
        sleep(30)
        os.system('cls')
    else:
        error()

#3교시 수업 시간 감지
def class3():
    if cls3 == 1:
        if classcount2 >= 1:
            class2()
        else:
            print("-----------------")
            print("3교시 " , a3 , "수업시간까지 대기중입니다.")
            print("수업시간이 되면 자동으로 이동합니다.")
            print("-----------------")
            schedule.every().day.at("11:05").do(CS3)
    elif cls3 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
        sleep(30)
        os.system('cls')
    else:
        error()

#4교시 수업 시간 감지
def class4():
    if cls4 == 1:
        if classcount2 >= 1:
            class2()
        else:
            print("-----------------")
            print("4교시 " , a4 , "수업시간까지 대기중입니다.")
            print("수업시간이 되면 자동으로 이동합니다.")
            print("-----------------")
            schedule.every().day.at("12:00").do(CS4)
    elif cls4 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
        sleep(30)
        os.system('cls')
    else:
        error()

#5교시 수업 시간 감지
def class5():
    if cls5 == 1:
        if Un == 1:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("5교시 " , a5 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
            schedule.every().day.at("13:40").do(CS5)
        else:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("5교시 " , a5 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
            schedule.every().day.at("13:35").do(CS5)
    elif cls5 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
    else:
        error()

#6교시 수업 시간 감지
def class6():
    if cls6 == 1:
        if Un == 1:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("6교시 " , a6 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
                schedule.every().day.at("14:35").do(CS6)
        else:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("6교시 " , a6 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
                schedule.every().day.at("14:30").do(CS6)
    elif cls6 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
    else:
        error()

#7교시 수업 시간 감지
def class7():
    if cls7 == 1:
        if Un == 1:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("7교시 " , a7 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
                schedule.every().day.at("15:30").do(CS7)
        else:
            if classcount2 >= 1:
                class2()
            else:
                print("-----------------")
                print("7교시 " , a7 , "수업시간까지 대기중입니다.")
                print("수업시간이 되면 자동으로 이동합니다.")
                print("-----------------")
                schedule.every().day.at("15:25").do(CS7)
    elif cls7 == 2:
        print("---------------------------")
        print(datetime.today() + " 의 수업이 종료되었습니다 ")
        print("프로그램이 30초 후 자동으로 종료됩니다.")
        print("---------------------------")
    else:
        error()

############################################################ 수업 실행 ############################################################ 

#1교시 수업 실행
def CS1():
    os.system('cls')
    if b1 == 1:
        webbrowser.open(c1)
        os.system('cls')
        class2()
    elif b1 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "1교시 컨텐츠", "1교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class2()
        elif msgbox == 2 or msgbox == 4:
            class2()
        else:
            error()
    elif b1 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "1교시 미정", "1교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            class2()
        elif msgbox == 2 or msgbox == 4:
            class2()
        else:
            error()
    else:
        error()

#2교시 수업 실행
def CS2():
    os.system('cls')
    if b2 == 1:
        webbrowser.open(c2)
        os.system('cls')
        class3()
    elif b2 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "2교시 컨텐츠", "2교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class3()
        elif msgbox == 2 or msgbox == 4:
            class3()
        else:
            error()
    elif b2 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "2교시 미정", "2교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            class3()
        elif msgbox == 2 or msgbox == 4:
            class3()
        else:
            error()
    else:
        error()

#3교시 수업 실행
def CS3():
    os.system('cls')
    if b3 == 1:
        webbrowser.open(c3)
        os.system('cls')
        class4()
    elif b3 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "3교시 컨텐츠", "3교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class4()
        elif msgbox == 2 or msgbox == 4:
            class4()
        else:
            error()
    elif b3 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "3교시 미정", "3교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            class4()
        elif msgbox == 2 or msgbox == 4:
            class4()
        else:
            error()
    else:
        error()

#4교시 수업 실행
def CS4():
    os.system('cls')
    if b4 == 1:
        webbrowser.open(c4)
        os.system('cls')
        class5()
    elif b4 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "4교시 컨텐츠", "4교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class5()
        elif msgbox == 2 or msgbox == 4:
            class5()
        else:
            error()
    elif b4 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "4교시 컨텐츠", "4교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요", 0)
            sleep(5)
            class5()
        elif msgbox == 2 or msgbox == 4:
            class5()
        else:
            error()
    else:
        error()

#5교시 수업 실행
def CS5():
    os.system('cls')
    if b5 == 1:
        webbrowser.open(c5)
        os.system('cls')
        class6()
    elif b5 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "5교시 컨텐츠", "5교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class6()
        elif msgbox == 2 or msgbox == 4:
            class6()
        else:
            error()
    elif b5 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "5교시 미정", "5교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            class6()
        elif msgbox == 2 or msgbox == 4:
            class6()
        else:
            error()
    else:
        error()

#6교시 수업 실행
def CS6():
    os.system('cls')
    if b6 == 1:
        webbrowser.open(c6)
        os.system('cls')
        class7()
    elif b6 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "6교시 컨텐츠", "6교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            class7()
        elif  msgbox == 2 or msgbox == 4:
            class7()
        else:
            error()
    elif b6 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "6교시 미정", "6교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            class7()
        elif msgbox == 2 or msgbox == 4:
            class7()
        else:
            error()
    else:
        error()

#7교시 수업 실행
def CS7():
    os.system('cls')
    if b7 == 1:
        webbrowser.open(c7)
        os.system('cls')
        CloseProgram()
    elif b7 == 2:
        if msgbox == 1 or msgbox == 3:
            msg = ctypes.windll.user32.MessageBoxW(None, "7교시 컨텐츠", "7교시 수업은 컨텐츠 수업입니다.", 0)
            sleep(5)
            CloseProgram()
        elif msgbox == 2 or msgbox == 4:
            CloseProgram()
        else:
            error()
    elif b7 == 3:
        if msgbox == 1 or msgbox == 2:
            msg = ctypes.windll.user32.MessageBoxW(None, "7교시 미정", "7교시 수업은 미정입니다. 클래스에 들어가 직접 확인해주세요.", 0)
            sleep(5)
            CloseProgram()
        elif msgbox == 2 or msgbox == 4:
            CloseProgram()
        else:
            error()
    else:
        error()

############################################################ 기타 ############################################################ 

ProgramStart() #시작

#스케쥴 1초마다 확인
while True:
    schedule.run_pending()
    time.sleep(1) 