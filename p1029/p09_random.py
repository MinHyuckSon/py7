import random

lotto = random.sample(range(1,46),6)

#6개 숫자를 입력받아 출력하시오
#변수 선언
num_list = []
iCount = 0
c_list = []

for i in range(1,7):
    num_list.append(input("숫자를 입력하시오 "))
    

    
for i in lotto:
    for j in num_list:
        if i== j:
            iCount = iCount+1
            c_list.append(i)
            break
    


#4.결과화면 출력
num_list.sort()        
print("입력한 번호 : {}".format(num_list))
lotto.sort()
print("당첨번호 : {}".format(lotto))
print("{}개 번호당첨".format(iCount))

#5번째 당첨금 출력
if iCount == 0 or 1: 
    print("당첨금 : 0원")
elif iCount == 2:
    print("당첨금 : 5,000원")
elif iCount == 3:
    print("당첨금 : 50,000원")
elif iCount == 4:
    print("당첨금 : 10,0000원")
elif iCount == 5:
    print("당첨금 : 5,000,000원")
elif iCount == 6:
    print("당첨금 : 200,000,000원")
    