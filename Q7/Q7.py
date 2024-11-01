
plan = [183, 383, 983, 1283] #月租方案(費)
fee_list = [[0.08, 0.07, 0.06, 0.05], # 語音費率 網內(元/秒)
            [0.139, 0.130, 0.108, 0.100], # 語音費率 網外(元/秒)
            [0.135, 0.121, 0.101, 0.090], # 語音費率 網話(元/秒)
            [1.128, 1.128, 1.128, 1.128], # 簡訊費率 網內(元/則)
            [1.483, 1.483, 1.483, 1.483], # 簡訊費率 網外(元/則)
            [250, 200, 150, 0]] # 網路加購價(元/G)
internet_discount = [1, 3, 5, 0] # 方案附贈額度

best_plan = 0
cheapest_price = -1

data = [0, 0, 0, 0, 0, 0]
for i in range(6):
    data[i] = int(input())

for i in range(4):
    total = 0

    for j in range(6):
        if (j < 5): # [5] 對應到fee_list是網路加購價行
            total += (data[j] * fee_list[j][i])
            continue
        if (data[j] > internet_discount[i]):
            total += ((data[j] - internet_discount[i]) * fee_list[5][i])
    


    if (total < plan[i]):
        total = plan[i]
    total = int(total)

    if (cheapest_price == -1):
        cheapest_price = total
        best_plan = 0
    
    elif (total < cheapest_price):
        cheapest_price = total
        best_plan = i

print(cheapest_price)
print(plan[best_plan])

        

