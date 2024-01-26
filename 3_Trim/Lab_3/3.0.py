# -*- coding: utf8 -*-
class Tpeople:  # Класс человек

    def __init__(self, fio, DR, pol):  # Начальные настройки
        self.fio = fio
        self.__DR = DR  # 1. Инкапсуляция
        self.pol = pol

    def VD(self):  # Вывод инкапсулированной даты
        return self.__DR

    def age(self, A, B, C):  # Вычисление возраста человека
        s = str(self.__DR).split('.')
        a = int(s[0])
        b = int(s[1])
        c = int(s[2])
        if DATA(a, b, c):
            Z0 = C - c # Вычисление года
            if b > B:  # Если родился позже указанного месяца
                Z0 -= 1
                Z1 = 11 - (b - B)
                Z2 = 11 - (a - A)
            elif b == B:  # Если в этот месяц
                Z1 = 0
                if a > A:  # Если родился позже указанного числа
                    Z0 -= 1
                    Z1 = 11
                    Z2 = A
                elif a == A:
                    Z2 = 0
                else:
                    Z2 = A - a
            else:  # Если в раний месяц
                Z1 = B - b
                Z2 = A - a
            print("{} лет, {} месяц(-ев), {} дней".format(Z0, Z1, Z2))
        else:
            print('Данныес в списках не корректны')

    def zamena(self):  # Изменить дату рождения
        print('Дата рождения:', self.__DR)
        a, b, c = map(str, input('Запишите изменённую дату через точку:').split('.'))
        if DATA(a, b, c):
            self.__DR = str(a) + '.' + str(b) + '.' + str(c)
            print("Изменённая запись: {} {} {}".format(self.fio, self.__DR, self.pol))
        else:
            print('Данные не корректны')

    # 3. Свойство выводить нужного человека
    v = property((lambda x: print(x.fio, x.__DR, x.pol) ))

    # 4. Свойство позволяет только менять фамилию человека
    def zamfio(self):
        print('Данные для замены:', self.fio)
        self.fio = input('Введите изменённые ФИО')
    v = property(lambda x: x.fio, zamfio)


def DATA(DD, MM, G):  # 2. Проверка даты, День, Месяц, Год
    if isint(DD) and isint(MM) and isint(G):
        G = int(G)
        MM = int(MM)
        DD = int(DD)
        if MM > 0 and MM < 13:  # Проверка 0<Месяца<13
            if MM == 1 or MM == 3 or MM == 5 or MM == 7 or MM == 8 or MM == 10 or MM == 12:
                if DD > 0 and DD < 32:  # День не больше 31
                    return True
                else:
                    print('День указан не верно')
                    return False
            if MM == 4 or MM == 6 or MM == 9 or MM == 11:
                if DD > 0 and DD < 31:  # День не больше 30
                    return True
                else:
                    print('День указан не верно')
                    return False
            if MM == 2:
                if G % 4 == 0:
                    if DD > 0 and DD < 30:  # День не больше 29
                        return True
                    else:
                        print('День указан не верно')
                        return False
                else:
                    if DD > 0 and DD < 29:  # День не больше 28
                        return True
                    else:
                        print('День указан не верно')
                        return False
        else:
            print('Месяц указан не верно')
            return False
    else:
        print('Введённые данные не корректны')
        return False


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


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
                print('id = {}, ФИО = {}, Дата рождения = {}, Пол = {}'.format(i, M[i].fio, M[i].VD(), M[i].pol))
        elif z == 2:
            i = int(input('Введите id человека: '))
            print('id = {}, ФИО = {}, Дата рождения = {}, Пол = {}'.format(i, M[i].fio, M[i].VD(), M[i].pol))
        elif z == 3:
            FT = 1
            while FT == 1:  # 5 Вывод всех атрибутов объектов
                print('1. ФИО')
                print('2. Дата рождения')
                print('3. Пол')
                i = int(input('Выберите атрибут(введите число): '))
                if i == 1:
                    for i in range(len(M)):
                        print('id = {}, ФИО = {}'.format(i, M[i].fio))
                elif i == 2:
                    for i in range(len(M)):
                        print('id = {}, Дата рождения = {}'.format(i, M[i].VD()))
                elif i == 3:
                    for i in range(len(M)):
                        print('id = {}, Пол = {}'.format(i, M[i].pol))
                FT = int(input('Выбрат другой атрибут?(1 - Да, 2 - нет): '))
        TF = int(input('Повторить операцию?(1 - Да, 2 - нет): '))


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
        TF = 1
        while TF == 1:
            A, B, C = map(int, input('Введите сегодняшнюю дату через точку(ДД.ММ.ГГГГ): ').split('.'))
            a = DATA(A, B, C)
            FT = 1
            while FT == 1 and a:
                i = int(input('Введите id человека: '))
                M[i].age(int(A), int(B), int(C))
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
