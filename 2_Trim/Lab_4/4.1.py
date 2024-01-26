# -*- coding: utf8 -*-

def POST(s):
    stack = []
    for i in s:
        if i in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                Z = a + b
            elif i == '-':
                Z = a - b
            elif i == '*':
                Z = a * b
            else:
                Z = a // b
            stack.append(Z)
        else:
            stack.append(int(i))
    return stack


Fin = open('input.txt', "r")
Fout = open('output.txt', "a+")

s = Fin.readline().split()
if not s:
    print('Файл пустой')
elif int(s[0]) == 0:
    print('Нулевое значение выражения')
else:
    print('Выражение равно: ', POST(s))
    Fout.write("Выражение равно: {}\n".format(POST(s)))

Fin.close()
Fout.close()