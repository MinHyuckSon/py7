import random

listWinNum = []
listSelect = []
iCount = 0

listWinNum = random.sample(range(1,46),6)

for i in range(1,7):
    listSelect.append(int(input("숫자를 입력하세요 : ")))
    if 0 < listSelect[i] < 46:
        print("1~45까지의 숫자를 입력하세요")
        listSelect.pop()
        break 
    
# for i in listWinNum:
#     for j in listSelect:
#         if i == j:
#             iCount=iCount+1
        
    
# print(iCount)
    
listWinNum.sort ()
listSelect.sort ()

#print(iCount)
print(listWinNum)
print(listSelect)  