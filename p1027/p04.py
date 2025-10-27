#숫자 2개를 입력받아 사칙연산 결과를 출력하시오.
#10+5 = 15
#10-5 = 5
#10*5 = 50
#10/5 = 2

iNum1 = input("숫자를 입력하세요")
iNum2 = input("숫자를 입력하세요")
iNum3 = int(iNum1)+int(iNum2)
print("%s+%s는 %d"% (iNum1, iNum2, int(iNum1)+int(iNum2)))
print("%s-%s는 %d"% (iNum1, iNum2, int(iNum1)-int(iNum2)))
print("%s곱하기%s는 %d"% (iNum1, iNum2, int(iNum1)*int(iNum2)))
print("%s나누기%s는 %d"% (iNum1, iNum2, int(iNum1)/int(iNum2)))