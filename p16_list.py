#이름, 국어, 영어, 수학, 합계, 평균

stus =[]
# 3명의 학생성적을 입력받아 stus에 모두 저장하여 출력하시오.

name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요"))
eng = int(input("영어점수를 입력하세요"))
math = int(input("수학점수를 입력하세요"))
total = kor+eng+math
avg = total/3

stu_data=[name,kor,eng,math,total,avg]
stus.append(stu_data)
print("국어: %d\t영어: %d\t수학: %d"%(stu_data[1],stu_data[2],stu_data[3]))
print("합계 : ",int(kor+eng+math))
print("평균 : ",float((kor+eng+math)/3))

name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요"))
eng = int(input("영어점수를 입력하세요"))
math = int(input("수학점수를 입력하세요"))
total = kor+eng+math
avg = total/3

stu_data=[name,kor,eng,math,total,avg]
stus.append(stu_data)
print("국어: %d\t영어: %d\t수학: %d"%(stu_data[1],stu_data[2],stu_data[3]))
print("합계 : ",int(kor+eng+math))
print("평균 : ",float((kor+eng+math)/3))

name = input("이름을 입력하세요")
kor = int(input("국어점수를 입력하세요"))
eng = int(input("영어점수를 입력하세요"))
math = int(input("수학점수를 입력하세요"))
total = kor+eng+math
avg = total/3

stu_data=[name,kor,eng,math,total,avg]
stus.append(stu_data)
print("국어: %d\t영어: %d\t수학: %d"%(stu_data[1],stu_data[2],stu_data[3]))
print("합계 : ",int(kor+eng+math))
print("평균 : ",float((kor+eng+math)/3))

print(stus)

print(stus[0])
print(stus[0][1])
