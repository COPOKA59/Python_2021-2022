def Fun(N, M, i):
    N1 = N % 10
    if N1 < M:
        M = N1
        i = 0
        return Fun(N, M, i)
    if N1 == M:
        i += 1
    if N//10 == 0:
        return i

    return Fun(N//10, M, i)


N = int(input('Введите число N (N>0): '))
M = 10  # Минимальная цифра
i = 0  # Счётчик
if N > 0:
    print('Минимальных цифр в его записи =', Fun(N, M, i))
else:
    print('Введено неверное число')
