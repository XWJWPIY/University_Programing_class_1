

n = int(input())
d = int(input())
pair_list = ['(', ')', '{', '}', '[', ']']

for i in range(n):
    temp_str = input()
    deep_chars = [""]
    deep_sign = []
    now_deep = 0
    correct = True

    while (len(temp_str) > 0):
        if (temp_str[0] == '(' or temp_str[0] == '{' or temp_str[0] == '['):
            now_deep += 1
            deep_sign.append(temp_str[0])
            if (len(deep_chars) >= now_deep):
                deep_chars.append("")
            temp_str = temp_str[1:]
            continue
        
        elif (temp_str[0] == ')' or temp_str[0] == '}' or temp_str[0] == ']'):
            if (now_deep == 0):
                correct = False
                break
            if (pair_list[pair_list.index(temp_str[0]) - 1] == deep_sign[-1]):
                deep_sign.pop(-1)
                now_deep -= 1
                temp_str = temp_str[1:]
                continue
            else:
                correct == False
                break
        
        deep_chars[now_deep] += temp_str[0]
        temp_str = temp_str[1:]
    
    if (now_deep == 0 and correct == True):
        print("pass, ",end = "")

        if (deep_chars[d] != ""):
            print(deep_chars[d])
        else:
            print("EMPTY")
    else:
        print("fail")

        

