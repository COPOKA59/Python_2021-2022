# -*- coding: utf8 -*-

Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов Матрицы')
else:
    N = int(s[0])
    M = int(s[1])
    A = []

    s = Fin.readline().split()
    for i in range(N):
        A.append([0] * M)
    i = j = 0
    S = 0
    X = 0
    for Z in range(N*M):
        if i == 0+X and j == 0:
            for j in range(M-X):
                A[i][j] = float(s[j+S])
            S += M - 1 - X - X
        elif i == 0+X and j == M-1-X:
            for i in range(1+X, N-X):
                A[i][j] = float(s[i+S])
            S += N - 1 - X
        elif i == N-1-X and j == M-1-X:
            k = 1
            for j in range(M-2-X, -1+X, -1):
                A[i][j] = float(s[S+k])
                k += 1
            S += M - 1 - X
        elif i == N-1-X and j == 0+X:
            k = 1
            for i in range(N-2-X, 0+X, -1):
                A[i][j] = float(s[S+k-X])
                k += 1
            S += N - 2 - X
            X += 1
    Fin.write("\n {}".format(A))

Fin.close()
