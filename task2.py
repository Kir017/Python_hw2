# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

summa = int(input('Введите сумму чисел: '))
multiplication = int(input('Введите произведение чисел: '))
stop = 0
for i in range(summa):
    if stop == 1:
        break
    for j in range(multiplication):
        if summa == i + j and multiplication == i * j:
            print(f'Первое число {i}, второе число {j} ')
            stop += 1
else:
    print('Введенные данные не верны')



