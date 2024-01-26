# -*- coding: utf8 -*-

def Matr(Mat, N, M):
    for i in range(N):
        Mat.append([0] * M)
        s = Fin.readline().split()
        for j in range(M):
            Mat[i][j] = float(s[j])
    return Mat


def Ras(N, W, col):
    ostov = []
    for k in range(N-1):
        minDist = 1e10
        for i in range(N):
            for j in range(N):
                if col[i] != col[j] and W[i][j] < minDist and W[i][j] != 0:
                    iMin = i
                    jMin = j
                    minDist = W[i][j]
        ostov.append((iMin+1, jMin+1))  # Указываются парой две вершины между которыми выбрано ребро, добавляем 1, т.к. счёт вершин ведётся от 0 (мне удобнее вести от 1).
        c = col[jMin]
        for i in range(N):
            if col[i] == c:
                col[i] = col[iMin]
    return ostov


Fin = open('input.txt', "r")

s = Fin.readline()
if not s:
    print('Файл пустой')
elif int(s)==0:
    print('Пустая матрица')
else:
    N = int(s)
    W = []
    W = Matr(W, N, N)
    col = [i for i in range(N)]
    ostov = Ras(N, W, col)
    print('Список рёбер(где указаны две вершины по нему соединяющиеся) минимального остовного дерева:')
    for i in range(len(ostov)):
        print(ostov[i])

Fin.close()