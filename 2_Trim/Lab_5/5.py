# -*- coding: utf8 -*-

class Tree:  # Класс дерево
    pass


def Struk(k):  # Структура
    root = Tree()
    root.data = k
    root.left = None
    root.right = None
    return root


def Pr(op):  # Приоритет операции
    P = 4
    if op in '*/': P = 2
    if op in '+-': P = 1
    return P


def PostPr(s):  # Последняя позиция
    min_P = 3
    z = -1
    for i in range(len(s)):
        P = Pr(s[i])
        if P <= min_P:
            min_P = P
            z = i
    return z


def del_Tree(s):  # Делаем дерево
    Z = PostPr(s)
    if Z < 0:
        tree = Struk(s)
    else:
        tree = Struk(s[Z])
        if s[Z] == '-' and s[:Z] == '':
            tree.left = del_Tree('0')
        else:
            tree.left = del_Tree(s[:Z])
        tree.right = del_Tree(s[Z + 1:])
    return tree


def PoZ(Tree, a=0):  # Поворот на 90 градусов и вывод на экран
    if Tree:
        PoZ(Tree.right, a + 1)
        print(' ' * a, end='')
        print(Tree.data)
        PoZ(Tree.left, a + 1)


def Vich(a, b, i):
    if i == '+':
        Z = a + b
    elif i == '-':
        Z = a - b
    elif i == '*':
        Z = a * b
    else:
        Z = a // b
    return Z


# Префиксная форма(КЛП)
def PPREF(Tree):
    global S
    if Tree:
        S += Tree.data + ' '
        PPREF(Tree.left)
        PPREF(Tree.right)


def VV(stack, a, b):  # Вычисление
    i = stack.pop()
    Z = Vich(a, b, i)
    stack.append(Z)
    return stack


def Pred(stack):  # Проверка на значение предыдущего знака. Рекурсия.
    i = str(stack.pop())
    a = str(stack.pop())
    if a not in '+-*/':  # если предыдущий не знак
        stack = VV(stack, int(a), int(i))
        if len(stack) >= 3:
            Pred(stack)
    if a in '+-*/':
        stack.append(a)
        stack.append(i)
    return stack


def PREF(s):  # Ориентирование по стеку
    stack = []
    for i in s:
        if i in '+-*/':
            stack.append(i)
        elif i not in '+-*/':
            a = str(stack.pop())
            stack.append(a)
            stack.append(i)
            stack = Pred(stack)
    return stack


# Постфиксная форма(ЛПК)
def PPOST(Tree):
    global SS
    if Tree:
        PPOST(Tree.left)
        PPOST(Tree.right)
        SS += Tree.data + ' '


def POST(s):
    stack = []
    for i in s:
        if i in '+-*/':
            b = int(stack.pop())
            a = int(stack.pop())
            Z = Vich(a, b, i)
            stack.append(Z)
        else:
            stack.append(i)
    return stack


# Вычисление значения по бинарному дереву
def VBin(Tree):
    if not Tree.left:
        return int(Tree.data)
    else:
        a = VBin(Tree.left)
        b = VBin(Tree.right)
    return int(Vich(a, b, Tree.data))


Fin = open('input.txt', "r")
Fout = open('output.txt', "a+")

s = Fin.readline()
if not s:
    print('Файл пустой')
else:
    print(s)
    Tree = del_Tree(s)  # Создание дерева
    PoZ(Tree)  # Вывод дерева
    ...
    S = ''
    PPREF(Tree)
    print('Префиксная форма: ', S)
    print('Выражение равно: ', PREF(S.split()))
    ...
    SS = ''
    PPOST(Tree)
    print('Постфиксная форма: ', SS)
    print('Выражение равно: ', POST(SS.split()))
    ...
    print('Выражение вычисленного по бинарному дереву равно: ', VBin(Tree))
    ...

Fin.close()
Fout.close()