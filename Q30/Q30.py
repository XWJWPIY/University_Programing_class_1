def binary_to_decimal(bi_string: str) -> int:
    power = 0
    total = 0
    for i in range(len(bi_string) - 1, -1, -1):
        total += int(bi_string[i]) * (2 ** power)
        power += 1
    return total

def decimal_to_binary(num: int) -> str:
    power = 0
    total_list = []
    for i in range(14):
        total_list.append(str(num % 2))
        num //= 2

    return ''.join(reversed(total_list))

"""
C(0)與C(1)得到的反饋 R(0)與R(1)皆為0
而 C(2) = C(0) 得到的反饋為 R(2) = 1
C(3) = C(2) = C(0) , R(3) = 2 = 1 + R((3 + 1) // 2) = 1 + R(2)
C(4) = C(2) = C(0) , R(4) = 2 = 1 + R((4 + 1) // 2) = 1 + R(2)
C(5) = C(3) = C(2) = C(0), R(5) = 3 = 1 + R((5 + 1) // 2) = 1 + R(3)
...
C(n) = C((n+1) // 2), R(n) = 1 + R((n + 1) // 2)
"""

r = [0, 0] # R(0) 與 R(1)
ans = []

while (True):
    n = input()
    if (n == "-1"):
        break

    num = binary_to_decimal(n)
    for i in range(len(r), num + 1):
        r.append(1 + r[(i + 1) // 2])

    ans.append(decimal_to_binary(sum(r[0:num + 1])))

for i in ans:
    print(i)


