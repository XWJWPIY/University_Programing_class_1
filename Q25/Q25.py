import numpy


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
            if (not(i[1] == '1' and i[2] == '0')):
                return 1
        elif (len(i) != 2):
            return 1
        elif (not('2'<= i[1] <= '9' or i[1] == 'A'or i[1] == 'J'or i[1] == 'Q'or i[1] == 'K')):
            return 1
        
        if (not(i[0] == 'S' or i[0] == 'H' or i[0] == 'D' or i[0] == 'C')):
            return 1
        
        if ('A' == i[1]): num = 1
        elif ('J' == i[1]): num = 11
        elif ('Q' == i[1]): num = 12
        elif ('K' == i[1]): num = 13
        elif ('1' == i[1]): num = 10
        else: num = int(i[1])

        if ('S' == i[0]): sign = 1
        elif ('H' == i[0]): sign = 2
        elif ('D' == i[0]): sign = 3
        elif ('C' == i[0]): sign = 4

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





# TO-Change
def straight(num_cards: list): 
    for i in range(len(num_cards)):
        num_cards[i] %= 13
    num_cards.sort()
    correct = 0 

    for i in range(4):
        num_cards.append(num_cards[0] + 13)

    for i in range(len(num_cards) - 1):
        if (num_cards[i] + 1 == num_cards[i + 1]):
            correct += 1
        else:
            correct = 0
        if (correct == 4):
            return True
    return False


def same_flush(num_cards):
    flush_list = [0, 0, 0, 0]
    for i in range(len(num_cards)):
        flush_list[num_cards[i] // 13] += 1
   
    if (max(flush_list) >= 5):
        return (True, flush_list.index(max(flush_list)))
    return (False, None)

def same_flush_straight(num_cards: list):
    is_same_flush, flush_num  = same_flush(num_cards.copy())
    if (is_same_flush == False):
        return False
    same_flush_cards = []
    for i in num_cards:
        if (i // 13 == flush_num):
            same_flush_cards.append(i)
    return straight(same_flush_cards)

def get_style_num(cards):
    style_num = 1
    for i in range(len(cards)):
        num = 0
        if ('A' == cards[i][1]): num = 1
        elif ('J' == cards[i][1]): num = 11
        elif ('Q' == cards[i][1]): num = 12
        elif ('K' == cards[i][1]): num = 13
        elif ('1' == cards[i][1]): num = 10
        else: num = int(cards[i][1])

        sign = 0
        if ('S' == cards[i][0]): sign = 1
        elif ('H' == cards[i][0]): sign = 2
        elif ('D' == cards[i][0]): sign = 3
        elif ('C' == cards[i][0]): sign = 4

        cards[i] = (sign - 1) * 13 + (num - 1)

    num_times = [0] * 13

    for i in cards:
        num_times[i % 13] += 1
    
    nums = num_style(num_times.copy())
    is_straight = straight(cards.copy())
    is_same_flush, flush_num = same_flush(cards.copy())
    if (nums[2] >= 1): style_num = 2
    if (nums[2] >= 2): style_num = 3
    if (nums[3] >= 1): style_num = 4
    if (is_straight == True): style_num = 5
    if (is_same_flush): style_num = 6
    if (nums[2] >= 1 and nums[3] >= 1 or nums[3] >= 2): style_num = 7
    if (nums[4] >= 1): style_num = 8
    if (same_flush_straight(cards.copy())): style_num = 9

    return style_num


cards_list = []
cards_all = []
for i in range(3):
    cards = input().split(" ")
    cards_list.append(cards)
    cards_all += cards.copy()
check = cheaker(cards_all)
if (check == 1):
    print("Error input")
elif (check == 2):
    print("Duplicate deal")
else:
    style_num = []
    style_num.append(get_style_num(cards_list[0].copy() + cards_list[-1].copy()))
    style_num.append(get_style_num(cards_list[1].copy() + cards_list[-1].copy()))
    if (style_num[0] > style_num[1]):
        print("A %d" % style_num[0])
    elif (style_num[0] < style_num[1]):
        print("B %d" % style_num[1])
    else:
        print("Tie")
    


