def answer(n):
    if n < 1:
        return 'ERROR'
    k = 0
    while n > 0:
        n >>= 1
        k += 1

    return k


num = int(input('Введите число N: '))
print(f'Минимальное количество вопросов: {answer(num)}')

