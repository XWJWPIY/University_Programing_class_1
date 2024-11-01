
data = []
"""
def data_input():

    correct = True

    for i in range(3):
        data.append([])
        data[i].append(input())
        num_temp = ""
        all_char_before = True
        for j in data[i][0]:
            if ('0' <= j <= '9'):
                num_temp += j
                all_char_before = False
            elif (all_char_before == False):
                correct = False

        if (not(1000 <= int(num_temp) <= 9999)):
            correct = False

        h = int(input())
        data[i].append([])

        for j in range(h):
            temp = input()
            if (len(temp) != 2):
                correct = False
            elif (not('1' <= temp[0] <= '5')):
                correct = False
            elif (not(('1' <= temp[1] <= '9') or ('a' <= temp[1] <= 'c'))):
                correct = False
            data[i][1].append(temp)
        
    return correct

"""

# input_correct = data_input()

correct = True

for i in range(3):
    data.append([])
    data[i].append(input())
    num_temp = ""
    all_char_before = True
    for j in data[i][0]:
        if ('0' <= j <= '9'):
            num_temp += j
            all_char_before = False
        elif (all_char_before == False):
            correct = False

    if (not(1000 <= int(num_temp) <= 9999)):
        correct = False

    h = int(input())
    data[i].append([])

    for j in range(h):
        temp = input()
        if (len(temp) != 2):
            correct = False
        elif (not('1' <= temp[0] <= '5')):
            correct = False
        elif (not(('1' <= temp[1] <= '9') or ('a' <= temp[1] <= 'c'))):
            correct = False
        data[i][1].append(temp)
conflict = False

# if (not input_correct):
if (not correct):
    print(-1)
else:
    for i in range(3):
        for j in range(len(data[i][1])):
            for k in range(i + 1, 3):
                for m in range(len(data[k][1])):
                    if (data[i][1][j] == data[k][1][m]):
                        conflict = True
                        print("%s,%s,%s" %(data[i][0], data[k][0], data[i][1][j]))
    
    if(not conflict):
        print("correct")
