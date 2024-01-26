# -*- coding: utf8 -*-

Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов Матрицы')
else:
    N = int(s[0])
    A = []

    for i in range(N):
        s = Fin.readline().split()
        A.append([0] * N)
        for j in range(N):
            A[i][j] = float(s[j])
    print(A)

    S = N*(N-1)/2
    F = 0
    C = 0
    for i in range(N):
        for j in range(N):
            if j < i and A[i][j] == 0:
                F += 1
            if j >= i and A[i][j] == 0:
                C += 1
    if F == S and C < (S+N)//2:
        Fin.write('\n Матрица является верхней треугольной')
    else:
        Fin.write('\n Матрица не является верхней треугольной')

Fin.close()
