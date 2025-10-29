import random
#randnrange() 1~10까지의 랜덤 숫자를 3개를 출력하시오
r_num = random.randrange(1,101)
iNumbers = []

for i in range(10):
    my_Num = int(input("숫자를 입력하시오 "))
    iNumbers.append(my_Num)
    if r_num == my_Num:
        print("당첨되었습니다.")
        break
    elif r_num>my_Num:
        print("더 큰 수를 입력하세요.!!!")
    else:
        print("더 작은 수를 입력하세요!!!")

print("당첨번호 : {}\n입력한 횟수 : {}\n입력한 숫자들 : {}".format(r_Num,(len(iNumbers)),iNumbers))


# for i in range(1,10):
#     print(random.randrange(1,11))
    
# print(random.sample[1,2,3,4,5,6,7,8,9],5)
# print(random.sample(range(1,11),5))
# print(list(range))    