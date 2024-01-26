# -*- coding: utf8 -*-

def Mass(Mas, N):
    Mas = [0] * N
    s = Fin.readline().split()
    for i in range(N):
        Mas[i] = float(s[i])
    return Mas


Fin = open('input.txt', "r+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов массива')
else:
    N = int(s[0])
    A = [0] * N
    A = Mass(A, N)

    Z = 1
    S = 0
    for i in range(1, N):
        if A[i-1]==A[i]:
            Z += 1
            if Z == 2:
                S += 1
        else:
            Z = 1
    Fin.write("\nКол-во цепочек - {}".format(S))


Fin.close()