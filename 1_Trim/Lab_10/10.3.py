# -*- coding: utf8 -*-
Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "w")

s = Fin.readline().split()
if not s:
    Fout.write('Пустой файл')
elif int(s[0]) == 0:
    Fout.write('Массив пуст')
elif int(s[0]) == 1:
    s = Fin.readline().split()
    Fout.write("Массив состоит из одного элемента {}".format(int(s[0])))
else:
    N = int(s[0])
    X = [0] * N
    k = 0

    for i in range(N):
        s = Fin.readline().split()
        X[i] = float(s[0])

    for i in range(N):
        if X[i] < 0:
            Otr = X[i]
            for v in range(i, k, -1):
                X[v] = X[v - 1]
            X[k] = Otr
            k += 1

    Fout.write("Переставленный массив: {}".format(X))
Fin.close()
Fout.close()