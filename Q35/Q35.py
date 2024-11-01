
def get_second(var: list):
    return var[1]

def match_school(property_list: list, property_dict: dict, the_need: list):
    the_need.append("+")
    match_schools = {}
    property_match = {}
    temp_match = {}
    need_count = 0

    for i in the_need:
        if (i == "+"):
            for j in temp_match:
                if (temp_match[j] == need_count):
                    if (j in match_schools):
                        match_schools[j] += temp_match[j]
                    else:
                        match_schools[j] = temp_match[j]
            temp_match.clear()
            need_count = 0

        if (i in property_dict):
            for j in property_dict[i]:
                if (j in temp_match):
                    temp_match[j] += 1
                else:
                    temp_match[j] = 1
                if (j in property_match):
                    property_match[j] += 1
                else:
                    property_match[j] = 1
            need_count += 1
    
    match_schools_list = []
    property_match_list = []

    for i in match_schools:
        match_schools_list.append(i)
    for i in property_match:
        property_match_list.append([i, property_match[i]])
    property_match_list.sort(key = get_second, reverse = True)
    most_property_num = property_match_list[0][1]
    while (property_match_list[-1][1] < most_property_num):
        property_match_list.pop(-1)

    return (match_schools_list, property_match_list)



def func():
    property_list = ["GF", "BC", "NC", "CT", "NS", "NM", "HL", "NL"]
    property_dict = {}
    for i in property_list:
        property_dict[i] = []

    n = int(input())
    for i in range(n):
        temp = input().split(" ")
        name = temp.pop(0)
        for j in temp:
            property_dict[j].append(name)

    n = int(input())
    ans_all = []
    ans_property = []
    for i in range(n):
        temp = input()
        if (temp.count(" ") > 0):
            temp = temp.split(" ")
        else:
            temp = [temp]
        temp_all, temp_property = match_school(property_list.copy(), property_dict.copy(), temp)
        ans_all.append(temp_all)
        ans_property.append(temp_property)
    
    n = int(input())
    if (n == 1):
        for temp_list in ans_property:
            for i in range(len(temp_list)):
                if (i == len(temp_list) - 1):
                    print(temp_list[i][0])
                    break
                else:
                    print(temp_list[i][0], end = " ")
                
    else:
        for temp_list in ans_all:
            print(" ".join(temp_list))

func()