# -*- coding: utf8 -*-
from tkinter import *
from tkinter import messagebox as mb


def close():
    res = mb.askyesno('Exit', 'Вы уверены что хотите выйти?')
    if res:
        w.destroy()


def TF(x):
    for i in range(len(x)):
        if x[i] not in '.,0123456789':
            return False
        else:
            return True


def Chet(event):
    D = DE.get()
    H = HE.get()
    if D and H:
        if D.isdigit() and H.isdigit() and TF(D) and TF(H):
            PP = int(D) * int(H)
            P['text'] = 'Площадь = {} кв.м.'.format(PP)
        else:
            P['text'] = 'Площадь = ? кв.м.'


# Создание окна
w = Tk()
w.title("Площадь комнаты")
w.geometry('250x100')
w['bg'] = 'gray80'
w.resizable(width = False, height = False)
w.protocol('WM_DELETE_WINDOW', close)

#  Текст
DL = Label(w, text="Длина=", font=("Arial Bold", 12), bg = 'gray80').place(x = 10, y = 10)
HL = Label(w, text="Ширина=", font=("Arial Bold", 12), bg = 'gray80').place(x = 10, y = 35)
M1L = Label(w, text="м", font=("Arial Bold", 12), bg = 'gray80').place(x = 145, y = 10)
M2L = Label(w, text="м", font=("Arial Bold", 12), bg = 'gray80').place(x = 145, y = 35)

# Окна ввода
DE = Entry(w, font=("Arial Bold", 12))
DE.bind('<KeyRelease>', Chet)
DE.place(x = 90, y = 10, width = 50, height = 20)
HE = Entry(w, font=("Arial Bold", 12))
HE.bind('<KeyRelease>', Chet)
HE.place(x = 90, y = 35, width = 50, height = 20)

# Надпись с Площадью
P = Label(w, text = "Площадь = кв.м.", font = ("Arial Bold", 12), fg = "blue", bg = 'gray80')
P.place(x = 10, y = 65)


w.mainloop()