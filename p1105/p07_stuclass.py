class Student:
    #전역변수 만들어짐.
    def __init__(self,_stuNum,_stuName,_Kor,_Eng,_Math):
        self.stuNum = _stuNum
        self.stuName = _stuName
        self.Kor = _Kor
        self.Eng = _Eng
        self.Math = _Math
        self.Total = self.Kor + self.Eng + self.Math
        self.Avg = self.Total/3
        self.Rank = 0
    #__str__ 객체, 참조변수를 출력하면 함수실행을 시킴
    def __str__(self):
        return (f"{self.stuNum} \t {self.stuName} \t {self.Kor} ")
    
    def Rander_Menu():
        print("-"*50)
        print(" "*10,"[ 학생성적프로그램 ]")
        print("-"*50)
        print("1. 학생성적입력")
        print("2. 학생성적출력")
        print("3. 학생성적수정")
        print("4. 학생성적삭제")
        print("0. 프로그램종료")
        print("-"*50)
        
    def s_Total(self):
        self.Total = self.Kor + self.Eng + self.Math
        
    def s_Avg(self):
        self.Avg = self.Total / 3
        
s1 = Student()
        
class Students:
    stu_list = []
    
    def add(self,studnt):
        self.stu_list.append(studnt)
        
stus = Students()

stus.add(Student(10101,'홍길동',100,100,99))
stus.add(Student(10102,'유관순',90,90,99))    
stus.add(Student(10103,'이순신',80,80,99))           

print(s1)