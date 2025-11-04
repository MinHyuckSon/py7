#클래스 장점 :
#1.변수, 함수를 함께 묶음 
#2. 여러개 변수, 여러개 함수를 객체선언으로 동시 생성가능
#3. 각각의 변수에 값을 제한할 수 있음 = 값 제한 접근제한




#함수 선언
class student:
    
    #변수 미리 지정
    hour = 0
    minuete = 0
    second = 0
    
    #생성자 - 함수를 호출하지 않아도, 객체 선언시 자동호출
    def _init_(self):
        pass
    
    #변수 = class명 : 객체선언 - class공간을 만들어줌
    s = student