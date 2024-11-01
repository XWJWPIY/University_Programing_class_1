
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
    for i in range(4):
        total_list.append(str(num % 2))
        num //= 2

    return ''.join(reversed(total_list))

def C(num: int):
    if (num == 0):
        return 0
    if (num == 1):
        return 0
    else:
        return C((num + 1) // 2) + 1

num_list = []
while (True):
    n = input()
    num_list.append(n)
    n = input()
    if (n == "-1"):
        break

for i in num_list:
    num = binary_to_decimal(i)
    count = C(num)
    print(decimal_to_binary(count))

