print("""삼중
      따옴 표는
      이렇게 쓸 수 있게 해준다""")

#문자열
str1 = "안녕"
str2 = '안녕'

print(str1)
print(str1,str2)
print(str1,"--",str2)
# %출력 자리수지정, 빈공백에 0을 표시 %05d, 소수점 제한 %.2f
print("%s -- %s"%(str1, str2))

print("안녕"*10) #문자열 반복연산. 파이썬에서만 쓸 수 있는 방식
print("이름\t국어\t수학\t") 

#문자열 선택. 문자는 주소를 가질 수 있다.
name = "안녕하세요"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

#문자슬라이싱
print(name[0:4])  #0부터 4앞까지 출력(0-3)
print(name[2:4])  #2부터 4앞까지 출력(2~3)
print(name[2:])   #뒷자리 입력하지 않으면 마지막까지 출력
print(name[:3])   #앞자리 입력하지 않으면 처음부터 출력

#문자 길이
print(len(name)) # 문자열의 길이 출력

#슬라이싱 - 스탭 (안) 녕 (하) 세 (요)
print(name::2) #모든 문자열 2칸씩 띄워 출력
print(::-1)    # 반대로 출력

# 88101-211111 주민번호
# 1- 남자, 2 - 여자 ,3 - 남자, 4 -여자
jumin = "88101-211111"
#2만 출력하는 방법
print(jumin[7])

#특별한 경우가 아닌이상 문자배열은 0부터 시작한다.