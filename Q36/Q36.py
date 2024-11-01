
def get_length(var: list):
    return len(var)

def get_min_distance(dictionary: dict, start: str, end: str, break_points: list):
    points = [x for x in dictionary]
    min_distance = ["Temp"]
    ans = "-1"

    while (len(min_distance) > 0):
        if (points.count(start) > 0):
            min_distance = []
            for j in dictionary[start]:
                min_distance.append([start, j])
            points.remove(start)
            continue

        min_distance.sort(key=get_length, reverse=True)

        if (min_distance[0][-1] == end):
            if (len(min_distance[0]) < len(ans) or (ans == "-1")):
                check = 0
                for i in break_points:
                    if (i in min_distance[0]):
                        check = 1
                        break
                if (check == 1):
                    ans = min_distance[0]
            min_distance.pop(0)
            continue
        
        if (min_distance[0][-1] in dictionary):
            for i in dictionary[min_distance[0][-1]]:
                again = False
                for j in min_distance[0]:
                    if (j == i):
                        again = True
                        break
                if (again == False):
                    temp_distance_list = min_distance[0].copy()
                    temp_distance_list.append(i)
                    min_distance.append(temp_distance_list)

            min_distance.pop(0)
            continue
        min_distance.pop(0)

    if (ans == "-1"):
        return (0, "No")

    the_break_point = 0
    for i in range(len(ans)):
        if (break_points.count(ans[i]) == 1 and the_break_point == 0):
            the_break_point = ans[i]
        ans[i] = str(ans[i])
    ans = " ".join(ans)
    return (the_break_point, ans)

def func():
    dictionary = {}
    n, start, end= map(int, input().split())
    break_points = input()
    if (break_points.count(' ') > 0):
        break_points = break_points.split(' ')
        for i in range(len(break_points)):
            break_points[i] = int(break_points[i])
    else:
        break_points = [int(break_points)]
    for i in range(n):
        temp = input().split(' ')
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        if (not (temp[0] in dictionary)):
            dictionary[temp[0]] = []
        if (not (temp[1] in dictionary)):
            dictionary[temp[1]] = []
        dictionary[temp[0]].append(temp[1])
        dictionary[temp[1]].append(temp[0])
    
    show_break_points, ans = get_min_distance(dictionary, start, end, break_points)
    if (ans == "No"):
        print("No")
    else:
        print(show_break_points)
        print(ans)

func()

