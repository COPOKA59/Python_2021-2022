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
    Fout.write("Минимальный локальный максимум {}".format(int(s[0])))
else:
    N = int(s[0])
    A = [0] * N
    B = [0] * N

    for i in range(N):
        s = Fin.readline().split()
        A[i] = float(s[0])
        B[i] = float(s[0])

    for i in range(N):
        if i != (N - 1):
            if A[i] >= A[i + 1] and A[i] >= B[i]:
                B[i] = A[i]
            elif A[i + 1] >= B[i]:
                B[i] = A[i + 1]
        if i != 0:
            if A[i] >= A[i - 1] and A[i] >= B[i]:
                B[i] = A[i]
            elif A[i - 1] >= B[i]:
                B[i] = A[i - 1]

    Fout.write("Минимальный локальный максимум {}".format(min(B)))

Fin.close()
Fout.close()
