def SumRange(A, B) -> int:
    S = 0
    if A > B:
        S = 0
    else:
        K = A
        while K <= B:
            S += K
            K += 1
    return S


Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "a")

s = Fin.readline().split()
if s==[]: print('Файл пустой')
else:
 A, B = int(s[0]), int(s[1])
 while True:
    print("Исходные данные: A={:d}, B={:d}; Результат: S={:d}".format(A, B, SumRange(A, B))) # вывод на экран
    Fout.write = ("Исходные данные: A={:d}, B={:d}; Результат: S={:d}".format(A, B, SumRange(A, B)))  # вывод в файл
    s = Fin.readline().split()
    A, B = int(s[0]), int(s[1])

Fin.close()
Fout.close()