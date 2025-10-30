# a_list = [1,2,3,4,5,]
# b_list = list(range(1,6))
# c_list = [i for i in range(1,6)]#리스트 내포.

# print(a_list)
# print(b_list)
# print(c_list)

#append, insert, extend (값 입력)
#pop, del, remove, clear (값 삭제)
# 수정 : a_listp[index] 
# index : 해당 위치값 리턴

aa_list =[10,5,15,7,9]
# print(aa_list)

# num = int(int(input("")))

#2. 비교
# print(aa_list) #[10,5,15,7,9]
# num = int(input("원하는 번호를 입력하세요.>> "))
# if num in aa_list:
#     aa_list[aa_list.index(num)] = "X"
    
# print(aa_list)

# 5*5의 2차원 형태 리스트를 생성
# 좌표 만들기
#qjsgh qlry

lDest = list(range(25))

for idx,a in lDest:
    if idx%5 == 0:
        print()
        
    print(idx+1)
    

#print(lDest)
