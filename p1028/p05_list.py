#list추가 append,insert,extend
#append = 제일뒤에 추가
#복합변수의 값이 변경이 됨.

#insert -(위치,값)
a_list = []
a_list2 = [4,5,6]
a_list.append(10)

# a_list.extend(a_list2)
a_list + [4,5,6]

print(a_list)

#list 값 변경
a_list2[2] = 10000 #없는 주소를 넣으면 에러

# 삭제 = pop()-제일 뒤 삭제, del-해당위치삭제, remove-해당값 삭제, clear-모두삭제

aa_list = [1,2,3,4,5,6,7]
aa_list.pop() #제일 뒤 삭제
print(aa_list)
del aa_list[0] #해당위치 삭제
aa_list.remove(5)#해당 값 삭제
aa_list.clear()#전체 값 삭제

#[]1개 :1차원 리스트
#[[]]2개: 2차원 리스트
#[[[]]]3개: 3차원 리스트

b_list = [["홍길동",100],["유관순,99"],["이순신,90"],["김구,89"]]