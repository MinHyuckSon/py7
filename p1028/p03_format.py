# year = 2025
# month = 10
# day = 28
#2025년 10월
# print("%d년\t%d월\t%d일"%(year,month,day))
# date1="{}년{}월{}일".format(year,month,day) 포맷함수
# print(date1)

# a1=100000

# b= 25.2345678

# b_format = "{}".format(b)
# b_format = "{:.2f}".format(b)

#list타입 format함수 사용
# stus =['홍길동',100,90,80]
# print("이름 : {},국어 : {},영어 : 수학{}".format(\
#     stus[0],stus[1],stus[2],stus3))
# # *stus->전개연산자 stus[0],stus[1],stus[2],stus[3]
# print("이름 : {},국어 : {},영어 : 수학{}".format(*stus)
      
      
# # 1번 홍길동 100,000
# bank = [1,'홍길동',100000]
# print("{}번\t{}\t{:,}원".format(bank[0],bank[1],bank[2]))

dest = ["유관순",3,98.234567]

print("이름 : {} \t단계 {}\t성공률 {:.2f}".format(\
    dest[0],dest[1],dest[2]))

##f함수
print(f"이름: {dest[0]}\t단계 {dest[1]}\t성공률{dest[2]}")
