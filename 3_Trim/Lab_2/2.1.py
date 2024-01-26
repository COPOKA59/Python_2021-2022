# -*- coding: utf8 -*-
class Tpeople:  # Класс человек

    def __init__(self, fio, DR, pol):  # Начальные настройки
        self.fio = fio
        self.DR = DR
        self.pol = pol

    def age(self, A, B, C):  # Вычисление возраста человека
        a = self.DR[0] + self.DR[1]  # День
        b = self.DR[3] + self.DR[4]  # Месяц
        c = self.DR[6:]  # Год
        Z = int(C) - int(c)  # Вычисление года
        if int(b) > int(B):  # Если родился позже указанного месяца
            Z -= 1
        elif int(b) == int(B):  # Если в этот месяц
            if int(a) > int(A):  # Если родился раньше указанного числа
                Z -= 1
        print("{} лет".format(Z))

    def zamena(self):  # Изменить дату рождения
        print('Дата рождения:', self.DR)
        a, b, c = map(str, input('Запишите изменённую дату через точку:').split('.'))
        self.DR = str(a)+'.'+str(b)+'.'+str(c)
        print("Изменённая запись: {} {} {}".format(self.fio, self.DR, self.pol))


def mas():  # Массив объектов
    global M
    Fin = open('input.txt', "r")  # Ввод данных из файла
    s = Fin.readline().split()
    M = []
    kol = 0
    while s:
        M.append(Tpeople(s[0], s[1], s[2]))  # 1 Создание объектов
        kol += 1
        s = Fin.readline().split()
    Fin.close()


def VM():
    global M
    TF = 1
    while TF == 1:
        print('1. Вывести информацию всех людей;')
        print('2. Вывести информацию по конкретному человеку;')
        print('3. Вывести информацию по конкретному атрибуту.')
        z = int(input('Выберите подоперацию(введите число): '))
        if z == 1:
            for i in range(len(M)):
                print('id = {}, ФИО = {}, Дата рождения = {}, Пол = {}'.format(i, M[i].fio, M[i].DR, M[i].pol))
        elif z == 2:
            i = int(input('Введите id человека: '))
            print('id = {}, ФИО = {}, Дата рождения = {}, Пол = {}'.format(i, M[i].fio, M[i].DR, M[i].pol))
        elif z == 3:
            FT = 1
            while FT == 1: # 5 Вывод всех атрибутов объектов
                print('1. ФИО')
                print('2. Дата рождения')
                print('3. Пол')
                i = int(input('Выберите атрибут(введите число): '))
                if i == 1:
                    for i in range(len(M)):
                        print('id = {}, ФИО = {}'.format(i, M[i].fio))
                elif i == 2:
                    for i in range(len(M)):
                        print('id = {}, Дата рождения = {}'.format(i, M[i].DR))
                elif i == 3:
                    for i in range(len(M)):
                        print('id = {}, Пол = {}'.format(i, M[i].pol))
                FT = int(input('Выбрат другой атрибут?(1 - Да, 2 - нет): '))
        TF = int(input('Повторить операцию?(1 - Да, 2 - нет): '))

def DD(a, b, c):  # Проверка даты ДД.ММ.ГГГГ
    if str(c) in '0123456789':
        if str(b) in '0123456789':
                if str(a) in '0123456789':
                    if (b < 13) and (b > 0) and isint(b) and isint(c):
                        if (a < 32) and (a > 0) and isint(a):
                            return 1
                        else:
                            return 2
def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


mas()
# Интерфейс
TT = 1
while TT == 1:
    print('1. Вывести информацию по человеку;')
    print('2. Вычислить возраст человека;')
    print('3. Изменить дату рождения;')
    print('4. Вывести кол-во человек в списке.')
    z = int(input('Какую провести операцию?(введите число): '))

    if z == 1:  # Вывод информации по спискам
        VM()

    elif z == 2:  # Вычисление возраста человека
        TF = FT = 1
        while TF == 1:
            A, B, C = map(int, input('Введите сегодняшнюю дату через точку(ДД.ММ.ГГГГ): ').split('.'))
            #D = DD(A, B, C)
            while FT == 1:
                i = int(input('Введите id человека: '))
                M[i].age(A, B, C)
                FT = int(input('Изменить id человека и повторить операцию?(1 - Да, 2 - нет): '))
            TF = int(input('Изменить сегодняшнюю дату и повторить операцию?(1 - Да, 2 - нет): '))

    elif z == 3:  # 3 Изменение даты рождения
        FT = 1
        while FT == 1:
            i = int(input('Введите id человека: '))
            M[i].zamena()
            FT = int(input('Изменить id человека и повторить операцию?(1 - Да, 2 - нет): '))

    elif z == 4:  # 4 Вывод кол-ва объектов
        print('В списках записано {} людей'.format(len(M)))
    TT = int(input('Выбрать другую операцию?(1 - Да, 2 - нет):'))