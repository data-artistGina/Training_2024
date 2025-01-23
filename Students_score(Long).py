students = []
stu_num = 0

while True :
    print('='*40)
    print('[학생성적프로그램]')
    print('='*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램종료')
    print('='*40)
    choice = input('원하는 번호를 입력하세요 >>')
    if not choice.isdigit():
        print('숫자를 입력하세요')
        continue
    choice = int(choice)

    if choice == 1:
        print('학생성적입력을 선택하셨습니다')
        while True :
            name = input('학생이름을 입력하세요(-1. 종료) >>')
            if name == '-1':
                print('학생 성적 입력을 취소합니다.')
                break
            student = {}
            student["stuNo"] = stu_num+1
            student["name"] = name
            kor = int(input('국어성적 >>'))
            student["kor"] = kor
            eng = int(input('영어성적 >>'))
            student["eng"] = eng
            math = int(input('수학성적 >>'))
            student["math"] = math
            total = kor + eng + math
            student["total"] = total
            avg =  total/3
            student["avg"] = float('{:.2f}'.format(avg))
            student["rank"] = 1
            students.append(student)
            print(students)
            stu_num += 1
    
    elif choice == 2:
        print('학생성적전체출력을 선택하셨습니다.')
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*50)
        for stu in students :
            for elem in stu :
                print(stu[elem],end='\t')
            print()

    elif choice == 3:
        print('학생검색을 선택하셨습니다')
        print('-'*50)
        print('1. 이름검색')
        print('2. 총점이상')
        print('3. 총점이하')
        print('-'*50)
        choice = input('검색조건을 선택하세요 >>')

        search_students = []
        if choice == '1':
            print('이름 검색을 선택하셨습니다')
            search_name = input('검색하고자 하는 학생의 이름을 입력하세요 (-1. 취소)')
            if search_name == '-1':
                break
            search_cnt = 0
            for stu in students:
                if stu['name'].find(search_name) != -1 :
                    search_students.append(students[search_cnt])
                search_cnt += 1
                if len(students) == search_cnt:
                    break 
        elif choice == '2':
            print('총점 이상을 선택하셨습니다')
            search_score = int(input('검색하고자 하는 성적기준을 입력하세요 (-1. 취소)'))
            if search_score == '-1':
                break
            search_cnt = 0
            for stu in students:
                if stu['total'] >= search_score:
                    search_students.append(students[search_cnt])
                search_cnt += 1
                if len(students) == search_cnt:
                    break 
        elif choice == '3':
            print('총점 이하를 선택하셨습니다')
            search_score = int(input('검색하고자 하는 성적기준을 입력하세요 (-1. 취소)'))
            if search_score == '-1':
                break
            search_cnt = 0
            for stu in students:
                if stu['total'] <= search_score:
                    search_students.append(students[search_cnt])
                search_cnt += 1
                if len(students) == search_cnt:
                    break 
        print('-'*50)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*50)
        for stu in search_students :
            for elem in stu :
                print(stu[elem],end='\t')
            print()

    elif choice == 4:
        print('학생수정을 선택하셨습니다')
        chk = 0
        count = 0
        search_name = input('수정하고자 하는 학생의 이름을 입력하세요 >> ')
        if search_name == '0':
            break
        for stu in students :
            if search_name == stu["name"]:
                print('{}, 학생이 명단에 있습니다'.format(search_name))
                chk = 1
                break
            count += 1
        
        if chk == 1:
            print('-'*50)
            print("1. 국어성적")
            print("2. 영어성적")
            print("3. 수학성적")
            print('-'*50)
            cor_sub = input('수정하고자 하는 과목을 선택해 주세요(0.취소)')
            if cor_sub == '0':
                break
            cor_sub = int(cor_sub)
            if  cor_sub == 1:
                print('{}를 선택하셨습니다.'.format(s_title))
                print('{}의 국어 성적은 현재 {}점 입니다.'.format(search_name,students[count]["kor"]))
                c_kor = int(input('수정할 국어 성적을 입력하세요 >>'))
                students[count]["kor"] = c_kor
                print('{} 학생의 국어 성적이 {}점으로 수정되었습니다.'.format(search_name,c_kor))
                students[count]["total"] = students[count]["kor"]+students[count]["eng"]+students[count]["math"]
                students[count]["avg"] = students[count]["total"]/3
                print(students[count])
            elif cor_sub == 2:
                print('영어를 선택하셨습니다.')
                print('{}의 영어 성적은 현재 {}점 입니다.'.format(search_name,students[count]["eng"]))
                c_eng = int(input('수정할 영어 성적을 입력하세요 >>'))
                students[count]["eng"] = c_eng
                print('{} 학생의 영어 성적이 {}점으로 수정되었습니다.'.format(search_name,c_eng))
                students[count]["total"] = students[count]["kor"]+students[count]["eng"]+students[count]["math"]
                students[count]["avg"] = students[count]["total"]/3
                print(students[count])
            elif cor_sub == 3:
                print('수학을 선택하셨습니다.')
                print('{}의 수학 성적은 현재 {}점 입니다.'.format(search_name,students[count]["math"]))
                c_math = int(input('수정할 수학 성적을 입력하세요 >>'))
                students[count]["math"] = c_math
                print('{} 학생의 수학 성적이 {}점으로 수정되었습니다.'.format(search_name,c_math))
                students[count]["total"] = students[count]["kor"]+students[count]["eng"]+students[count]["math"]
                students[count]["avg"] = students[count]["total"]/3
                print(students[count])
    elif choice == 5:
        print("등수처리를 선택하셨습니다")
        for stu in students:
            rank_cnt = 1
            for comp in students:
                if stu["total"] < comp["total"]:
                    rank_cnt += 1
            stu["rank"] = rank_cnt
        print("등수처리가 완료되었습니다.")
        print(students)
        
    elif choice == 6:
        print("학생삭제를 선택하셨습니다.")
        while True:
            search = input("삭제하고자 하는 학생의 이름을 입력하세요 (-1.취소)>> ")
            if search == "-1":
                break
            chk = 0
            for stu in students:
                if search == stu["name"]:
                    break
                chk += 1
            if chk >= len(students):
               print("찾고자 하는 학생이 없습니다.")
            else: 
                print("{} 학생을 찾았습니다.".format(search))
                ask = input("{} 학생의 성적을 삭제하시겠습니까?(1.삭제, 0.취소)".format(search))
                if ask == "1":
                    del students[chk]
                    print("삭제되었습니다.")
                    re_ask = input("삭제된 명단을 확인하시겠습니까?(1.확인, 0.취소)")
                    if re_ask == "1":
                        print("학생성적 출력")
                        print("-"*50)
                        print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
                        for stu in students:
                            for elem in stu:
                                print(stu[elem],end="\t")
                            print()           
                elif ask == "0":
                    print("취소되었습니다.")
                    break
                else:
                    print("잘못 선택하였습니다. 다시 선택해주세요")


    elif choice == 0:
        print('프로그램을 종료합니다')
        break
