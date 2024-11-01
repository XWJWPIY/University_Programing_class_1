
def get_second(var: list):
    return var[1]

dictionary = {}

temp = input().split(" ")
n, k = int(temp[0]), int(temp[1])
ans = [[[k], 0]]
value = 0

for i in range(n):
    temp = input().split(" ")
    dictionary[int(temp[0])] = [[int(temp[2]), int(temp[3])], int(temp[1])]

while (len(ans) != 0):
    temp_point_index = ans[0]
    end_num = temp_point_index[0][-1]
    ans[0][1] += dictionary[ans[0][0][-1]][1]
    for i in dictionary[end_num][0]:
        if (i != 0 and temp_point_index[0].count(i) == 0):
            temp_list = temp_point_index[0].copy()
            temp_list.append(i)
            ans.append([temp_list, temp_point_index[1]])
    
    if (value < temp_point_index[1]):
        value = temp_point_index[1]
    ans.pop(0)
    ans.sort(key = get_second, reverse=False)

print(value)
