english={
    '사랑':'love',
    '차' : 'car',
    '커피' : 'coffee',
    '전화' : 'pohn',
    '컴퓨터': 'computer',
    '이름':'name',
    '한국': 'korea'
}
iCount = 0
for k,v in english.items():
    print("{}은(는) 영어로 뭘까요?".format(k))
    answer=input(">> ")
    if answer == v:
        print("정답입니다.")
        iCount+=1
    else:
        print("오답입니다 :",v)
    
print("총 정답수는 {}개 입니다".format(iCount))





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