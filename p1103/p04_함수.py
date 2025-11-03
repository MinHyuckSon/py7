#stus = [1,'홍길동',100,90,80]
#함수를 제대로 구성해서 stus 리스트를 아래와 같이 변경하시오.
#stus = [1,'홍길동',100,90,80,270,90.00]
#함수를 꼭 사용할 것

num1 = int(input("숫자를 입력하세요. "))
num2 = int(input("숫자를 입력하세요. "))
str1 = input("원하는 사칙연산 기호를 입력하세요.(+,-,*,/)")

def cal(_iNum1,_iNum2,_str):
    if str1 == ("+"):
        return print(_iNum1 + _iNum2)
    
    elif str1 == ("-"):
        return  print(_iNum1 - _iNum2)
    
    elif str1 == ("*"):
        return print( _iNum1 * _iNum2)
    
    elif str1 == ("-"):
        return print( _iNum1 / _iNum2)

    else:print("잘못된 사칙기호 입니다.")


#1~10까지의 합이 출력되도록 구성하시오.
#cal(1,10)

#함수정의
def cal(_iNum1,_iNum2):
      sum = 0
      for i in range(_iNum1,_iNum2+1):
          sum += 1
          
      print(sum)

#함수호출
#값 출력