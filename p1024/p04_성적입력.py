name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요"))
eng = int(input("영어점수를 입력하세요"))
meth = int(input("수학점수를 입력하세요"))
total = kor+eng+math
avg = total/3

print("%s\t%d\t%dt\t%d\t%d\t%d\t%f" % (name,kor,eng,math,total,avg))
