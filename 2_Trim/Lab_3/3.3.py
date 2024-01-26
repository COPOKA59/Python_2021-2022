# -*- coding: utf8 -*-

class MN():  # Класс Многочлен
    step = 0
    coef = []


Fin = open('input.txt', "r")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('Многочлен задан одним числом без x')
else:
    SS = int(s[0])  # Старшая степень
    M = MN()  # Переменная для многочлена

Fin.close()