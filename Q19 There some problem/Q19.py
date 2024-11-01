
# n >= 10 的顯示字元數
def graph_1(n): # 直角三角形
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end = "")
        for j in range(i , 0, -1):
            print(j, end = "")
        print()

def graph_2(n):
    for i in range(n):
        for j in range(n - i - 1):
            print("_", end = "")
        for j in range(i + 1):
            print(j + 1, end = "")
        for j in range(i , 0, -1):
            print(j, end = "")
        for j in range(n - i - 1):
            print("_", end = "") 
        print()

def graph_3(n):
    for i in range(n):
        for j in range(i):
            print("_", end = "")
        for j in range(n - i):
            print(j + 1, end = "")
        for j in range(n - i - 1 , 0, -1):
            print(j, end = "")
        for j in range(i):
            print("_", end = "") 
        print()

graph = int(input())
n = int(input())

if (graph == 1):
    graph_1(n)
elif (graph == 2):
    graph_2(n)
elif (graph == 3):
    graph_3(n)
