#if문은 :으로 꼭 닫아줘야함
# 아래문구는 들여쓰기를 해줘야 인식함

# if 10>5:
#     print("정상입니다")
# else:
#     print("비정상입니다")

#숫자를 입력받아 100보다 큰 수 인지 아닌지 출력하시오.
# 100보다 큰 수 입니다. 100보다 작은 수 입니다.

# iTest = 0;
# print("숫자를 입력하시오")
# iTest = int(input("iTest"))

# if(iTest<100):
#     print("100보다 작은수 입니다.")
# else:
#     print("100보다 큰 수 입니다")

#입력된 숫자가 짝수인지 홀수인지 출력하시오.
#짝수입니다. 홀수입니다.

# iDest = 0

# print("숫자를 입력하시오")

# iDest = int(input())

# if(iDest%2 == 0):
#     print("짝수입니다")
# else:
#     print("홀수입니다")


# 내부모듈
# import datetime

# now = datetime.datetime.now()

# print(now.year,"년")
# print(now.month,"월")
# print(now.day,"일")
# print(now.hour,"시")
# print(now.minute,"분")
# print(now.second,"초")

#입력한 주민번호의 월을 파악해서 현재 날짜와 같은 월이면
#이벤트 대상입니다.,이벤트 대상이 아닙니다. 출력하시오

# import datetime

# now = datetime.datetime.now()

# jumin = input("주민번호를 입력하세요")

# if((int(jumin[2:4]))==now.month ):
#     print("이벤트 대상입니다")
# else:
#     print("이벤트 대상이 아닙니다")

# n ="03"
# print(int(n))
# n2 = 3
# print("%02d" % n2)

str1 ="abcdefg"
# [시작번호:끝번호:스텝]
print(str1[1:6::2]) #bdf
print(str1[:5:2-1]) #fed
print(str1[::-1])   #gfedcba 역순으로 숫자를 부름