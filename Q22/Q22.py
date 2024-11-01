
def cheaker(cards):
    cheaklist = []
    error_input = False # return 1
    duplicate_deal = False # return 2

    for i in range(4):
        cheaklist.append([])
        for j in range(13):
            cheaklist[i].append(False)
    
    for i in cards:
        if (len(i) == 3):
            if (not(i[0] == '1' and i[1] == '0')):
                return 1
        elif (len(i) != 2):
            return 1
        elif (not('2'<= i[0] <= '9' or i[0] == 'A'or i[0] == 'J'or i[0] == 'Q'or i[0] == 'K')):
            return 1
        
        if (not(i[-1] == 'S' or i[-1] == 'H' or i[-1] == 'D' or i[-1] == 'C')):
            return 1
        
        if ('A' == i[0]): num = 1
        elif ('J' == i[0]): num = 11
        elif ('Q' == i[0]): num = 12
        elif ('K' == i[0]): num = 13
        elif ('1' == i[0]): num = 10
        else: num = int(i[0])

        if ('S' == i[-1]): sign = 1
        elif ('H' == i[-1]): sign = 2
        elif ('D' == i[-1]): sign = 3
        elif ('C' == i[-1]): sign = 4

        if (cheaklist[sign - 1][num - 1] == True):
            duplicate_deal = True
        else:
            cheaklist[sign - 1][num - 1] = True
    
    if (duplicate_deal == True):
        return 2
    return 0


def num_style(cards):
    cards.sort(reverse = True)
    nums = [0, 0, 0, 0, 0]
    testing = 4
    while (len(cards) > 0):
        if (testing == cards[0]):
            nums[testing] += 1
            cards.pop(0)
        else:
            testing -= 1

    return nums


def straight(num_cards):
    for i in range(len(num_cards)):
        num_cards[i] %= 13
    num_cards.sort()
    correct = 0

    for i in range(len(num_cards)):
        if ((num_cards[(i - 1)] + 1) % 13 == num_cards[i]):
            correct += 1
    
    if (correct == 4):
        return True
    return False


def same_flush(num_cards):
    for i in range(len(num_cards)):
        num_cards[i] //= 13
    num = num_cards[0]

    for i in num_cards:
        if (num != i):
            return False
    return True

def sortSecond(val):
    return val[1]

all_card = []
ans = []
n = int(input())
error_input = False
duplicate_deal = False

for times in range(n):
    cards = input().split(" ")
    name = cards.pop(0)
    check = cheaker(cards)
    if (check == 1):
        error_input = True # Error input
    elif (check == 2):
        duplicate_deal = True # Duplicate deal
    else:
        style_num = 1
        for i in range(len(cards)):
            all_card.append(cards[i])
            num = 0
            if ('A' == cards[i][0]): num = 1
            elif ('J' == cards[i][0]): num = 11
            elif ('Q' == cards[i][0]): num = 12
            elif ('K' == cards[i][0]): num = 13
            elif ('1' == cards[i][0]): num = 10
            else: num = int(cards[i][0])

            sign = 0
            if ('S' == cards[i][-1]): sign = 1
            elif ('H' == cards[i][-1]): sign = 2
            elif ('D' == cards[i][-1]): sign = 3
            elif ('C' == cards[i][-1]): sign = 4

            cards[i] = (sign - 1) * 13 + (num - 1)
        
        num_times = [0] * 13

        for i in cards:
            num_times[i % 13] += 1
        
        nums = num_style(num_times.copy())
        is_straight = straight(cards.copy())
        is_same_flush = same_flush(cards.copy())

        if (nums[2] == 1): style_num = 2
        if (nums[2] == 2): style_num = 3
        if (nums[3] == 1): style_num = 4
        if (is_straight == True): style_num = 5
        if (is_same_flush): style_num = 6
        if (nums[2] == 1 and nums[3] == 1): style_num = 7
        if (nums[4] == 1): style_num = 8
        if (is_same_flush and is_straight): style_num = 9

        ans.append([name, style_num])

if (error_input or cheaker(all_card) == 1):
    print("Error input")
elif (duplicate_deal or cheaker(all_card) == 2):
    print("Duplicate deal")
else:
    ans.sort(key = sortSecond, reverse=True)
    for i in range(n):
        print("%s %d" %(ans[i][0], ans[i][1]))

