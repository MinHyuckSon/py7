
import random

english={
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea',
    '물':'water',
    '지구':'earth',
    '하늘':'sky',
    '공기':'air',
    '고양이':'cat',
    '강아지':'dog',
    '아기':'baby',
    '엄마':'mother',
    '아빠':'father',
    '집':'house',
    '소년':'boy',
    '소녀':'girl',
    '열쇠':'key'
}

a_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
quest = random.sample(a_list,5)
quest.sort()
quest_dic = {}

for i,k in enumerate(english.keys()):
    if i in quest:
        count = 0
        #정답입력
        print("{}은(는) 영어로 뭘까요?".format(k))
        answer = input()
# iCount = 0
# #key 가 5 value는 무제한
# import random

# iRange = random.sample(range(1,21),5)
# iExit = 5
# for k,v in english.items():
#     k=iRange[0+1]
#     print("{}은(는) 영어로 뭘까요?".format(k,v))
#     answer=input(">> ")
#     iExit -= 1
#     if answer == v and iExit!=0:
#         print("정답입니다.")
#         iCount+=1
#     elif answer != v and iExit!=0:
#         print("오답입니다 :")
#         continue
    
#     else: break
    
    
# print("총 정답수는 {}개 입니다".format(iCount))





#홍:100, 이:90, 유80 딕셔너리에 추가
# c_dic = {}
# c_dic['홍'] = 100
# c_dic['이'] = 90
# c_dic['유'] = 80
# print(c_dic)

# names = ['홍','홍','김','이','유','홍','김','강','홍']
# n_dic = {}

# for i in names:
#     if i not in n_dic:
#         n_dicp[i] = ""