Fin=open('../2TriM/input.txt')
s = Fin.readline().split()
max = min = int(s[0])
while True:
    s = Fin.readline().split()
    if not s:break
    a = int(s[0])
    if a > max: max=a
    if a < min: min=a
Fin.close()
S=max-min
print('Разность минимального и максимального элемента равна = ', S)