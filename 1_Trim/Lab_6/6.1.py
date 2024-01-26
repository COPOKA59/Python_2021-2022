def AddLeftDigit(D, K):
    K1 = K
    while K1 > 0:
        K1 = K1 // 10
        D = D * 10

    if K == 0:
        K = D * 10
    else:
        K = K + D
    return K


Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "a")

s = Fin.readline().split()
K = int(s[0])

while True:
    s = Fin.readline().split()
    D = int(s[0])
    if 0 < D < 10 and K > 0:
        print("Исходные данные: D={:d}, K={:d}; Результат: K={:d}".format(D, K, AddLeftDigit(D, K)))  # вывод на экран
        Fout.write = ("Исходные данные: D={:d}, K={:d}; Результат: K={:d}".format(D, K, AddLeftDigit(D, K)))  # вывод в файл
        K = AddLeftDigit(D, K)
    else:
        print('Неправильно заданы данные для переменных')
        break

Fin.close()
Fout.close()
