import math

a = int(input())
b = int(input())
c = int(input())

D = b ** 2 - 4 * a * c # 判別式

if (D >= 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("%.1f" %(x1))
    print("%.1f" %(x2))

else:
    x_r = -b / (2 * a) # x1, x2 實部相同，用 x_r 取代
    x_i = math.sqrt(-D) / (2 * a) # x1, x2 係數相同，僅差正負，用 x_i 取代係數值
    print("%.1f+%.1fi" %(x_r, x_i))
    print("%.1f-%.1fi" %(x_r, x_i))
