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
    A = [0] * N * 2
    k = -1

    for i in range(N):
        s = Fin.readline().split()
        if int(s[0])%2 == 0:
            k += 1
            A[k] = int(s[0])

    for i in range(k, -1, -1):
        A[i*2] = A[i]
        A[i * 2 + 1] = A[i]

    Fout.write('Переделанный массив: [')
    for i in range(k*2+2):
        Fout.write("{} ".format(A[i]))
    Fout.write(']')

Fin.close()
Fout.close()