#이름, 국어
#입력받아 출력하시오
print("[ 학생성적입력 ]")
print("1.학생 ")
print("2.학생성적출력")
print("3.학생성적수정")






stu_Data = [[]]


strName = input("이름을 입력하시오")
iKor = int(input("국어점수를 입력하시오"))
iEng = int(input("영어점수를 입력하시오"))
iMath =  int(input("수학점수를 입력하시오"))

iTotal = iKor + iEng + iMath
iEvg   = iTotal/3

stu_Data[[]]
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("{}\t{}\t{}\t{}\t{}\t{}".format(strName,iKor,iEng,iMath,iTotal,iEvg))