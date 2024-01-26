def Koord(MAS, k):  # Составление массива с координатами (X, Y) для множества
    S = Fin.readline().split()
    for i in range(0, k * 2, 2):
        MAS[i] = float(S[i])
        MAS[i+1] = float(S[i + 1])
    return MAS


def SRAV():  # Сравнение координат первого множества с другим
    global M, m, A, B
    d = 0
    c = 0
    for i in range(0, M*2, 2):
        for v in range(0, m*2, 2):
            if A[i] == B[v] and A[i+1] == B[v+1]:
                c += 1
        if c > 0:
            C[d] += 1
        d += 1
        c = 0
    return C


Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "w")

s = Fin.readline().split()  # Первая строка

if not s:
    Fout.write('Файл пуст')
elif int(s[0]) == 0:
    Fout.write('В файле 0 множеств')
elif int(s[0]) == 1:
    Fout.write('В файле только 1 множество')
else:
    n = int(s[0])  # Переменная для количества множеств
    M = int(s[1])  # Переменная для количества точек в 1 множестве
    A = [0] * M * 2  # Массив для 1 множества
    C = [0] * M  # Массив для подсчёта

    A = Koord(A, M)  # Массив первого множества
    for i in range(2, n + 1):  # Перебор других множеств:
        m = int(s[i])  # Количество точек в другом множестве
        B = [0] * m * 2  # Массив для другого множества
        B = Koord(B, m)
        SRAV()

    Max = -1  # Максимальное кол-во множеств у точки
    for i in range(M):
        if C[i] > Max:  # Выявление максимального
            c = i  # индекс точки с макс.множествами
            Max = C[i]

    if Max == 0:
        Fout.write('В файле точки первого множества не встречаются в других множествах')
    else:
        Fout.write("Точка ({}, {}) первого множества принадлежит ещё {} множеств(-у/-ам)".format(A[c*2], A[c*2+1], Max))

Fin.close()
Fout.close()