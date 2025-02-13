height = eval(input())
weight = int(input())

bmi = weight / (height ** 2)

bmi = int(bmi * 1000)

if (bmi % 10 < 5):
    bmi -= bmi % 10
    bmi /= 1000
elif (bmi % 10 > 5):
    bmi -= bmi % 10
    bmi = (bmi + 10) / 1000
else:
    if (bmi % 20 > 10):
        bmi -= bmi % 10
        bmi = (bmi + 10) / 1000
    else:
        bmi -= bmi % 10
        bmi = bmi / 1000

print(format(bmi, '.2f'))