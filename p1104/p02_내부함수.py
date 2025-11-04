#lambda() 함수 = 함수를 한줄로 간단히 만든 것

#함수 선언, 함수 정의
def add(a,b):
    return a+b

#함수호출
print(add(10,20))

#함수 축약 rambda()
# def선언하는것과 같음
# lambda 매개변수 : 함수수식
#resul : 함수명(값, 값)
result = lambda a,b : a+b

print(result(10,20))

#map함수 = 여러개의 함수 적용시킬때 사용 / 리스트 = map(함수, 리스트)