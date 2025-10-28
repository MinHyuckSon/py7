# a = 100
# if a>10: #True,False 2가지 bool(불)
#     print("참입니다.")

# num= int(input("숫자를 입력하세요.>>"))
# if num>="0":
#     print("양수입니다.")
# else:
#     print("음수입니다.")

#입력한 숫자에 50을 더해서 100보다 큰 수인지 출력하시오

# iNum = int(input("숫자를 입력하시오"))

# if iNum+50 >= 100:
#     print("입력한 값",iNum,"현재값",iNum,"100보다 큰 수입니다.")
#     print("입력한 값: %d, 현재값: %d,%s"%(iNum,iNum+50,"100보다 큰 수 입니다."))
# else:
#     print("입력한 값",iNum,"현재값",iNum,"100보다 작은 수 입니다.")
#     print("입력한 값: %d, 현재값: %d,%s"%(iNum,iNum+50,"100보다 작은 수 입니다."))

# iNum = int(input("숫자를 입력하세요"))

# if iNum % 2==0:
#     print("입력한 값: %d, 짝수입니다"%iNum)
# else:
#     print("입력한 값: %d, 홀수입니다."%iNum)


#문자열 슬라이싱
#문자열은 두개의 주소값을 가진다. 양수 혹은 음수
str1 = "안녕하세요"
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])

print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])

print(str1[1:3]) # 1부터 3번 앞 2번까지 출력 "녕하"
print(str1[1:4]) #녕하세
#두번째 입력이 없으면 끝까지
print(str1[1:]) #녕하세요
print(str1[:3]) #안녕하세

#처음입력이 없으면 첫 시작부터
print(str1[::1]) #안녕하세요
#처음번호:끝번호:스텝(증가)
print(str1[::-1])#요세하녕안
print(str[1:5:3])#안녕하세요 -> 녕요

a = "123456789"
print(a[::2]) #홀수만 찍음
print(a[1::2])#짝수만 찍음
print(a[2::3])#3의 배수

###입력을 받아, 마지막 글자를 출력하시오
strInput = input("문자를 입력하세요.")
print("마지막 글자 :",strInput[-1])