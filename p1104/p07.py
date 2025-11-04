#클래스
#클래스 내 변수, 함수를 사용하려면, 무조건 객체선언을 해야 사용할 수 있음
#객체선언 : 참조변수 = 클래스 명
class Car:
    color = ""
    speed = 0
    
    #클래스내 함수 첫매개변수로 self
    def upSpeed(self,num):
        #함수 내 변수를 선택
        self.speed += num
    
    def downSpeed(self,num):
        self.speed -= num
        
c1 = Car() #객체선언 = 변수 함수 사용
           # 사용방법 = 참조변수.변수명
c1.upSpeed(50)
print(c1.speed)
c1.downSpeed(30)
print(c1.speed)
c1.speed = 100
print(c1.speed)
