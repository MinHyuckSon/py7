# stu_list=[]
f= open("c:/download/aaa.txt","r")
while True:
    txt = f.readline()
    if txt == "":break
    import ast
    t_dic = ast.literal_eval(txt)
#딕셔너리 형태 변경
    t_dic = "{stu_list[0][stuNum]}",{stu_list[0][stuName]},{stu_list[0][stuKor]},\
            {stu_list[0][stuEng]},{stu_list[0][stuMath]},{stu_list[0][stuTotal]},\
            {stu_list[0][stuAvg]}

# f= open("c:/download/aaa.txt","w",encoding="utf-8")
# stu_str = ""
# for i in range(len(stu_list)):
#     stu_str += f"{stu_list[]}"