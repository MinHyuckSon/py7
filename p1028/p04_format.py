#3개의 값을 입력받아, 숫자를 모두 합친 금액을 출력하시오
#1000원 이상 입력하세요.
#총금액 : 1,000,000

iMoney1 = int(input("금액을 입력하세요"))
iMoney2 = int(input("금액을 입력하세요"))
iMoney3 = int(input("금액을 입력하세요"))

iTotal = iMoney1 + iMoney2 + iMoney3

fMoney = print("첫번째 : {}원\n두번째 : {d}원\n세번째 :{d}원\n총합{:.d}원").format(iMoney1,iMoney2,iMoney3,iTotal)
    

# year = 2025
# month = 10
# day = 28

# day_format = "{:d}년 {:03d}월{}일.format(year,month,day)



# #이름, 국어, 영어, 수학점수를 입력받아 홍길동, 국어,영어,수학,합계, 평균 출력하시오.
# a_list = ['홍길동',100,90,80,270,90.000000]
# print("이름:{},국어{},영어{},수학:{},합계:{},평균{:.2f}".format\
#     (a_list[0],a_list[1],a_list[2],a_list[3],a_list[4],a_list[5]))
# print("이름:{},국어{},영어{},수학:{}합계:{},평균{:.2f}".format(*a_list))