#990101-1111111
#870101-2111111

#070101-4111111
#1-남자,2-여자
#주민번호를 입력받아 ,남자인지 여자인지 출력하시오

import datetime

now = datetime.datetime.now()
month = now.month

strJumin = input("주민번호를 입력하세요")

iNum = int(strJumin[7])

if iNum==1:
    print("남자입니다.")
else:
    print("여자입니다.")
    
iMonth = int(strJumin[2:4])