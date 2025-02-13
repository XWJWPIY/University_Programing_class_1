
def main():
    begin = input()
    wrong = False
    if (len(begin) != 4 or begin[0] != "A" or begin[-1] != "G"):
        wrong = True
    elif (not("E" <= begin[1] <= "T") or not("E" <= begin[2] <= "T")):
        wrong = True

    temp = input()
    final = temp.split(" ")

    test = input()

    if (wrong):
        print("No gene")
        return
    
    ans_list = []
    temp_list = []
    protect = 3

    for i in range(len(test)):
        if (i < 3):
            continue
        for j in range(len(temp_list)):
            temp_list[j] += test[i]
            protect -= 1
        if (test[i - 3:i + 1] in begin):
            temp_list.append("")
            protect = 3
        # print(temp_list)
        if (test[i - 2:i + 1] in final and protect <= 0):
            temp_list.sort(key = lambda x :len(x), reverse= True)
            for j in temp_list:
                flag = False
                for k in range(2, len(j) - 3):
                    if ((len(j) - 3) % k == 0):
                        flag = True
                        break
                if (flag == False):
                    ans_list.append(j[:len(j) - 3])
                    break
            temp_list = []
    ans_list.sort()
    ans_list.sort(key = lambda x : len(x))

    if (len(ans_list) == 0):
        print("No gene")
    else:
        for i in ans_list:
            print(i)
                
        

main()