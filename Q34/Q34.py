
def get_value(var:list):
    return var[1]

def get_max_distance(dictionary: dict, start: str, end:str):
    points = [x for x in dictionary]
    max_distance = ["Temp"]
    ans = ["Start", -1]

    while (len(max_distance) > 0):
        if (points.count(start) > 0):
            max_distance = []
            for j in dictionary[start]:
                max_distance.append([start + j, dictionary[start][j]])
            points.remove(start)
            continue

        max_distance.sort(key=get_value)
        if (max_distance[0][0][-1] == end):
            if (max_distance[0][1] > ans[1]):
                ans = max_distance[0]
            max_distance.pop(0)
            continue
        
        if (max_distance[0][0][-1] in dictionary):
            for i in dictionary[max_distance[0][0][-1]]:
                again = False
                for j in max_distance[0][0]:
                    if (j == i):
                        again = True
                        break
                if (again == False):
                    max_distance.append([max_distance[0][0] + i, max_distance[0][1] + dictionary[max_distance[0][0][-1]][i]])

            max_distance.pop(0)
            continue
        max_distance.pop(0)
    
    ans_string = ""
    for i in range(len(ans[0])):
        ans_string += ans[0][i]
        if (i != len(ans[0]) - 1):
            ans_string += " "

    ans_distance = ans[1]
    return ans_string, ans_distance

def get_min_distance(dictionary: dict, start: str, end: str):
    points = [x for x in dictionary]
    min_distance = ["Temp"]
    ans = ["Start", -1]

    while (len(min_distance) > 0):
        if (points.count(start) > 0):
            min_distance = []
            for j in dictionary[start]:
                min_distance.append([start + j, dictionary[start][j]])
            points.remove(start)
            continue

        min_distance.sort(key=get_value, reverse=True)
        if (min_distance[0][0][-1] == end):
            if (min_distance[0][1] < ans[1] or (ans[1] == -1)):
                ans = min_distance[0]
            min_distance.pop(0)
            continue
        
        if (min_distance[0][0][-1] in dictionary):
            for i in dictionary[min_distance[0][0][-1]]:
                again = False
                for j in min_distance[0][0]:
                    if (j == i):
                        again = True
                        break
                if (again == False):
                    min_distance.append([min_distance[0][0] + i, min_distance[0][1] + dictionary[min_distance[0][0][-1]][i]])

            min_distance.pop(0)
            continue
        min_distance.pop(0)

    ans_string = ""
    for i in range(len(ans[0])):
        ans_string += ans[0][i]
        if (i != len(ans[0]) - 1):
            ans_string += " "

    return ans_string, (len(ans[0]) - 1)

def function():
    n = int(input())

    dictionary = {}
    
    while (True):
        temp = input()
        if (temp == "-1"):
            break
        temp = temp.split()
        if (not (temp[0] in dictionary)):
            dictionary[temp[0]] = {}
        if (not (temp[1] in dictionary[temp[0]])):
            dictionary[temp[0]][temp[1]] = int(temp[2])
        if ((temp[1] in dictionary) and (temp[0] in dictionary[temp[1]])):
            dictionary[temp[0]][temp[1]] = min(dictionary[temp[0]][temp[1]], dictionary[temp[1]][temp[0]])
            dictionary[temp[1]][temp[0]] = min(dictionary[temp[0]][temp[1]], dictionary[temp[1]][temp[0]])
    
    ans_max_string, ans_max_num = get_max_distance(dictionary, "A", "B")
    ans_min_string, ans_min_num = get_min_distance(dictionary, "A", "B")
    print(ans_min_num)
    print(ans_min_string)
    
    print(ans_max_num)
    print(ans_max_string)
    



function()