import stuFunc

while True:
    stuFunc.Rander_Menu()
    choice = int(input("원하는 번호를 입력하세요.>> "))
    if choice == 1:   #학생성적입력
        stuFunc.Input_data()
    elif choice == 2: #학생성적출력
       stuFunc.Render_stus()
    elif choice == 3: #학생성적수정
        stuFunc.Modify_stus()
    elif choice == 4: #학생성적삭제
        stuFunc.Del_Stus()
    elif choice == 0: #프로그램종료
        print("[ 프로그램을 종료합니다. ]")
        print()
        break