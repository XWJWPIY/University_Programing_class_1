location_begin = []
location_end = []

n = int(input())

for i in range(n):
    temp = input()
    temp = temp.split(" ")
    location_begin.append(int(temp[0]))
    location_end.append(int(temp[1]))

location_begin.sort()
location_end.sort()

is_lining = 0
total = 0
begin = min(location_begin)

while(len(location_begin) > 0 or len(location_end) > 0):
    if (is_lining == 0):
        begin = location_begin.pop(0)
        is_lining = 1
        continue
    elif (len(location_end) > 0 and len(location_begin) == 0):
        total += (location_end[-1] - begin)
        is_lining = 0
        break
    elif (location_begin[0] < min(location_end)):
        is_lining += 1
        location_begin.pop(0)
    elif (location_begin[0] == min(location_end)):
        location_begin.pop(0)
        location_end.pop(0)
    else:
        if (is_lining == 1):
            total += (location_end[0] - begin)
        is_lining -= 1
        location_end.pop(0)

print(total)
