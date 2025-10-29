# 4*4 출력
import random


a_list = list(range(1,10))
random.shuffle(a_list)

while True:
    print(a_list)
    print("[ 좌표 맞추기 게임 ]")
    print("-"*30)
    for idx, a in enumerate(a_list):
        print(a,end="\t")
        if(idx+1)%3 == 0:
            print()
            
            print()