import random

stu_list = []
stu_count = 101 #학생번호
titles=['번호','이름','국어','영어','수학','합계','평균']

while True:
    print("[학생성적관리프로그램]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("4. 학생성적삭제")
    print("5. 프로그램종료")
    print("-"*50)
    iChoice = int(input("원하는 번호를 입력하세요 >>"))
    
    if iChoice == 1: #학생성적입력
        
        print("[학생성적입력]")
        insList = []
        iStuNum = stu_count + 1
        strStuName = input("이름을 입력하세요")
        iKor    = int(input("국어성적을 입력하세요"))
        iEng    = int(input("영어성적을 입력하세요"))
        iMath   = int(input("수학점수를 입력하세요"))
        iTotal  = iKor + iEng + iMath
        iEvg    = iTotal/3
        
        insList.append(iStuNum)
        insList.append(strStuName)
        insList.append(iKor)
        insList.append(iEng)
        insList.append(iMath)
        insList.append(iTotal)
        insList.append(iEvg)
        
        stu_list.append(insList)
        
    elif iChoice == 2:
        print("[학생성적확인]")
        for i,idx in titles:
            for j,jdx in stu_list:
                print(titles[i],)
            
    
    elif iChoice == 3:
        pass
    
    elif iChoice == 4:
        pass
    
    elif iChoice == 5:
        break
    