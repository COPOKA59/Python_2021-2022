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
            a[j+1] = a[j]
            j -= 1
        a[j+1] = z
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

    # Удаление слов на определённую букву
    b = input('Введите первую букву, слова на которую надо удалить: ').lower()
    a = list(slov.keys())
    for i in a:
        if i[0] == b:
            del(slov[i])
    for i in slov.keys():
        Fout.write("{} - {}\n".format(i, slov[i]))

Fin.close()
Slovar.close()
Fout.close()