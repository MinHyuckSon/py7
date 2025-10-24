# +더하기, -빼기, *곱하기, /나누기
# //:몫, % 나머지, **제곱

# print(10+20)
# print(10-20)
# print(10*20)
# print(10/20)    # 3.33333
# print(10//20)   # 3
# print(10%20)    # 1 나머지
# print(10**3)    # 10*10*10 = 1000

# #두 수를 입력받아 위의 연산을 출력하시오
# #+,-,*,/,//,%,**

# num = int(input("숫자를 입력하세요"))
# num2 = int(input("숫자를 입력하세요"))

# print(num+num2)
# print(num-num2)
# print(num*num2)
# print(num/num2)
# print(num//num2)
# print(num%num2)
# print(num**num2)

### 789원 동전으로 교환을 하려고 합니다.
### 500, 100, 50, 10
# 500-1(몫) 나머지/ 100-1(몫) 나머지 50-1(몫) 나머지10-3몫
# iNum1 = 780
# iNum2 = 500

# money1 = iNum1//iNum2 #몫 - 갯수
# money2 = iNum1%iNum2
# money3 = 

# money =print("500원 동전 %d 개"% money1)
# print("100원 동전 %d 개"%(money3%100))

iCoin = 1597000

iDest1= 50000
iDest2= 10000
iDest3= 5000
iDest4= 1000
iDest5= 500
iDest6= 100
iDest7= 50
iDest8= 10

iSour1 = iCoin//iDest1 # 몫
iResult1 = iCoin%iDest2 # 나머지
iSour2 = iResult1//iDest2
iResult2 = iResult1%iDest3
iSour5 = iSour4//iDest5
iSour6 = iSour4%iDest6
iSour7 = iSour6//iDest7
iSour8 = iSour6%iDest8

print("%d는, %d원, %d개\n %d원, %d개\n %d원, %d개\n %d원 %d개" % (iCoin,iDest1,iSour1,iDest2,iSour2,iDest3,iResult2,iDest4,iSour5))