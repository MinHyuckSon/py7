#국어, 영어, 수학, 점수를 입력받아 합계 평균을 출력하시오

ikor = input("국어점수를 입력하세요")
iEng = input("영어점수를 입력하세요")
iMath = input("수학점수를 입력하세요")

iPlus = int(ikor)+int(iEng)+int(iMath)

print("합계",iPlus)

print(int(iPlus))

#num = int(int(input("국어점수를 입력하세요")))
#num2 = int(int(input("영어점수를 입력하세요")))
#num3 = int(int(input("수학점수를 입력하세요")))
#print("합계 : ",num+num2+num3) 쉼표구분자를 사용하면 타입이 달라진다.
#print("평균 : ",num+num2+num3/3)