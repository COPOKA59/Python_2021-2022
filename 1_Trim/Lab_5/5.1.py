Fin = open('../2TriM/input.txt')
s = Fin.readline().split()
if s == []:
    print('Файл пустой')
else:
    k = int(s[0])
    s = Fin.readline().split()
    N = int(s[0])
    S1 = 0
    for i in range(0, N):
        s = Fin.readline().split()
        a = int(s[0])
        if k == a == 0:
            S1 += 1
        elif a % k == 0:
            S1 += 1

Fin.close()
print('Количество кратных элементов = ', S1)
