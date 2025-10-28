#for 변수 in 범위

# for i in range(5):
#     print(i,end="") #한칸씩 띄워서 출력

# iSour = 0

# for i in range(1, 101):
#     iSour = iSour + i
# print("합계 : ", iSour)

# 100을 넘는 위치는 얼마를 더 할때 일까요?
#1+2+3+4+5+6+7+8+9+10+11+12+13+14

# iTotal = 0

# for i in range(1,101):
#     if(iTotal < 1000):
#        iTotal = iTotal + i
#        print(i,iTotal)
       
#     else:
#         break
    
# print(iTotal)
    
#1*2*3....*10 결과값 출력

iResult = 0

for i in range(1,11):
    iResult = (iResult+1) * i
    print("{}곱하기{}는 {}".format(int((iResult)/i),i,iResult))

