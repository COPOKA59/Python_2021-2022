# -*- coding: utf8 -*-

def Matr(Mat, N, M):
    for i in range(N):
        Mat.append([0] * M)
        s = Fin.readline().split()
        for j in range(M):
            Mat[i][j] = float(s[j])
    return Mat


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
    A = Matr(A, N, M)

    B = []
    for i in range(M):
        B.append([0] * N)

    for i in range(N):
        for j in range(M):
            B[j][N-1-i] = A[i][j]

    for i in range(M):
        Fin.write("\n {}".format(B[i]))

Fin.close()