
def G(n: int, k: int):
    if (n == 1):
        return str(k)
    elif (k < 2 ** (n - 1)):
        return "0" + G(n - 1, k)
    else:
        return "1" + G(n - 1, 2 ** n - 1 - k)
        
ans = []

while (True):
    temp = input()
    if (temp == "-1"):
        break
    n, k = int(temp.split()[0]), int(temp.split()[1])
    the_ans = G(n, k)
    the_ans = "0" * (n - len(the_ans)) + the_ans
    ans.append(the_ans)

for i in ans:
    print(i)
