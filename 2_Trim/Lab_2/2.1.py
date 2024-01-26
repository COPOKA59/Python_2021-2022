# -*- coding: utf8 -*-

def Kyz(A, N, L):
    A[0] = 1
    A[1] = 1
    for i in range(2, N + 1):
        A[i] = A[i - 1]
        j = 2
        while j <= i and j <= L:
            A[i] += A[i - j]
            j += 1
    return A


Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов Матрицы')
else:
    N = int(s[0])  # Элементы
    L = int(s[1])  # Деления
    A = [0]*(N+1)
    A = Kyz(A, N, L)
    print(A)
    Fin.write("\n {}".format(A[N]))

Fin.close()
