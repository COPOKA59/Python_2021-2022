# -*- coding: utf8 -*-

Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов массива')
else:
    N = int(s[0])
    A = [0] * N

    for i in range(N):
        s = Fin.readline().split()
        A[i] = float(s[0])
    print(A)

    for i in range(1, N):
        Z = A[i]
        j = i - 1
        while j >= 0 and Z >= A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = Z
        print('=', A)
    print(A)
    Fin.write("\n{}".format(A))
Fin.close()
