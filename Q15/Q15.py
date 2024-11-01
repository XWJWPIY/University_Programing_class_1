
# 四捨六入五看偶規則
def float_process(num):
    num = int(num * 1000)
    if (num % 10 > 5):
        num = num - num % 10 + 10
        return num / 1000
    elif (num % 10 < 5):
        num = num - num % 10
        return num / 1000
    elif (num % 20 == 15):
        num = num + 5
        return num / 1000
    else:
        num = num - 5
        return num / 1000


n = int(input())
bmi_list = []

for i in range(n):
    temp_data = input().split(" ")
    temp_data[0], temp_data[1] = eval(temp_data[0]), eval(temp_data[1])
    bmi = float_process(temp_data[1] / (temp_data[0] ** 2))
    bmi_list.append(bmi)

bmi_list.sort()

print("%.2f" % max(bmi_list))
print("%.2f" % min(bmi_list))

if (len(bmi_list) % 2 == 1):
    print("%.2f" % bmi_list[int(len(bmi_list) / 2)])
else:
    print("%.2f" % float_process((bmi_list[len(bmi_list) // 2 - 1] + bmi_list[len(bmi_list) // 2]) / 2))

ans_num = [-1, 0]
temp_num = [-1, 0]
for i in bmi_list:
    if (i == temp_num[0]):
        temp_num[1] += 1
    else:
        if (ans_num[1] < temp_num[1]):
            ans_num[0] = temp_num[0]
            ans_num[1] = temp_num[1]

        temp_num[0] = i
        temp_num[1] = 1

if (ans_num[1] < temp_num[1]):
    ans_num[0] = temp_num[0]
    ans_num[1] = temp_num[1]

print("%.2f" % ans_num[0])
