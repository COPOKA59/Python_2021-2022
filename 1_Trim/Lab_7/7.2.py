def Fun(N, M, i):
    global k
    N1 = N % 10
    i += 1
    if N1 >= M:
        M = N1
        k = i
    if N//10 == 0:
        return k  # Позиция мак.цифры
    return Fun(N//10, M, i)


N = int(input('Введите число N (N>0): '))
M = 0  # Максимальная цифра
i = 0  # Счётчик позиции
if N > 0:
    print('Позиция последней максимальной цифры =', Fun(N, M, i))
else:
    print('Введено неверное число')