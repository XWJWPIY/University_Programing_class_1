import math

def getTriangle(a, b, c):
    if (a + b + c < abs(a) + abs(b) + abs(c)): #邊長若有負值，三者合必小於三者各取絕對值後的合
        return 1 #有負值邊長的組合不再繼續運算
    if (a == 0): #已排除負值，有0的邊長組，0必為最小的整數，會被排在[0]
        return 1 #有邊長為 0 的組合不再繼續運算
    if (a + b <= c): # 兩短邊合小於等於第三邊長
        return 1 
    
    if ((a == b) and (b == c)): # 若3邊同時等長
        return 2 #回傳正三角
    
    elif (b == c): #處理[小, 大, 大]組合
        return 3 #回傳等腰三角形
    
        """
        條件為任兩邊相等，且平方和大於第三邊的平方。
        若要等腰的兩邊平方和大於第三邊的平方，
        代表等腰的兩邊長夾角必須要是銳角。
        最長兩邊等長的三角形，平方合必大於第三邊平方
        """

    elif (a == b): #處理[小, 小, 大]組合
        if (a ** 2 + b ** 2 > c ** 2):
            return 3

            """
            條件為任兩邊相等，且平方和大於第三邊的平方。
            若要等腰的兩邊平方和大於第三邊的平方，
            代表等腰的兩邊長夾角必須要是銳角。
            最短兩邊等長的三角形，夾角可能非銳角(ex: [6, 5, 5])
            需要進行計算
            """

    if (a ** 2 + b ** 2 < c ** 2): # 排除頓角三角形
        return 4
    elif (a ** 2 + b ** 2 > c ** 2): # 排除銳角三角形
        return 5
    # 排除後僅剩直角三角形
    return 6



length = [0, 0, 0] # 三邊長
# tri_list 為三角形種類([0]項僅為方便後方種類的索引值與題目種類編號對其)
tri_list = ["", "not a", "equilateral", "isosceles", "obtuse", "acute", "right"]
ans = []

n = int(input())
max_area = -1
min_area = -1
not_triangle = 0

for i in range(n):
    length = input().split()
    for j in range(3):
        length[j] = int(length[j])

    length.sort() # 邊長由小到大排列
    type = getTriangle(length[0], length[1], length[2])
    
    if (type == 1):
        # print("%s triangle" %tri_list[type])
        ans.append("%s triangle" %tri_list[type])
        not_triangle += 1
        continue
    
    s = sum(length) / 2
    area = math.sqrt(s * (s - length[0]) * (s - length[1]) * (s - length[2]))
    area = int(area * 1000)
    if (area % 10 >= 5):
        area = area - area % 10 + 10
    else:
        area = area - area % 10
    area /= 1000

    if (max_area == -1 or max_area < area):
        max_area = area
    if (min_area == -1 or 0 <= area < min_area):
        min_area = area
    
    # print("%s triangle %.2f" % (tri_list[type], area))
    ans.append("%s triangle %.2f" % (tri_list[type], area))

for i in ans:
    print(i)

if (not_triangle == n):
    print("All inputs are not triangles!")
else:
    print("%.2f" %max_area)
    print("%.2f" %min_area)

