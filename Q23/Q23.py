
def get_card(card):
    if (card == "A"):
        return 1
    elif (card == "J" or card == "Q" or card == "K"):
        return 0.5
    else:
        return int(card)

total_num = []
stop_get_card = []

for i in range(2):
    total_num.append(0)
    stop_get_card.append(0)

for i in range(2):
    card = input()
    total_num[i] += get_card(card)

while (sum(stop_get_card) < len(stop_get_card)):
    if (stop_get_card[0] == 0 and sum(total_num) - total_num[0] != 0):
        card = input()
        if (card == "N"):
            stop_get_card[0] = 1
        else:
            card = input()
            total_num[0] += get_card(card)
            if (total_num[0] > 10.5):
                total_num[0] = 0
                stop_get_card[0] = 1
    else:
        stop_get_card[0] = 1
    
    if (stop_get_card[1] == 0):
        if ((total_num[1] <= 8 or total_num[0] > total_num[1]) and sum(total_num) - total_num[1] != 0):
            card = input()
            total_num[1] += get_card(card)
            if (total_num[1] > 10.5):
                total_num[1] = 0
                stop_get_card[1] = 1
        else:
            stop_get_card[1] = 1
    else:
        stop_get_card[1] = 1

if (total_num[1] > total_num[0]):
    print("computer win")
elif (total_num[1] == total_num[0]):
    print("it's a tie")
else:
    print("player win")



