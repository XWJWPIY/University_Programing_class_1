
n = int(input()) # 人口
m = int(input()) # 計算期間
a = int(input()) # 確診人數
b = float(input()) # 傳播率
c = int(input()) # 康復天數
d = float(input()) # 免疫率

protect_people = int(n * d)
unprotect_people = n - protect_people
total_cases = 0 # 累積確診數
new_cases_list = []

for i in range(m):
    recovery = 0
    new_cases = a
    if (i == 0):
        new_cases_list.append(a)
    else:
        x = (b / c) * (1 - d)
        new_cases = int(sum(new_cases_list) * x)
        if (unprotect_people < new_cases):
            new_cases = unprotect_people
        new_cases_list.append(new_cases)
        if (len(new_cases_list) > c):
            recovery = new_cases_list.pop(0)
            protect_people += recovery
            d = protect_people / n
    total_cases += new_cases
    unprotect_people -= new_cases

    print("%d %d %d %d" %(i + 1, sum(new_cases_list), new_cases, recovery))


print(total_cases)
