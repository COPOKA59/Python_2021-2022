# -*- coding: utf8 -*-

class MN():  # Класс Многочлен
    step = 0
    coef = []


def OMG(M, SS):  # Инициализация
    s = Fin.readline().split()
    M.coef = [0] * (SS + 1)
    if SS != int(s[0]):
        print('Неправильно введена старшая степень')
    else:
        for i in range(SS + 1, -2, -2):
            M.step = int(s[(SS + 1) - i])
            M.coef[M.step] = int(s[(SS + 1) - i + 1])
    return M


def Fun1(M, Z, NT):
    L1 = len(M.coef)
    L2 = len(Z.coef)
    T = True
    if L1 >= L2:
        NT.coef = [0] * L1
    else:
        NT.coef = [0] * L2
        L1, L2 = L2, L1
        T = False
    for i in range(L1):
        if i >= L2:
            if T == True:
                NT.coef[i] = M.coef[i]
            else:
                NT.coef[i] = Z.coef[i]
        else:
            NT.coef[i] = M.coef[i] + Z.coef[i]
    return NT


def Fun2(M, Z, NT):
    for i in range(len(Z.coef)):
        Z.coef[i] *= -1
    NT = Fun1(M, Z, NT)
    return NT


def Fun3(M, Z, NT):
    L1 = len(M.coef)
    L2 = len(Z.coef)
    NT.coef = [0]*(L1 + L2 - 1)
    for i in range(L1):
        for j in range(L2):
            NT.coef[i+j] += M.coef[i]*Z.coef[j]
    return NT


def Fun4(M):
    N = int(input('Введите значение X: '))
    Z = 0
    for i in range(len(M.coef)):
        Z += N**(i)*M.coef[i]
    return Z


def VV(M):  # Ввод многочлена в строку для вывода
    s = ''
    L = len(M.coef)
    for i in range(L - 1, -1, -1):
        if M.coef[i] < 0 and s == '':
            s += '-'
        if s != '' and s[len(s) - 1] != '+' and s[len(s) - 1] != '-':
            if M.coef[i] > 0:
                s += '+'
            elif M.coef[i] < 0:
                s += '-'
        if i == 0 and M.coef[i] != 0:
            s += str(abs(M.coef[i]))
        else:
            if M.coef[i] == 1 or M.coef[i] == -1:
                if i == 1:
                    s += 'x'
                else:
                    s += 'x^(' + str(i) + ')'
            elif M.coef[i] != 0:
                if i == 1:
                    s += str(abs(M.coef[i])) + '*' + 'x'
                else:
                    s += str(abs(M.coef[i])) + '*' + 'x^(' + str(i) + ')'
    return s


Fin = open('input.txt', "r")
Fout = open('output.txt', "w+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
    Fout.write('Файл пустой\n')
elif int(s[0]) == 0:
    print('Многочлен задан одним числом без x')
    Fout.write('Многочлен задан одним числом без x\n')
else:
    SS = int(s[0])  # Старшая степень
    M = MN()  # Переменная для первого многочлена
    M = OMG(M, SS)  # Занесение данных многочлена в переменную
    if M.coef == [0] * (SS + 1):
        print('Неправильный ввод. Выполнение операций невозможно.')
        Fout.write('Неправильный ввод. Выполнение операций невозможно.\n')
    else:
        print('Какой тип операции выполнить?')
        print('1) Сложение')
        print('2) Вычитание')
        print('3) Произведение')
        print('4) Значение многочлена')
        Fout.write('Какой тип операции выполнить?\n')
        Fout.write('1) Сложение\n')
        Fout.write('2) Вычитание\n')
        Fout.write('3) Произведение\n')
        Fout.write('4) Значение многочлена\n')
        N = int(input('Введите число операции: '))
        Fout.write("Число операции: {}\n".format(N))
        NT = MN()  # Переменная для итога
        if N == 1:
            s = Fin.readline().split()
            if not s:
                print('Нет второго многочлена в файле')
                Fout.write('Нет второго многочлена в файле\n')
            elif int(s[0]) == 0:
                print('Многочлен задан одним числом без x')
                Fout.write('Многочлен задан одним числом без x\n')
            else:
                SS = int(s[0])
                Z = MN()  # Переменная для второго многочлена
                Z = OMG(Z, SS)
                print('(', VV(M), ') + (', VV(Z), ')', sep='')
                Fout.write('({}) + ({})\n'.format(VV(M),VV(Z)))
                NT = Fun1(M, Z, NT)
                print(VV(NT))
                Fout.write('Результат операции: {}\n'.format(VV(NT)))
        elif N == 2:
            s = Fin.readline().split()
            if not s:
                print('Нет второго многочлена в файле')
                Fout.write('Нет второго многочлена в файле\n')
            elif int(s[0]) == 0:
                print('Многочлен задан одним числом без x')
                Fout.write('Многочлен задан одним числом без x\n')
            else:
                SS = int(s[0])
                Z = MN()  # Переменная для второго многочлена
                Z = OMG(Z, SS)
                print('(', VV(M), ') - (', VV(Z), ')', sep='')
                Fout.write('({}) - ({})\n'.format(VV(M), VV(Z)))
                NT = Fun2(M, Z, NT)
                print(VV(NT))
                Fout.write('Результат операции: {}\n'.format(VV(NT)))
        elif N == 3:
            s = Fin.readline().split()
            if not s:
                print('Нет второго многочлена в файле')
                Fout.write('Нет второго многочлена в файле\n')
            elif int(s[0]) == 0:
                print('Многочлен задан одним числом без x')
                Fout.write('Многочлен задан одним числом без x\n')
            else:
                SS = int(s[0])
                Z = MN()  # Переменная для второго многочлена
                Z = OMG(Z, SS)
                print('(', VV(M), ') * (', VV(Z), ')', sep='')
                Fout.write('({}) * ({})\n'.format(VV(M), VV(Z)))
                NT = Fun3(M, Z, NT)
                print(VV(NT))
                Fout.write('Результат операции: {}\n'.format(VV(NT)))
        elif N == 4:
            print(VV(M), sep='')
            Fout.write('{}\n'.format(VV(M)))
            Z = Fun4(M)
            print(Z)
            Fout.write('Результат операции: {}\n'.format(Z))
        else:
            print('Неправильно введены данные операции')
            Fout.write('Неправильно введены данные операции\n')

Fin.close()
Fout.close()
