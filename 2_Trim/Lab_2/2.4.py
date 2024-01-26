# -*- coding: utf8 -*-

def Kyz(A, N, M):
    A[0] = 1
    A[1] = 1
    L = 4
    s = Fin.readline().split()
    z = 0
    for i in range(2, N + 1):
        print(s[z], i)
        if i == int(s[z]):
            A[i] = 0
            if z+1 < M:
                z += 1
        else:
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
    M = int(s[1])
    A = [0]*(N+1)
    A = Kyz(A, N, M)
    print(A)
    Fin.write("\n {}".format(max(A)))

Fin.close()
