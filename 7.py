num = int(input('Введите число->'))
if num % 2 == 0:
    while num > 2:
        num /= 2
    if num == 2:
        print('верно')
    else:
        print('неверно')
else:
    print('неверно')
