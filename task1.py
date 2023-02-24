n = int(input('Введите количество монет: '))
count_reshko = 0
count_gerb = 0
for i in range(n):
    x = int(input("Введите 0 если решко или 1 если герб: "))
    if x == 0:
        count_reshko += 1
    else:
        count_gerb += 1
if count_gerb > count_reshko:
    print('Нужно перевернуть  = ', count_reshko)
else:
    print('Нужно перевернуть  = ', count_gerb)
