#셋 - 키값만 존재. 중복 불가
#중복 제거하는 때에 유리
set1 = {1,1,2,3,4,2}
print(set(set1))

a_list = [1,2,3,1,1,5,6,4,4,3]
print(set(a_list))

names = ['홍길동','유관순','이순신','홍길동','홍길동','유관순']
nset = set(names)   #변수 저장
print(nset)         
print(set(names)) 