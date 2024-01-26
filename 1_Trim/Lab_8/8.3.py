def fun(Sum):
    global M, i, Sum4
    i = 0
    Sum4 = 0
    while Sum != 0:
        M = Sum % 4
        Sum //= 4
        Sum4 += M * 10 ** i
        i += 1
    return Sum4


S = str(input('Введите число в системе с основанием 12:'))
S = S.upper()
Sum = 0
if S == '':
    print('Введена пустая строка')
else:
    for n in range(len(S)):
        i = len(S) - 1 - n
        if S[n] == 'A' or S[n] == 'B':
            if S[n] == 'A':
                Sum += 10 * 12 ** i
            else:
                Sum += 11 * 12 ** i
        elif '9' >= S[n] >= '0':
            N = int(S[n])
            Sum += N * 12 ** i
        else:
            print('Введены некорректные данные')
            Sum = -1
            break
    if Sum != -1:
        print('Число', S, '(в системе счисления с основанием 12) =', fun(Sum), '(в системе счисления c основанием 4)')