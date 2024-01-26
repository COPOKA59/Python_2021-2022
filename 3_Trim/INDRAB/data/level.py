from typing import List

from constants import EMPTY_SYMBOL, FLASK_HEIGHT
from data.flask import Flask


class Level:
    def __init__(self,hel, flask_array: List[Flask], flask_count, empty_flask_count, num_id=0):
        self.num_id = num_id
        self.data = flask_array
        self.flask_count = flask_count
        self.empty_flask_count = empty_flask_count
        self.move_list = []
        self.help = hel
        # self.description_of_moves = ""

        if not self.is_valid():
            raise Exception("Invalid Puzzle")

    def rep(self, flask_array: List[Flask]):

        self.data = flask_array

    def __eq__(self, other):
        for t in self.data:
            if t not in other.data:
                return False
        return True

    def is_valid(self):
        # головоломка решена, если каждый тип цвета встречается ровно в 4 четвертях из всех пробирок
        colors = dict()
        for flask in self.data:
            for color in flask.data:
                if color == EMPTY_SYMBOL:
                    continue

                if color in colors:
                    colors[color] += 1
                else:
                    colors[color] = 1

        for color in colors:
            if colors[color] != FLASK_HEIGHT:
                return False
        return True

    def is_solved(self):
        # Решена, если любая пробирка либо пуста, либо полностью заполнена только одним цветом жидкости
        return all(map(lambda flask: flask.is_solved(), self.data))
