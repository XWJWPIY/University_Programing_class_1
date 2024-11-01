name = []
point = []

for i in range(2):
    name.append(input())
    total = 0
    for j in range(3):
        temp = input()
        
        if ('2' <= temp <= '9'):
            total += eval(temp)
        else:
            total += 0.5
    if (total > 10.5):
        total = 0
    point.append(total)

if (point[0] == 0):
    print("%s Win" %name[1])
elif (point[0] > point[1]):
    print("%s Win" %name[0])
elif (point[0] < point[1]):
    print("%s Win" %name[1])
else:
    print("Tie")

if (point[0] > point[1]):
    print("%s Win" %name[0])
elif (point[0] < point[1]):
    print("%s Win" %name[1])
else:
    print("Tie")
        
    