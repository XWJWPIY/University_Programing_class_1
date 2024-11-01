
def triangle_1(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("#", end = "")
        for j in range(2 * i + 1):
            print("*", end = "")
        for j in range(n - i - 1):
            print("#", end = "") 
        print()

def triangle_2(n):
    for i in range(n):
        for j in range(i):
            print("#", end = "")
        for j in range(n - i):
            print("*", end = "")
        for j in range(n - i - 1 , 0, -1):
            print("*", end = "")
        for j in range(i):
            print("#", end = "") 
        print()

def diamond_and_fish(n, type):
    for i in range(n):
        if (i <= n // 2):
            for j in range(n // 2 - i):
                print(" ", end = "")
            for j in range(2 * i + 1):
                print("*", end = "")
            for j in range(n // 2 - i):
                print(" ", end = "")
            if (type == 4):
                for j in range(n // 2 - i):
                    print(" ", end = "")
                for j in range(i):
                    print("-", end = "")
        else:
            for j in range(i - n // 2):
                print(" ", end = "")
            for j in range(n - (i - n // 2)* 2):
                print("*", end = "")
            for j in range(i - n // 2):
                print(" ", end = "")
            if (type == 4):
                for j in range(i - n // 2):
                    print(" ", end = "")
                for j in range(n - i - 1):
                    print("-", end = "")
        print()

c = int(input())
n = int(input())

if (not(0 < n < 50)):
    print("error")
elif (n % 2 == 0):
    print("error")
else:
    if (c == 1):
        triangle_1(n)
    elif (c == 2):
        triangle_2(n)
    elif (c == 3):
        diamond_and_fish(n, 3)
    elif (c == 4):
        if (n == 1):
            print("error")
        else:
            diamond_and_fish(n, 4)
