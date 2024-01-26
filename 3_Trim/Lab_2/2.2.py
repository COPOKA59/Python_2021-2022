# -*- coding: utf8 -*-
import random
import time

class Voin():
    def __init__(self, HP = 100, ATK = 20):
        self.HP = HP
        self.ATK = ATK

    def Fight(self, Agro):
        Agro.HP = Agro.HP - self.ATK


AA = Voin(100, 20)
BB = Voin(100, 20)

print('FIGHT !!!')
time.sleep(1)

while AA.HP > 0 and BB.HP > 0:
    if random.choice((AA, BB)) == BB:
        print('Второй бьёт первого')
        print('У первого осталось  HP = {}'.format(AA.HP))
        BB.Fight(AA)
    else:
        print('Первый бьёт второго')
        print('У второго осталось  HP = {}'.format(BB.HP))
        AA.Fight(BB)
    time.sleep(1)

if BB.HP == 0:
    print('ПЕРВЫЙ ПОБЕДИЛ !')
else:
    print('ВТОРОЙ ПОБЕДИЛ !')