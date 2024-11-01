score = []
get_back = [0, 0]
total = 0
ten_plus = False
game = 0

for i in range(9):
    score.append(int(input()))
    if (score[-1] != 10):
        score.append(int(input()))

score.append(int(input()))
score.append(int(input()))
if (score[-2] == 10):
    score.append(int(input()))
    ten_plus = 2
elif (score[-1] + score[-2] == 10):
    score.append(int(input()))
    ten_plus = 1

get_back[0], get_back[1] = score[-2], score[-1]

score.append(0)
score.append(0)
for i in range(len(score) - 2):
    if (score[i] == 10):
        total += (score[i] + score[i + 1] + score[i + 2])
        score[i] = 0
        game = 0
    elif (i != 0 and (score[i - 1] + score[i] == 10) and (game == 1)):
        total += (score[i] + score[i + 1])
        score[i] = 0
        game = 0
    else:
        total += score[i]
        game = (game + 1) % 2

for i in range(ten_plus):
    total -= get_back[-i - 1]

print(total)
