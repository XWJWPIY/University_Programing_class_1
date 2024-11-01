
sudoku = []

for i in range(4):
    sudoku.append([])
    temp = input().split()
    for j in temp:
        sudoku[i].append(int(j))

zero  = 8

while (zero > 0):
    for i in range(4):
        # print("r", sudoku[i])
        if (sudoku[i].count(0) == 1):
            zero -= 1
            for j in range(4):
                if (sudoku[i][j] == 0):
                    sudoku[i][j] = ((1 + 4) * 4) // 2 - sum(sudoku[i])
        # print(zero)

    for j in range(4):
        temp_list = [0, 0, 0, 0]
        for i in range(4):
            temp_list[i] = sudoku[i][j]
        # print("L", temp_list)
        if (temp_list.count(0) == 1):
            zero -= 1
            for i in range(4):
                if (sudoku[i][j] == 0):
                    sudoku[i][j] = ((1 + 4) * 4) // 2 - sum(temp_list)
        # print(zero)

    for i in range(2):
        for j in range(2):
            temp_list = [0, 0, 0, 0]
            for k in range(4):
                temp_list[k] = sudoku[i*2 + k//2][j*2 + k%2]
            # print(temp_list)
            
            if (temp_list.count(0) == 1):
                zero -= 1
                for k in range(4):
                    if (temp_list[k] == 0):
                        temp_list[k] = ((1 + 4) * 4) // 2 - sum(temp_list)
                        sudoku[i*2 + k//2][j*2 + k%2] = temp_list[k]
            # print(zero)

for i in sudoku:
    print(' '.join(map(str, i)))