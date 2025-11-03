#함수 : 특정명령어를 집합시킴 - 반복을 제거, 유지보수를 쉽게함

#함수형태
#def 함수명():
    #pass
    
#함수호출
#함수명()

def calculate():
    print("더하기")
    print("빼기")
    print("곱하기")
    print("나누기")
    
    a,b = 10,2
    calculate()
    a,b = 5,3
    calculate()
    a,b= 5,1