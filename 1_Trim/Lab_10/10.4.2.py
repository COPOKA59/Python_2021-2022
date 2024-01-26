# -*- coding: utf8 -*-
Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "w")

s = Fin.readline().split()
if not s:
    Fout.write('Пустой файл')
elif int(s[0]) == 0:
    Fout.write('Массив пуст')
else:
    N = int(s[0])
    A = [0] * N
    k = -1

    for i in range(N):
        s = Fin.readline().split()
        A[i] = int(s[0])
        if int(s[0])%2 == 0:
            k += 1

    B = [0] * (k * 2 + 2)
    k = 0
    for i in range(N):
        if A[i] % 2 == 0:
            B[k] = B[k + 1] = A[i]
            k += 2

    Fout.write("Переделанный массив: {}".format(B))

Fin.close()
Fout.close()