Fin = open('../2TriM/input.txt')

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('0 элементов массива')
else:
    N = int(s[0])
    A = [0]*N
    Sum = 0
    c = 0
    for i in range(N):
        s = Fin.readline().split()
        if not s:
            c = 1
            print('Неправильные данные файла')
            break
        A[i] = float(s[0])
        Sum += A[i]
    k = 0
    for x in A:
        if x > (Sum/N):
            k += 1
    s = Fin.readline().split()
    if not s and c == 0:
        print("Количество элементов превышающих среднее арифметическое {:5.2f} = {}".format(Sum/N, k))
    elif c != 1:
        print('Неправильные данные файла')

Fin.close()
