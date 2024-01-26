# -*- coding: utf8 -*-
def Zapoln():
    sim = ' ,.;:?!—-\n«»()'
    word = ''
    slov = {}
    s = Fin.readline()
    while s:  # если есть слова в файле
        for i in s:
            if i in sim:  # если i символ
                if word in slov.keys():  # если есть слово в словаре
                    slov[word] += 1
                elif word != '':  # если нет слова в словаре
                    slov[word] = 1
                word = ''
            else:  # если i буква
                word += i.lower()
        s = Fin.readline()
    return slov


def SSort(a, n):
    for i in range(1, n):
        z = a[i]
        j = i - 1
        while j >= 0 and z >= a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = z
    return a


def Chast_Sort(slov):
    n = 0  # Кол-во слов
    m = []  # Частота встречаемости: список
    K = []  # Список ключевых слов
    for i in slov.keys():
        m += [slov[i]]
        K += [i]
        n += 1
    m = SSort(m, n)  # Сортировка частоты встречаемости по убыванию
    K = SSort(K, n)  # Сортировка слов по убыванию
    Sort_Y = {}  # Словарь отсортированный по убыванию частоты и по убыванию слов
    for i in m:
        for z in range(n):
            for j in slov.keys():
                if slov[j] == i and K[z] == j:
                    Sort_Y[j] = i
    return Sort_Y


class CU:
    pass


def Files(slov, f1, f2):
    import pickle
    n = 0
    m = []
    for i in slov.keys():
        n += 1
        Z = CU()
        Z.count = slov[i]
        Z.word = i
        m += [Z]

    # Запись по байтам
    F1 = open(f1, 'wb')
    for i in range(n):
        pickle.dump(m[i].count, F1)
        pickle.dump(m[i].word, F1)
    F1.close()
    # Чтение байт
    F1 = open(f1, 'rb')
    m = []
    for i in range(n):
        word = pickle.load(F1)
        count = pickle.load(F1)
        Z = CU()
        Z.count = count
        Z.word = word
        m += [Z]
    F1.close()
    # Запись словаря
    F1 = open(f1, 'w')
    for i in range(n):
        F1.write("{} - {}\n".format(m[i].count, m[i].word))
    F1.close()
    # Второй файл
    # Запись байт массива целиком
    F2 = open(f2, 'wb')
    pickle.dump(m, F2)
    F2.close()
    # Чтение байт целиком
    m = []
    F2 = open(f2, 'rb')
    m = pickle.load(F2)
    F2.close()
    # Запись словаря
    F2 = open(f2, 'w')
    for i in range(n):
        F2.write("{} - {}\n".format(m[i].count, m[i].word))
    F2.close()


Fin = open('input.txt', "r")
Slovar = open('slovar.txt', "w")
Fout = open('output.txt', "w")

slov = Zapoln()
if not slov:
    print('Файл пустой')
else:
    print(slov)

    slov = Chast_Sort(slov)
    print(slov)
    # Занесения словаря в файл
    Slovar.write("Словарь упорядоченный по убыванию частоты встречаемости:\n")
    for i in slov.keys():
        Slovar.write("{} - {}\n".format(i, slov[i]))

    Files(slov, 'F1.txt', 'F2.txt')

    # Удаление слов на определённую букву
    b = input('Введите первую букву, слова на которую надо удалить: ').lower()
    a = list(slov.keys())
    for i in a:
        if i[0] == b:
            del (slov[i])
    for i in slov.keys():
        Fout.write("{} - {}\n".format(i, slov[i]))

Fin.close()
Slovar.close()
Fout.close()
