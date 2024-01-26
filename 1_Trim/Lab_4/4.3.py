print('Введите числа из последовательности через enter:')
n = int(input())
max=n
min=n
while n!=0:
    n = int(input())
    if n > max: max = n
    if n < min and n!=0: min = n
print('Разность максимального и минимального элемента  =', max - min)