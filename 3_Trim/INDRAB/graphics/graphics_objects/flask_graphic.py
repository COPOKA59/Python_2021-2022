from typing import List

import pygame
import pygame as pg
from pygame.font import Font

from data.flask import Flask


class FlaskGraphic:
    def __init__(self, flask: Flask, flask_x, flask_y, FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT, FLASK_BORDER_WIDTH,
                 visual_indicator_offset: int):
        self.flask = flask
        self.flask_graphic = pg.Rect(flask_x, flask_y, FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT)
        self.flask_graphic_top_cover = pg.Rect(flask_x, flask_y, FLASK_GRAPHIC_WIDTH, FLASK_BORDER_WIDTH)
        self.visual_indicator_offset = visual_indicator_offset

        self.flask_x = flask_x
        self.flask_y = flask_y
        self.FLASK_GRAPHIC_WIDTH = FLASK_GRAPHIC_WIDTH
        self.FLASK_GRAPHIC_HEIGHT = FLASK_GRAPHIC_HEIGHT
        self.FLASK_BORDER_WIDTH = FLASK_BORDER_WIDTH

        self.color_graphics: List[pg.Rect] = self.get_color_graphics(flask_x, flask_y,
                                                                     FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT,
                                                                     FLASK_BORDER_WIDTH)
        self.is_selected = False

    def get_color_graphics(self, flask_x, flask_y, FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT, FLASK_BORDER_WIDTH):
        # наберите жидкости в каждой четверти колбы сверху вниз
        # в каждой пробирке по 4 единицы жидкости,
        # но они нарисованы как 1/5 часть колбы, поэтому жидкость не кажется переполненной
        color_graphics = []
        color_height_step = FLASK_GRAPHIC_HEIGHT // 5

        # первый цвет с отступом в колбу
        color_height = color_height_step
        for color_idx, color in enumerate(self.flask.data):

            drawing_last_color = color_idx == len(self.flask.data) - 1

            # убедитесь, что цвет помещается внутри изогнутого дна колбы
            current_color_height = color_height
            if drawing_last_color:
                current_color_height -= FLASK_BORDER_WIDTH

            color_rect = pg.Rect(flask_x + FLASK_BORDER_WIDTH, flask_y + current_color_height,
                                 FLASK_GRAPHIC_WIDTH - 2 * FLASK_BORDER_WIDTH, color_height_step)

            color_graphics.append(color_rect)
            # увеличить высоту, на которой будет нарисована следующая секция жидкости
            color_height += color_height_step
        return color_graphics

    def __move_visual_indicator(self, offset):
        self.flask_graphic.update(self.flask_graphic.left,
                                  self.flask_graphic.top - offset,
                                  self.flask_graphic.width,
                                  self.flask_graphic.height)
        self.flask_graphic_top_cover.update(self.flask_graphic_top_cover.left,
                                            self.flask_graphic_top_cover.top - offset,
                                            self.flask_graphic_top_cover.width,
                                            self.flask_graphic_top_cover.height)
        for cg in self.color_graphics:
            cg.update(cg.left, cg.top - offset, cg.width, cg.height)

    def raise_visual_indicator(self):
        if not self.is_selected:
            self.is_selected = True
            self.__move_visual_indicator(self.visual_indicator_offset)

    def lower_visual_indicator(self):
        if self.is_selected:
            self.is_selected = False
            self.__move_visual_indicator(self.visual_indicator_offset * -1)
