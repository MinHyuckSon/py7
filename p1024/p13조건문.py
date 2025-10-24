#if문은 :으로 꼭 닫아줘야함
# 아래문구는 들여쓰기를 해줘야 인식함

# if 10>5:
#     print("정상입니다")
# else:
#     print("비정상입니다")

#숫자를 입력받아 100보다 큰 수 인지 아닌지 출력하시오.
# 100보다 큰 수 입니다. 100보다 작은 수 입니다.

# iTest = 0;
# print("숫자를 입력하시오")
# iTest = int(input("iTest"))

# if(iTest<100):
#     print("100보다 작은수 입니다.")
# else:
#     print("100보다 큰 수 입니다")

#입력된 숫자가 짝수인지 홀수인지 출력하시오.
#짝수입니다. 홀수입니다.

iDest = 0

print("숫자를 입력하시오")

iDest = int(input())

if(iDest%2 == 0):
    print("짝수입니다")
else:
    print("홀수입니다")
