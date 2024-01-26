def fun(S, q):
    global K, z, a
    z = 0
    a = 0
    K = 0
    for i in range(len(S) - 1):
        for n in range(len(q)):
            if S[i] == q[n]:
                z = 1
            if S[i + 1] == q[n]:
                a = 1
        if a == 1 and z == 0:
            K += 1
        z = 0
        a = 0
    return K


q = ' .,:;-!?'  # const
print('Используются только такие знаки препинания: "', q, '"', sep='')
S = input('Введите строку: ')
if S == '':
    print('Введена пустая строка')
else:
    print('Слов в строке:', fun(S, q))
