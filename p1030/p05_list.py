# a_list = [1,2,3,4,5,6,7,8,9]    #len(a_list)   9
# b_list = [                      #len(b_list)   3 
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for a in a_list:
#     print(a,end="\t")

# for b in b_list:
#     print(b,end="\t")

    

#print(stu_list[1][3])
#수정하고 싶은 학생
# print("1. 홍길동")
# print("2. 유관순")
# print("3. 이순신")
# print("-"*50)
# num = int(input("수정할 학생번호를 입력하세요.>>"))-1
# # 1번 선택
# # 국어점수를 70점으로 변경하고 합계 평균 변경해서 출력하시오.
# stu_list[num]
# print("수정할 학생은",stu_list[num][0])

# num = input("수정할 과목을 선택하세요")

stu_list = [
    ['홍길동', 100,90,80,270],
    ['유관순',90,90,89.269],
    ['이순신',100,100,100,300]
    ]


while True:
    print("     학생성적관리")
    print("-"*50)
    print("학생을 선택하세요\n1. {}\n2. {}\n3. {}")
    
