# 測資2 連續輸出兩個空白 (改成只輸出一個)

a = input()
b = input()
x = input()
y = input()
n = abs(len(x) - len(y))


c = a + " " + b
d = ""
c_removed = ""

c_list = []
d_list = []
d_reverse_list = []

if (c.count(" ") != 0):
    c_list = c.split(" ")
else:
    c_list.append(c)

for i in c_list:
    if (i.upper() == x.upper()):
        d_list.append(y)
        d_reverse_list.append(y[::-1])
    else:
        d_list.append(i)
        d_reverse_list.append(i)

d = " ".join(d_list)
d_reverse = " ".join(d_reverse_list)

print(c)
print(d)
print("%d %d" %(len(c) - c.count(" "), len(d) - d.count(" ")))
print(d_reverse)

counter = 0
for i in range(len(c)):
    if (counter == 0):
        # if (c[i] != " "):
        #     c_removed += c[i]
        # elif (len(c_removed) > 0 and c_removed[-1] != " "):
        #     c_removed += c[i]
        c_removed += c[i]
    counter = (counter + 1) % n

print(c_removed)
