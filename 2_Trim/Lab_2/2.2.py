# -*- coding: utf8 -*-

def Matr(Mat, N, M):
    for i in range(N):
        Mat.append([0] * M)
        s = Fin.readline().split()
        for j in range(M):
            Mat[i][j] = float(s[j])
        print(A[i])
    return Mat


def CHER(A, N):
    for i in range(1, N):
        A[0][i] += A[0][i-1]
    for i in range(1, N):
        A[i][0] += A[i-1][0]
    for i in range(1, N):
        for j in range(1, N):
            if A[i-1][j] >= A[i][j-1]:
                A[i][j] += A[i][j-1]
            else:
                A[i][j] += A[i-1][j]
    return A


Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов Матрицы')
else:
    N = int(s[0])
    A = []

    A = Matr(A, N, N)
    A = CHER(A, N)

    for i in range(N):
        Fin.write("\n {}".format(A[i]))

Fin.close()