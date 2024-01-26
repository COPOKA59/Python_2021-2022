def IsPalindrom(K: int):
    U = True
    if K // 10 == 0:
        U = False
    else:
        Z=0
        K1 = K
        while K1 > 0:
            K1 = K1 // 10
            Z += 1
        while K > 9 and U == True:
            if (K // (10**(Z-1) ))==(K%10):
                U = True
            else:
                U = False
            K = (K//(10**(Z-1)))%10
            Z -= 2
    return U


Fin = open('../2TriM/input.txt')
Fout = open('../2TriM/output.txt', "a")

s = Fin.readline().split()
K = int(s[0])
Sum = 0
while True:
    if K > 0:
        print("Исходные данные: K={:d}; Результат: {}".format(K, IsPalindrom(K)))  # вывод на экран
        Fout.write = ("Исходные данные: K={:d}; Результат: {}".format(K, IsPalindrom(K)))  # вывод в файл
        if IsPalindrom(K) == True:
            Sum += 1
    else:
        print('Неправильно заданы данные')
    s = Fin.readline().split()
    K = int(s[0])

print("Количество палиндромов: Sum={}".format(Sum))  # вывод на экран
Fout.write = ("Количество палиндромов: Sum={}".format(Sum))  # вывод в файл

Fin.close()
Fout.close()
