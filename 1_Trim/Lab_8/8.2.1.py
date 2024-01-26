def fun(S, L):
    global N
    N = 0
    for i in range(len(S)):
        if S[i] == L:
            N+=1
    return (N)
    

S=input('Введите строку: ')
if S=='': print('Введена пустая строка')
else:
    L=input('Введите символ, который нужно сосчитать: ')
    if L=='': print('Не введён символ')
    else:
        print('Символ "', L, '" встречается', fun(S, L), 'раз')