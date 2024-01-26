# -*- coding: utf8 -*-
from tkinter import *

def Shest(x):
    x = int(x)
    s = '0123456789abcdef'
    res = ''
    if x == 0:
        res = 0
    else:
        while x != 0:
            res = s[x % 16] + res
            x //= 16
    return res


def New_color(event):
    R = RE.get()
    G = GE.get()
    B = BE.get()
    if R and G and B:
        if R.isdigit() and G.isdigit() and B.isdigit() and (-1 < int(R) < 256) and (-1 < int(G) < 256) and (-1 < int(B) < 256):
            R = Shest(R)
            G = Shest(G)
            B = Shest(B)
            Color = '#' + str(R) + str(G) + str(B)
            TColor['text'] = Color
            TColor['font'] = ("Arial Bold", 16)
            CoLo['bg'] = Color
        else:
            TColor['text'] = 'Ошибка: не входит в диапозон значений'
            TColor['font'] = ("Arial Bold", 8)
            CoLo['bg'] = 'gray80'
    else:
        TColor['text'] = 'Ошибка: неккоректные данные'
        TColor['font'] = ("Arial Bold", 8)
        CoLo['bg'] = 'gray80'


# Создание окна
w = Tk()
w.title("RGB-кодирование")
w.geometry('350x100')
w['bg'] = 'gray80'

#  Текст RGB
RL = Label(w, text="R=", font=("Arial Bold", 18), bg = 'gray80').place(x = 10, y = 10)
GL = Label(w, text="G=", font=("Arial Bold", 18), bg = 'gray80').place(x = 10, y = 35)
BL = Label(w, text="B=", font=("Arial Bold", 18), bg = 'gray80').place(x = 10, y = 60)
# Окна ввода RGB
RE = Entry(w, font=("Arial Bold", 12))
RE.bind('<Return>', New_color)
RE.place(x = 60, y = 15, width = 50, height = 20)
GE = Entry(w, font=("Arial Bold", 12))
GE.bind('<Return>', New_color)
GE.place(x = 60, y = 40, width = 50, height = 20)
BE = Entry(w, font=("Arial Bold", 12))
BE.bind('<Return>', New_color)
BE.place(x = 60, y = 65, width = 50, height = 20)
# Надпись с номером цвета
TColor = Label(w, text = "#7b3850", font = ("Arial Bold", 16), fg = "blue", bg = 'gray80')
TColor.place(x = 120, y = 14)
# Вывод цвета
CoLo = Label(w, text = "", bg = '#7b3850')
CoLo.place(x = 120, y = 42, width = 100, height = 43)

w.mainloop()