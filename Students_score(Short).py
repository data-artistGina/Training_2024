students = []
subj = ['','국어','영어','수학학']
stu_num = 1

while True:
    print("-"*50)
    print("학생성적프로그램")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적검색")
    print("4. 성적수정")
    print("5. 등수처리")
    print("6. 성적삭제")
    print("0. 프로그램종료")
    print("-"*50)

    choice = input("원하는 번호를 입력하세요 >> ")
    if choice == "1":
        while True:
            print("성적입력을 선택하였습니다 >>")
            stu = []
            name = input("학생의 이름을 입력하세요(-1.취소) >> ")
            if name == "-1":
                break
            kor = int(input("국어성적을 입력하세요 >> "))
            eng = int(input("영어성적을 입력하세요 >> "))
            math = int(input("수학성적을 입력하세요 >> "))
            total = kor + eng + math
            avg = f'{total/3:.2f}'
            rank = 1
            stu.append(stu_num)
            stu.append(name)
            stu.append(kor)
            stu.append(eng)
            stu.append(math)
            stu.append(total)
            stu.append(avg)
            stu.append(rank)
            students.append(stu)
            stu_num += 1
            print(stu)

    elif choice == "2":
        print("성적출력을 선택하였습니다")
        choice = input("출력하시겠습니까? (1.출력 , 0.취소)")
        if choice == "0":
            break
        else:
            print("-"*50)
            print("학생성적 출력")
            print("-"*50)
            print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
            for stu in students:
                for elem in stu:
                    print(elem,end='\t')
                print()
                    
    elif choice == "3":
        print("학생성적 검색을 선택하셨습니다.")
        search = input("찾고자 하는 학생의 이름을 입력하세요(-1.취소) >> ")
        chk = 0
        if search == "-1":
            break
        for stu in students:
            if search != stu[1]:
                chk += 1 
            else:
                print("{} 학생의 이름이 존재합니다. {} 학생의 성적은 {}입니다.".format(search,search,students[chk]))

    elif choice == "4":
        print("학생성적 수정을 선택하셨습니다.")
        search = input("수정할 학생의 이름을 입력하세요(-1.취소) >> ")
        chk = 0
        if search == "-1":
            break
        for stu in students:
            if search != stu[1]:
                chk += 1 
            else:
                print("{} 학생의 이름이 존재합니다. {} 학생의 성적은 {}입니다.".format(search,search,students[chk]))
        while True:
            print("-"*50)
            print("1.국어성적")
            print("2.영어성적")
            print("3.수학성적")
            print("-"*50)
            choice = int(input("원하는 과목을 선택하세요"))
            print("{} 과목을 선택하였습니다".format(subj[choice]))
            cor = input("{}의 {}을 수정하시겠습니까?(1.수정, 0.취소) >> ".format(search,subj[choice]))
            if cor == "0":
                break
            else:
                change = int(input("수정할 성적을 입력하세요 >> "))
                students[chk][choice+1] = change
                students[chk][5] = students[chk][choice+1] + students[chk][choice+2] + students[chk][choice+3]
                students[chk][6] = f'{students[chk][5]/3:.2f}'
                print("성적 수정이 완료되었습니다")
                print(students[chk])

    elif choice == "5":
        print("등수처리를 선택하셨습니다.")
        choice = input("등수처리를 진행하시겠습니까? (1.선택, 0.취소) >>")
        if choice == "0" :
            break
        else:
            for stu in students:
                rank_cnt = 1
                for comp in students:
                    if stu[5] < comp[5]:
                        rank_cnt += 1
                    stu[7] = rank_cnt

    elif choice =="6":
        print("성적삭제를 선택하였습니다")
        search = input("찾고자 하는 학생의 이름을 입력하세요(-1.취소) >> ")
        chk = 0
        if search == "-1":
            break
        for stu in students:
            if search != stu[1]:
                chk += 1 
            else:
                print("{} 학생의 이름이 존재합니다.".format(search))
                confirm = input("삭제하시겠습니까?(1.삭제, 0.취소) >>")
                if confirm == "0":
                    break
                else:
                    del students[chk]
                    print("삭제가 완료되었습니다.")

    elif choice == "0":
        print("프로그램을 종료합니다")
        break