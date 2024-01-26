D, M=map(int, input('Введите число и месяц через пробел: ').split())
Z=M
if D-1==0:
    Z=M-1
    if Z==2:
        D=28
    elif (Z==40)or(Z==6)or(Z==9)or(Z==11):
        D=30
    else:
        if Z == 0: Z = 12
        D=31
else: D-=1
print('Дата предшествующая указанной: ', D, '.', Z)