def Sin1(x, E: float) -> float:
    n = 1
    S = k = x
    import math
    while abs(k) > E:
        k = (((-1) ** n) * (x ** (2 * n + 1))) / (math.factorial(2 * n + 1))
        S += k
        n += 1
    return S


Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "a")

x = float(input('Введите значение X: '))
s = Fin.readline().split()
E = float(s[0])
while s:
    print("Исходные данные: X={}, E={:10.2e}; Результат: Sin(X)={}".format(x, E, Sin1(x, E)))  # вывод на экран
    Fout.write = ("Исходные данные: X={}, E={:2.2e}; Результат: Sin(X)={}".format(x, E, Sin1(x, E)))  # вывод в файл
    s = Fin.readline().split()
    E = float(s[0])

import math

print('Значение стандартной ф-ции', math.sin(x))
Fout.write = ('Значение стандартной ф-ции', math.sin(x))

Fin.close()
Fout.close()
