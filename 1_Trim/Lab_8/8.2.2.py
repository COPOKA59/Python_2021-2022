def fun(S):
    global N, K
    N = 0
    K = ''
    for i in range(len(S)):
        for n in range(len(S)):
            if n != i and S[i] == S[n]:
                N = 1
        if N == 0:
            K += S[i]
        N = 0
    return K


S = input('Введите строку: ')
if S == '':
    print('Введена пустая строка')
else:
    if fun(S) == '': print('Нет символов встречающихся один раз')
    else: print('Символы встречающиеся только 1 раз', fun(S))
