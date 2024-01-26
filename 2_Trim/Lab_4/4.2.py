# -*- coding: utf8 -*-

def VV(stack):
    b = int(stack.pop())
    a = int(stack.pop())
    v = stack.pop()
    if v == '+':
        Z = a + b
    elif v == '-':
        Z = a - b
    elif v == '*':
        Z = a * b
    else:
        Z = a // b
    stack.append(Z)
    return stack

def PREF(s):
    stack = []
    for i in s:
        if i in '+-*/':
            stack.append(i)
        elif i not in '+-*/':
            a = str(stack.pop())
            stack.append(a)
            stack.append(i)
            if a not in '+-*/': # если предыдущий не знак
                stack = VV(stack)
    stack = VV(stack)
    return stack


Fin = open('input.txt', "r")
Fout = open('output.txt', "a+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
else:
    print('Выражение равно: ', PREF(s))
    Fout.write("Выражение равно: {}\n".format(PREF(s)))

Fin.close()
Fout.close()