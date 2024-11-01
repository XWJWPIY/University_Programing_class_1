# 不賺不賠? 顯示 +0
def get_card(card):
    if (card == "A"):
        return 1
    elif (card == "J" or card == "Q" or card == "K"):
        return 0.5
    else:
        return int(card)

n = int(input())

bet_money = []
total_num = []
quit_game = []

temp = input().split(" ")
for i in temp:
    bet_money.append(int(i))
    quit_game.append(False)
bet_money.append(0) # 莊家

temp = input().split(" ")
computer = get_card(temp[0])
for i in range(n):
    total_num.append(get_card(temp[i + 1]))

for i in range(n):
    temp = input()
    while (temp != "N"):
        total_num[i] += get_card(temp.split(" ")[1])
        if (total_num[i] > 10.5):
            quit_game[i] = True
            bet_money[-1] += bet_money[i]
            bet_money[i] = -bet_money[i]
            break

        elif (total_num[i] == 10.5):
            quit_game[i] = True
            bet_money[-1] -= bet_money[i]
            break
        
        temp = input()

while (True):
    if (min(total_num) >= 10.5):
        break
    if (computer > 10.5):
        for i in range(n):
            if (quit_game[i] == False):
                bet_money[-1] -= bet_money[i]
        break

    elif (computer == 10.5):
        for i in range(n):
            if (quit_game[i] == False):
                bet_money[-1] += bet_money[i]
                bet_money[i] = -bet_money[i]
        break

    elif (computer > min(total_num)):
        for i in range(n):
            if (quit_game[i] == False):
                if (computer >= total_num[i]):
                    bet_money[-1] += bet_money[i]
                    bet_money[i] = -bet_money[i]
                else:
                    bet_money[-1] -= bet_money[i]
        break

    computer += get_card(input())

for i in range(n + 1):
    if (i != n):
        print("Player%d " %(i + 1), end = "")
    else:
        print("Computer ", end = "")
    if (bet_money[i] < 0):
        print("%d" % bet_money[i])
    else:
        print("+%d" % bet_money[i])


