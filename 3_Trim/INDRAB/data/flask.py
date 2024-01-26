from __future__ import annotations
from typing import List

from constants import FLASK_HEIGHT, EMPTY_SYMBOL


class Flask:
    def __init__(self, flask_array: List[str]):
        if len(flask_array) < FLASK_HEIGHT:
            flask_array = [EMPTY_SYMBOL] * (FLASK_HEIGHT - len(flask_array)) + flask_array
        self.data = flask_array

    def __eq__(self, other):
        return self.data == other.data

    def is_solved(self):
        colors = set(self.data)
        return self.data.count(self.data[0]) == FLASK_HEIGHT or len(colors) == 0

    def is_empty(self):
        return all(x == EMPTY_SYMBOL for x in self.data)

    # возврат жидкости в верхнюю часть колбы и сколько единиц она занимает
    def top(self):
        """
        определите жидкость в верхней части этой пробирки
        :return: (жидкость в верхней части этой пробирки, высота этой жидкости, базовый уровень этой жидкости на основе 0)
        """
        # найти первую непустую единицу в пробирке
        first_color = ''
        first_color_index = -1
        for i, color in enumerate(self.data):
            if color != EMPTY_SYMBOL:
                first_color_index, first_color = i, color
                break

        # если не было найдено ни одного непустого блока, эта пробирка пуста
        if first_color_index == -1:
            return EMPTY_SYMBOL, 0, FLASK_HEIGHT - 1

        # найден непустой блок, эта пробирка непустая:
        # определить высоту цвета
        color_height = 1
        color_base = first_color_index
        for i, color in enumerate(self.data[first_color_index + 1:], start=first_color_index + 1):
            if color == EMPTY_SYMBOL:
                continue
            elif color == first_color:
                color_height += 1
                color_base = i
            # если цвет «иссякнет», выйти из цикла
            else:
                break

        return first_color, color_height, color_base

    def can_move_liquid_into(self, other: Flask) -> bool:
        """
        определить, можно ли переместить жидкость из одной колбы в другую
        сделать ход:
             - жидкость не может попасть ни в наполненную колбу, ни из нее
             - жидкость можно переливать из одной пробирки в другую
                 если жидкость в верхней части обеих колб одного типа
             - при выполнении хода столько однотипной жидкости в верхней части трубки
                 переносится в другую пробирку, если целевая пробирка способна удерживать жидкость
        :param другое целевая колба
        :return: истина, если верхняя жидкость в себе может быть перенесена в другую колбу, в противном случае ложь
        """
        self_color, self_height, self_color_base = self.top()
        other_color, other_height, other_color_base = other.top()

        # не может выйти из себя, если пуст
        if self_color == EMPTY_SYMBOL:
            return False

        # всегда можно перейти в другой, если другой пуст
        if other_color == EMPTY_SYMBOL:
            return True

        # оба не пусты: условие переноса
        # жидкость может быть перенесена, если они имеют одинаковый верхний цвет И если целевая пробирка имеет хотя бы свободную
        return self_color == other_color and (other_color_base + 1 - other_height) > 0

    def move_liquid(self, other: Flask):
        """
        перемещает жидкость из одной колбы в другую, в то время как он может перемещать эту жидкость.
        ничего не делает, если жидкость нельзя перемещать
        :param другое: целевая колба
        :return: nothing
        """
        while self.can_move_liquid_into(other):
            self_color, self_height, self_color_base = self.top()
            other_color, other_height, other_color_base = other.top()

            self.data[self_color_base + 1 - self_height] = EMPTY_SYMBOL
            # установить верхнее значение «другое» на self_color — нельзя использовать other_color, потому что other_color может быть EMPTY_SYMBOL
            other.data[other_color_base - other_height] = self_color
