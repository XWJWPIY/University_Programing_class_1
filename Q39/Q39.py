def testing(player_list: list, board_size:int):
    ans = 0
    for i in range(board_size):
        total = 0
        for j in range(board_size):
            total += player_list[i*board_size + j]
        if (total == 0):
            ans += 1

    for i in range(board_size):
        total = 0
        for j in range(board_size):
            total += player_list[j*board_size + i]
        if (total == 0):
            ans += 1
    
    total = 0
    for i in range(board_size):
        total += (player_list[i*board_size + i])
    if (total == 0):
        ans += 1
    total = 0
    for i in range(board_size):
        total += (player_list[i*board_size + board_size - i - 1])
    if (total == 0):
        ans += 1
    return ans

n = int(input())
m = int(input())

win_ans = [0, 0]

player_list = []

for i in range(2):
    player_list.append([])
    temp = input()
    temp = temp.split(" ")
    for j in temp:
        player_list[i].append(int(j))

temp = input()
if (temp.count(" ") > 0):
    temp = temp.split(" ")
else:
    temp = [temp]

index = 0


while (index < m):
    for i in range(2):
        player_list[i][player_list[i].index(int(temp[index]))] = 0
        win_ans[i] = testing(player_list[i], n)
    index = index + 1


if (win_ans[0] == win_ans[1]):
    print("Tie")
elif (win_ans[0] > win_ans[1]):
    print("A Win")
else:
    print("B Win")
