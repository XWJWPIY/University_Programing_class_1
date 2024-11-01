
def printer(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if (j != n - 1):
                print("%d " %array[i][j], end = '')
            else:
                print(array[i][j])

def clockwise(array, turns):
    temp = []
    if (turns == 0):
        return array
    
    for i in range(len(array)):
        temp.append([])
        for j in range(len(array[i])):
            temp[i].append(array[n - j - 1][i])
    return clockwise(temp, turns - 1)
    

n = int(input())
array = []
clockwise_turn = 0

for i in range(n):
    array.append([])
    for j in range(n):
        array[i].append(i * n + j + 1)

command = input()

clockwise_turn = (command.count('R') - command.count('L')) % 4

printer(clockwise(array, clockwise_turn))
