class Student:
    iStuNum = 0
    strStuname = ""
    iKor = 0
    iEng = 0
    iMath= 0
    iTotal = 0
    iAvg = 0
    iRank = 0
    
    def sum(self):
        # self.iTotal = self.iKor + self.iEng + self.iMath
        return self.iKor + self.iEng + self.iMath
    
    def Avg(self):
        return self.iTotal / 3
    
    