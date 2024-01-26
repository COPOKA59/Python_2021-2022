# -*- coding: utf8 -*-

class Tree:  # Класс дерево
    pass


def Struk(k):  # Структура
    root = Tree()
    root.data = k
    root.left = None
    root.right = None
    return root


def del_Tree1(s):  # Делаем дерево слева
    Z = len(s)//2
    if Z == 0:
        tree = Struk(s[Z])
    else:
        tree = Struk(s[Z])
        tree.left = del_Tree1(s[:Z])
        if s[Z + 1:]:
            tree.right = del_Tree1(s[Z+1:])
    return tree


def del_Tree2(s):  # Делаем дерево справа
    Z = len(s)//2
    if Z == 0:
        tree = Struk(s[Z])
    else:
        tree = Struk(s[Z])
        tree.right = del_Tree2(s[:Z])
        if s[Z + 1:]:
            tree.left = del_Tree2(s[Z+1:])
    return tree


def Zerkalo(Tree):  # Создаём зеркальное дерево
    Tree.left, Tree.right = Tree.right, Tree.left
    if Tree.left:
        Zerkalo(Tree.left)
    if Tree.right:
        Zerkalo(Tree.right)


def PoZ(Tree, a=0):  # Поворот на 90 градусов и вывод на экран
    if Tree:
        PoZ(Tree.right, a + 1)
        print('   ' * a, end='')
        print(Tree.data)
        PoZ(Tree.left, a + 1)


def LKP(Tree):  # Обход дерева ЛКП
    global S
    if Tree:
        LKP(Tree.left)
        S += Tree.data + ' '
        LKP(Tree.right)


def VvoD(b):  # Ввод данных
    global s
    if a == 1:
        s = Fin.readline().split()  # Ввод строки через файл
    else:
        print('Введите данные', b, 'дерева в одну строку через пробел: ')
        s = input().split()  # Ввод строки с клавиатуры

Fin = open('input.txt', "r")

print('Как хотите ввести данные? '
      '1 - Через файл; '
      '2 - Ввод с клавиатуры.')
a = int(input('Введите число операции: '))
if a != 1 and a != 2:
    print('Введено неправильное число операции. Выполнение программы невозможно.')
else:
    b = 1
    VvoD(b)

    if not s:
        print('Нет данных. Файл или строка ввода были пусты. Выполнение программы невозможно.')
    else:
        Tree1 = del_Tree1(s)  # Создание 1 дерева
        b += 1
        VvoD(b)

        if not s:
            print('Нет данных. Файл или строка ввода были пусты. Выполнение программы невозможно.')
        else:
            Tree2 = del_Tree2(s)  # Создание 2 дерева
            print('')
            print('1 Дерево:')
            PoZ(Tree1)  # Вывод 1 дерева
            print('')
            print('2 Дерево:')
            PoZ(Tree2)  # Вывод 2 дерева

            # Отзеркаливание дерева
            Zerkalo(Tree2)
            print('')
            print('Отзеркаленное 2 дерево:')
            PoZ(Tree2)

            S = ''
            LKP(Tree1)  # LKP обход 1 дерева
            S1 = S

            S = ''
            LKP(Tree2)  # LKP обход 2 'отзеркаленного' дерева
            S2 = S

            print('')
            if S1 == S2:  # Сравнение 1 дерева и зеркального дерева
                print('Заданные деревья являются зеркальными')
            else:
                print('Заданные деревья не являются зеркальны')
Fin.close()