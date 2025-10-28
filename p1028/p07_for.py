#for문
# 구조 - for 변수 in범위(range,list,문자열) :

# for i in range(10):
#     print("반갑습니다.")


#1~5 for문을 사용해서 출력하시오

# for i in range(5):
#     print(i+1)

    
# #숫자를 입력받아, 입력받은 값을 출력하는것을 5번 반복하시오    
    
# iSour = int(input("숫자를 입력하세요"))

# for i in range(5):
#     print(iSour)

#1~10까지 숫자의 합을 출력하시오. 반복 10번
iTotal = 0
# for i in range(1,11):
#     iTotal = i + iTotal
    
# print(iTotal)

#홀수만 출력 합계


# for i in range(1,11,2):
#     iTotal = i + iTotal
#     print(iTotal)
    
# print("홀수의 합은 ",iTotal)

for i in range(10):
    if i%2 == 1:
        iTotal = (i) + iTotal
        print(i,iTotal)    
    
    
print(iTotal)    



    
    
    
    
    
    
# a_list =[]
# for i in range(10):
#     num = int(input("숫자를 입력하세요. "))
#     if num%2 == 0: