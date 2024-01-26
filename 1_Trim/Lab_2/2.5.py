a,b,c=map(int,input('Введите время(через пробел): ').split())
a2,b2,c2=map(int,input('Введите конечное время(через пробел): ').split())
p=0
if c > c2: #секунды
    p=1
    c=60+c2-c
else:
    c=c2-c
if b >= b2: #минуты
    b=60+b2-b-p
    p=1
else:
    b=b2-b-p
    p=0
if a >= a2: #часы
    a=24-a+a2-p
else:
    a=a2-a-p
print(f'Промежуток равен: {a:0{2}}:{b:0{2}}:{c:0{2}}')