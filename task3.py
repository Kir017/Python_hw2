number = int(input('Введите число: '))
i = 0
while 2 ** i <= number:
    print(f'2^{i} = {2 ** i}')
    i += 1