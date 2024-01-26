# -*- coding: utf8 -*-
from tkinter import *
from tkinter import messagebox as mb


def close():
    res = mb.askyesno('Exit', 'Вы уверены что хотите выйти?')
    if res:
        w.destroy()


def TF(x):
    for i in range(len(x)):
        if x[i] not in '.,-0123456789':
            return False
        else:
            return True


def Chet(event):
    D = DE.get()
    H = HE.get()
    if D and H:
        if TF(D) and TF(H):
            D = float(D)
            H = float(H)
            if event == 1:
                P['text'] = str(D + H)
            elif event == 2:
                P['text'] = str(D - H)
            elif event == 3:
                P['text'] = str(D * H)
            elif H != 0:
                P['text'] = str(D / H)
            else:
                P['text'] = 'Ошибка: деление на 0'
        else:
            P['text'] = 'Ошибка ввода данных'


# Создание окна
w = Tk()
w.title("Калькулятор")
w.geometry('200x200')
w['bg'] = 'gray80'
w.resizable(width = False, height = False)
w.protocol('WM_DELETE_WINDOW', close)

# Окна ввода
DE = Entry(w, font=("Arial Bold", 12))
DE.bind('<Return>', Chet)
DE.place(x = 10, y = 10, width = 180, height = 20)
HE = Entry(w, font=("Arial Bold", 12))
HE.bind('<Return>', Chet)
HE.place(x = 10, y = 35, width = 180, height = 20)

# Кнопки
but1 = Button(text = '+', command = lambda: Chet(1)).place(x = 10, y = 65, width = 180, height = 20)

but2 = Button(text = '-', command = lambda: Chet(2)).place(x = 10, y = 90, width = 180, height = 20)

but3 = Button(text = '*', command = lambda: Chet(3)).place(x = 10, y = 115, width = 180, height = 20)

but4 = Button(text = '/', command = lambda: Chet(4)).place(x = 10, y = 140, width = 180, height = 20)

# Надпись
P = Label(w, text = "", font = ("Arial Bold", 12), bg = 'gray80')
P.place(x = 10, y = 165)


w.mainloop()