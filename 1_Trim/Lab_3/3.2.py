a,b,c=map(float, input('Введите три числа через пробел: ').split())
if a>=b and a>=c:
    S=b+c
elif b>=a and b>=c:
    S=a+c
else: S=a+b
print('Сумма двух наименьших чисел равна: ', S)

