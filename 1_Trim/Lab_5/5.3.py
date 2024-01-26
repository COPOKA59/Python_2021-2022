Fout = open("../2TriM/output.txt", "a")
X = int(input('Введите значение X (X>1): '))
E = int(input('Введите степень точности (0<E<1): '))
E1 = 10 ** E
n = 0
import math
S = math.pi / 2
while n < E:
    S += ((-1) ** (n + 1)) / ((2 * n + 1) * (X ** (2 * n + 1)))
    n += 1
S2=math.atan(X)
print(("Точность: {:10.2e}; Найденное значение tg(x): {}; Значение по стандартной функции tg(x): {}".format(E1, S, S2)))
Fout.write = ("Точность: {:10.2e}; Найденное значение tg(x): {}; Значение по стандартной функции tg(x): {}".format(E1, S, S2))
Fout.close()