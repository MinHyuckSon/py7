#학생성적입력,출력,삭제를 구현하시오

import random

stu_list =[
    [10101,'홍길동',80,80,80,240,80.00]
    [10102,'유관순',90,90,90,270,90.00]
    [10103,'이순신',100,100,100,300,100.00]
    ]

iStu_count = 10103
iChoice = 0

title = ['번호','이름','국어','영어','수학','합계','평균']

while True:
    print("-"*50)
    print("[학생성적관리프로그램]")
    print("-"*50)
    print("1.학생성적입력\n2.학생성적출력\n3.학생성적수정\n4.학생성적삭제\n5.프로그램종료")
    iChoice = input("원하시는 작업을 입력해주세요")
    
    if iChoice == 1:
        ins_list =[]
        iStu_count += 1
        _strName = input("이름을 입력하세요 :")
        _iKor   = int(input("국어성적을 입력하세요 : "))
        _iEng   = int(input("영어성적을 입력하세요 : "))
        _iMath  = int(input("수학점수를 입력하세요 : "))
        _iTotal = _iKor + _iEng + _iMath
        _fAvg   = _iTotal / 3
        
        ins_list.append(iStu_count)
        ins_list.append(_iKor)
        ins_list.append(_iEng)
        ins_list.append(_iMath)
        ins_list.append(_iTotal)
        ins_list.append(_fAvg)
        
        stu_list.append(ins_list)
        
    elif iChoice ==2:
        for i,idx in title:
            for j,jdx in stu_list:
                print("{}{}\t{}{}\t{}{}\t{}{}\t{}{}\t{}{}\t{}{}".format(\
                    #학생번호, 이름, 국어, 영어,  수학,  합계, 평균     
                    ))
    elif iChoice ==3:
        pass
    elif iChoice ==4:
        pass
    elif iChoice ==5:
        break