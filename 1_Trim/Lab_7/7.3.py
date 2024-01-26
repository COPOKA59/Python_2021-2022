def Fun(N, M, i):
    global S
    i += 1
    N1 = N % 10
    if N1 > M:
        M = N1
        S = i
    elif N1 == M:
        S += i
    if N//10 == 0:
        return S  # Сумма позиций макс.цифры
    return Fun(N//10, M, i)


N = int(input('Введите число N (N>0): '))
M = 0  # Максимальная цифра
i = 0  # Счётчик позиций
if N > 0:
    print('Сумма номеров позиций макс.цифр =', Fun(N, M, i))
else:
    print('Введено неверное число')
