# [3 * 3 리스트형태]

# a_list = list(range(1,10))

# for i in a_list:
#     print(i,end="\t")
#     if i%3 == 0:
#         print()

#4x4 리스트 형태

# b_list = list(range(1,17))

# for i in b_list:
#     print(i,end="\t")
#     if i%4 == 0:
#         print()

# c_list = list(range(1,26))

# for i in c_list:
#     print(i,end="\t")
#     if i%5 == 0:
#         print()

# d_list =[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#     ]

# for aa in d_list:
#     for a in aa:
#         print(a,end="\t")
#     print()

# f_list = [9,1,2,5,6,8,3,4,7]
# #[3 * 3 리스트 형태]

# for i,val in enumerate(f_list):
#     print(val,end="\t")
#     if i ==0 :
#         continue
#     if i%3 == 0:
#         print()
        
import random

a_list = list(range(1,17))
random.shuffle(a_list)
print(a_list)
### 4 * 4 리스트 형태로 출력하시오

for i,val in enumerate(a_list):
    print(val,end="\t")
    if i == 0 :
        continue
    if i%4 == 0:
        print()