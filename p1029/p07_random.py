import random # 선언 랜덤클래스 불러오기
print(random.random())  #0,00000000 <= //이 함수 밑으로는 파이썬만 가능한 함수
print(random.randrange(1,11)) # 1~10사이의 숫자를 랜덤으로 가져옴

#해당 리스트에서 4개를 랜덤으로 가져옴. 중복이 안됨
print(random.sample([1,2,3,4,5]),4)

#해당 리스트에서 4개를 랜덤으로 가져옴 중복가능
print(random.choice[1,2,3,4,5],k=4)

#해당리스트 순서를 랜덤으로 조정
a_list = [1,2,3,4,5]
random.shuffle(a_list)
print(a_list)