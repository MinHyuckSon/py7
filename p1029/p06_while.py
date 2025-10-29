n_list = []
i=0
while True:
    if i<4:
        name = input("{}번째 이름을 입력하세요".format(len(n_list)+1))
        kor = int(input("{}번째 국어 점수를 입력하세요".format(len(n_list)+1)))
        n_list.append(name)
        print(n_list)
    else:
        break
    i = i+1
    
for i in range(n_list):
    print ("이름\t국어")
    print("-"*50)
    print("".format(*n_list[i]))




# n_list = []


# #반복시작--------

# while true:

#     name = input("이름을 입력하세요. ")
#     n_list = n_list.append(name)
#     print(n_list)