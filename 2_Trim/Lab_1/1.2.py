# -*- coding: utf8 -*-

def Mass(Mas, N):
    Mas = [0] * N
    s = Fin.readline().split()
    for i in range(N):
        Mas[i] = float(s[i])
    return Mas


Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов массива')
else:
    N = int(s[0])
    A = [0] * N
    A = Mass(A, N)

    for i in range(1, N):
        Z = A[i]
        j = i - 1
        while j >= 0 and Z >= A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = Z
    Fin.write("\n{}".format(A))

    #  Бинарный поиск

    L = 0
    R = N
    J = -1
    while L < R or N == 1:
        C = (L + R) // 2
        N -= 1
        if C < A[C]:
            L = C
        elif C > A[C]:
            R = C
        elif C == A[C]:
            J = C
            L = R

    while A[J+1] == C:
            J += 1

    if J == -1:
        Fin.write("\n Номер элемента = {}. Такого элемента нет".format(J))
    else:
        Fin.write("\n Номер элемента = {}".format(J))

Fin.close()
