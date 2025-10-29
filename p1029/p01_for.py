#5,21까지 출력하시오
# for i in range(5,22):
#     print(i)
    

# #1,10까지 출력하시오
# for i in range(10):
#     print(i+1)

# #0,9까지 출력하시오
# for i in range(1,10,2): #홀수만 출력하시오
#     print(i)
    
# for i in range(1,10):
#     if i%2 == 0:
#         continue
#     print(i)

# for i in range(1,10):
#     print("{}단".format(i))
#     for j in range(1,10):
#         print("{}X{}={}".format(i,j,i*j,)end=" " )
        
#     print()
        
# for i in range(1,10):
#     if i%2==1 :continue
#     print("{}단".format(i))
#     for j in range(1,10):
#             print("{} X {} = {}\t".format(i,j,i*j),end= "")
        
#     print()

#for문을 사용해서 0을 10개 들어가는 리스트를 만드시오

a_list = []

# for i in range(10):
#     a_list.append(0)
# print(a_list)


# a_list = list('0'*10)
# print(a_list)

#list내포
a_list = ['0' for _ in range(10)]

