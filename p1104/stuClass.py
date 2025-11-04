class CStus: 
    stuTotal = 0
    def __init__(self,_stuNum,_stuName,_stuKor,_stuEng,_stuMath):
        self.stuNum     = _stuNum
        self.stuName    = _stuName
        self.stuKor     = _stuKor
        self.stuEng     = _stuEng
        self.stuMath    = _stuMath
        self.stuTotal   = _stuKor + _stuEng + _stuMath
        self.stuAvg     = stuTotal/3
        self.rank       = 0

    def Set_Info(self,_stuNum,_stuName,_stuKor,_stuEng,_stuMath):
        self.stuNum     = _stuNum
        self.stuName    = _stuName
        self.stuKor     = _stuKor
        self.stuEng     = _stuEng
        self.stuMath    = _stuMath
        


StuInfo = CStus()

StuInfo.Set_Info(input("학생번호를 입력하세요: "),input("학생이름을 입력하세요"),\
                int(input("국어점수를 입력하세요: ")),int(input("영어점수를 입력하세요: ")),\
                   int(input("수학점수를 입력하세요: ")))

print(StuInfo.stuNum,StuInfo.stuName,StuInfo.stuKor,StuInfo.stuEng,\
    StuInfo.stuMath)