book_prise = [0] * 3
book_type = ["A", "B", "C"]
normal = [380, 1200, 180]

for i in range(3):
    amount, discount_1, discount_2, discount_3 = eval(input())
    book_prise[i] = amount * normal[i]
    if (amount <= 10):
        book_prise[i] *= 1
    elif (amount <= 20):
        book_prise[i] *= (discount_1 / 100)
    elif (amount <= 30):
        book_prise[i] *= (discount_2 / 100)
    else:
        book_prise[i] *= (discount_3 / 100)

    if (int(book_prise[i]) != book_prise[i]):
        book_prise[i] = int(book_prise[i]) + 1

total = int(sum(book_prise))
for i in range(3):
    max_num = max(book_prise)
    index = book_prise.index(max_num)
    print("%s,%d" %(book_type[index], max_num))
    book_prise.pop(index)
    book_type.pop(index)

print(total)
