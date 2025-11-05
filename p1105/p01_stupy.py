import os

#1, 통로(stream) : 파일열기
#r: 읽기모드, w:쓰기모드, a:추가모드
# f = open("c:/download/aaa.txt","r",encoding="utf8")
# txt = f.read() #read()-속도느림, readline()-1줄, readllines()-전체
#읽기모드
#-------------------------------------------------------------------
# while True:
#     txt = f.readline()
#     if txt == "": break
#     print(txt,end="")

# f.close()
#--------------------------------------------------------------------
# #쓰기모드
# f=open("c:/download/ccc.txt","w") #파일이없으면 w:모드는 파일을 생성
# txt = input("글자를 입력하세요.>> \n")
# f.write(txt)
# # f.write("안녕하세요 김멈머입니다")
# f.close()
# print("완료!")