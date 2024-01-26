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


def VV(M):  # Ввод многочлена в строку для вывода
    s = ''
    L = len(M.coef)
    for i in range(L-1, -1, -1):
        if M.coef[i]<0 and s == '':
            s += '-'
        if s != '' and s[len(s)-1] != '+' and s[len(s)-1] != '-':
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
                    s += 'x^('+str(i)+')'
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
elif int(s[0]) == 0:
    print('Многочлен задан одним числом без x')
else:
    SS = int(s[0])  # Старшая степень
    M = MN()  # Переменная для многочлена
    M = OMG(M, SS)  # Занесение данных многочлена в переменную
    s = VV(M)  # Заносим запись многочлена в строку
    print('Многочлен: ', s)
    Fout.write("Многочлен: {}\n".format(s))
Fin.close()
Fout.close()