from copy import deepcopy

from constants import FLASK_HEIGHT, EMPTY_SYMBOL
from data.level import Level
from data.flask import Flask


class Graph:
    def __init__(self, start_node: Level):
        self.start_node = start_node
        # все узлы должны иметь одинаковое количество колб
        self.flask_count = start_node.flask_count

        self.final_node = self.generate_final_state()

    def generate_final_state(self):
        # построить конечное состояние графа из начального состояния
        colors = set()
        for flask in self.start_node.data:
            for color in flask.data:
                colors.add(color)
        colors -= set(EMPTY_SYMBOL)  # исключить пустой символ из рассмотрения

        number_empty_flasks = self.flask_count - len(colors)

        final_flasks = [Flask([EMPTY_SYMBOL] * FLASK_HEIGHT)] * number_empty_flasks
        for color in colors:
            final_flask = Flask([color] * FLASK_HEIGHT)
            final_flasks.append(final_flask)

        return Level(final_flasks, self.flask_count, number_empty_flasks)

    @staticmethod
    def solve(start_node: Level, path=None) -> (bool, Level):
        """
        решает головоломку
        :param start_node:
        :param path:
        :return: (boolean: была ли решена головоломка?, путь: список узлов, которые повторяются для решения головоломки)
        """

        # базовый случай: если головоломка решена, остановитесь
        if path is None:
            path = []
        if start_node.is_solved():
            return True, path[-1]

        # обнаружить циклы: если текущий узел уже обнаружен, остановить рекурсию
        if start_node in path and path.index(start_node) != len(path) - 1:
            return False, path[-1]

        # перебрать все возможные ходы
        for i, flask_one in enumerate(start_node.data):
            for j, flask_two in enumerate(start_node.data[i+1:], start=(i+1)):
                # проверьте, можно ли перекачивать жидкость из первой трубки во вторую или наоборот
                if flask_one.can_move_liquid_into(flask_two):
                    # узел глубокого копирования
                    copy_node = deepcopy(start_node)
                    # переместите жидкость в скопированном узле и обновите описание пути
                    copy_node.move_list += [(i, j)]
                    copy_node.data[i].move_liquid(copy_node.data[j])
                    # рекурсивное решение
                    result, final_node = Graph.solve(copy_node, path + [copy_node])
                    if result:
                        return True, final_node
                if flask_two.can_move_liquid_into(flask_one):
                    # узел глубокого копирования
                    copy_node = deepcopy(start_node)
                    # переместить жидкость в скопированном узле
                    copy_node.move_list += [(j, i)]
                    copy_node.data[j].move_liquid(copy_node.data[i])
                    # рекурсивное решение
                    result, final_node = Graph.solve(copy_node, path + [copy_node])
                    if result:
                        return True, final_node

        return False, None
