# 撤選率小數?

# courses key 課程代碼/ key 年度/ key 學生 : Value 分數
# students key 學號 / key 課程代碼 / key 開課年度 / value 是否退選(徹選 True)

def remove_point(a: float):
    return int(a)

def remove_point_plus(a: float):
    if (int(a) != a):
        return int(a) + 1
    return int(a)

def get_average(var: dict):
    return var[1]

def get_second(var: dict):
    return var[1]

def student_id(var: list):
    return var[0]

def get_class_id(var: list):
    return var[0]

def group_getting(courses: dict):
    # [學號, 總積分, 學分加權, 總課數, 撤選數]
    students_total = {}
    
    for class_id in courses:
        for class_year_m in courses[class_id]:
            for the_student in courses[class_id][class_year_m]:
                group = the_student[3:6]
                apply_year = the_student[0:3]
                class_year = class_year_m[0:3]
                score = courses[class_id][class_year_m][the_student]
                point = int(class_id[-1])
                get_back = 0
                if (score < 0):
                    get_back = 1
                    score = 0
                    point = 0
                if (not (group in students_total)):
                    students_total[group] = {}
                if (not (apply_year in students_total[group])):
                    students_total[group][apply_year] = {}
                if (not (class_year in students_total[group][apply_year])):
                    students_total[group][apply_year][class_year] = []
                list_test = False
                for j in range(len(students_total[group][apply_year][class_year])):
                    if (students_total[group][apply_year][class_year][j][0] == the_student):
                        list_test = True
                if (list_test == False):
                    students_total[group][apply_year][class_year].append([the_student, point * score, point, 1, get_back])
                else:
                    index = 0
                    for i in range(len(students_total[group][apply_year][class_year])):
                        if (students_total[group][apply_year][class_year][i][0] == the_student):
                            index = i
                    students_total[group][apply_year][class_year][index][1] += point * score
                    students_total[group][apply_year][class_year][index][2] += point
                    students_total[group][apply_year][class_year][index][3] += 1
                    students_total[group][apply_year][class_year][index][4] += get_back
    # [學號, 總積分, 學分加權, 總課數, 撤選數] -> [學號, 平均, 系排%數, 總課數, 撤選率]
    for group in students_total:
        for apply_year in students_total[group]:
            for class_year in students_total[group][apply_year]:
                temp_student = students_total[group][apply_year][class_year]
                for i in range(len(temp_student)):
                    if (temp_student[i][2] == 0):
                        temp_student[i][1] = 0
                    else:
                        temp_student[i][1] = remove_point(temp_student[i][1] / temp_student[i][2])
                    
                    temp_student[i][-1] = int(temp_student[i][4] / temp_student[i][3] * 100)
                    
                students_total[group][apply_year][class_year].sort(key = student_id, reverse = False)
                students_total[group][apply_year][class_year].sort(key = get_average, reverse = True)

                students_number = len(temp_student)
                rank = 0

                for j in range(101):
                    while (remove_point_plus(students_number * 0.01 * j) > rank):
                        students_total[group][apply_year][class_year][rank][2] = j
                        rank += 1
                    if (rank == 3):
                        students_total[group][apply_year][class_year] = temp_student[0:3]
                        break

    return students_total

def print_group_course(students_total: list):
    group_list = []
    apply_year_list = []
    class_year_list = []

    for i in students_total:
        if (group_list.count(i) == 0):
            group_list.append(i)
        for j in students_total[i]:
            if (apply_year_list.count(j) == 0):
                apply_year_list.append(j)
            for k in students_total[i][j]:
                if (class_year_list.count(k) == 0):
                    class_year_list.append(k)
    
    group_list.sort()
    apply_year_list.sort()
    class_year_list.sort()

    for i in group_list:
        for j in apply_year_list:
            if (not (j in students_total[i])):
                continue
            for k in class_year_list:
                if (not (k in students_total[i][j])):
                    continue
                print("%s %s %s" %(i, j, k))
                for m in students_total[i][j][k]:
                    print("%s %s %s %s" %(m[0], str(m[1]), str(m[2]) + "%", str(m[-1]) + "%"))
    return

def class_getting(course: list, class_num: str):
    class_total = {}
    class_pointer = ["A", "B"]
    count_pointer = []
    

    for class_id in course:
        class_total[class_id] = {}
        total_score = 0
        len_num = 0
        back_num = 0
        max_num = 0
        min_num = 100
        all_sample = []
        for class_year_m in course[class_id]:
            class_year = class_year_m[0:3]
            class_total[class_id][class_year] = []
            temp_student = class_total[class_id][class_year] # 用 temp_total 作為內部指標的代替物
            total_score = 0
            len_num = 0
            back_num = 0
            max_num = 0
            min_num = 100
            
            for student in course[class_id][class_year_m]:
                score = course[class_id][class_year_m][student]
                
                len_num += 1
                if (score == -1):
                    back_num += 1
                else:
                    total_score += score
                    if (score > max_num):
                        max_num = score
                    if (score < min_num):
                        min_num = score
                
                if (class_id == class_num):
                    remember = False
                    for i in range(len(count_pointer)):
                        if (count_pointer[i][0] == student[3:6]):
                            count_pointer[i][1] += 1
                            remember = True
                    if (remember == False):
                        count_pointer.append([student[3:6], 1])

                temp_student.append([student, score])
                all_sample.append([student, score])

            temp_student.sort(key = student_id)
            temp_student.sort(key = get_second, reverse = True)
            
            rank = 0

            for j in range(101):
                while (remove_point_plus((len_num) * 0.01 * j) > rank):
                    class_total[class_id][class_year][rank].append(j)
                    rank += 1
                if (rank == 3):
                    class_total[class_id][class_year] = temp_student[0:3]
                    break

            class_total[class_id][class_year].append(["Average", max_num, int(total_score / (len_num - back_num)), min_num, int(back_num / len_num * 100)])
        

        if (class_id == class_num):
            all_sample.sort(key = student_id)
            all_sample.sort(key = get_second, reverse = True)
            class_pointer[0] = all_sample[0][0]
            class_pointer[1] = all_sample[1][0]
        
    count_pointer.sort(key = get_class_id, reverse = False)
    count_pointer.sort(key = get_second, reverse = True)
    max_count = count_pointer[0][1]
    index = 0

    while (index < len(count_pointer) and index < 2):
        class_pointer.append(count_pointer[index][0])
        index += 1

    return (class_total, class_pointer)

def print_class_course(class_total: dict):
    class_name = []
    year = []

    for i in class_total:
        if (class_name.count(i) == 0):
            class_name.append(i)
        for j in class_total[i]:
            if (year.count(j) == 0):
                year.append(j)
    
    class_name.sort()
    year.sort()

    for i in class_name:
        for j in year:
            if (not (j in class_total[i])):
                continue
            print("%s %s" %(i, j))
            temp = class_total[i][j][-1]
            print("%s %s %s %s" %(str(temp[1]), str(temp[2]), str(temp[3]), str(temp[4]) + "%"))
            for m in range(len(class_total[i][j]) - 1):
                temp = class_total[i][j][m]
                print("%s %s %s" %(temp[0], str(temp[1]), str(temp[2]) + "%"))
    return

def print_point(ans_list: list):
    print(" ".join(ans_list))
    return

def func():
    n = int(input())

    courses = {}

    for i in range(n):
        temp = input().split()
        class_id = temp[0]
        class_year = temp[1]
        if (class_id not in courses):
            courses[class_id] = {}
        courses[class_id][class_year] = {}
        student_num = int(temp[2])

        for j in range(student_num):
            temp2 = input().split(" ")
            score = 0

            if (len(temp2) == 3):
                score = int(temp2[1]) * 0.7 + int(temp2[2]) * 0.3
                if (int(score) != score):
                    score = int(score) + 1
                else:
                    score = int(score)
            elif (temp2[1] == "w"):
                score = -1
            else:
                score = int(temp2[1])
            


            the_student = temp2[0]

            if (not (the_student in courses[class_id][class_year])):
                courses[class_id][class_year][the_student] = score
    

    search_course = input()

    students_total = group_getting(courses)
    print_group_course(students_total)
    class_total, class_pointer = class_getting(courses, search_course)
    print_class_course(class_total)
    print_point(class_pointer)



func()