# 測資二 第18台無人機座標輸入與輸出不同
import math

def get_first(a: list):
    return a[0]

drive = []
distance_and_pairs = []

n = int(input())

for i in range(n):
    temp = input().split()
    drive.append([int(temp[1]), int(temp[2]), int(temp[3])])

for i in range(n):
    for j in range(i + 1, n):
        distance = math.sqrt((drive[i][0] - drive[j][0]) ** 2 + (drive[i][1] - drive[j][1]) ** 2 + (drive[i][2] - drive[j][2]) ** 2)
        distance_and_pairs.append([distance, [i, j]])

distance_and_pairs.sort(key = get_first, reverse= False)

for i in range(3):
    drive1 = distance_and_pairs[i][1][0]
    drive2 = distance_and_pairs[i][1][1]

    print("%d %d " %(drive1 + 1, drive2 + 1), end = "")
    print("%s %s"  %(" ".join(map(str,drive[drive1])), " ".join(map(str,drive[drive2]))))
