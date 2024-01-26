from typing import List

import pygame
import pygame as pg

from constants import WIDTH, HEIGHT, FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT, FLASK_BORDER_WIDTH, FLASK_BORDER_RADIUS, \
    FLASK_VISUAL_INDICATOR_OFFSET, UPDATE_FLASK_EVENT, COLORS, BACKGROUND_COLOR
from data.level import Level
from graphics.graphics_objects.flask_graphic import FlaskGraphic


def create_flask_graphics(puzzle: Level) -> List[FlaskGraphic]:
    # настройка графики
    n = len(puzzle.data)

    remaining_space = WIDTH - (n * FLASK_GRAPHIC_WIDTH)
    space_between_flasks = remaining_space // (n + 1)

    # нарисовать пробирки в начальном узле
    flask_graphics = []

    flask_x = space_between_flasks
    flask_y = HEIGHT // 8

    # определить, следует ли рисовать все пробирки на одной линии или в нескольких рядах
    multiple_rows = len(puzzle.data) >= 10
    flask_row_delimiter = len(puzzle.data) // 2 - 1
    multiple_row_offset = WIDTH // 8 + space_between_flasks

    if multiple_rows:
        space_between_flasks *= 2
        flask_x = multiple_row_offset
    #screen =
    # нарисовать каждую пробирку
    for flask_idx, flask in enumerate(puzzle.data):

        flask_graphic = FlaskGraphic(
            flask=flask,
            flask_x=flask_x,
            flask_y=flask_y,
            FLASK_GRAPHIC_WIDTH=FLASK_GRAPHIC_WIDTH,
            FLASK_GRAPHIC_HEIGHT=FLASK_GRAPHIC_HEIGHT,
            FLASK_BORDER_WIDTH=FLASK_BORDER_WIDTH,
            visual_indicator_offset=FLASK_VISUAL_INDICATOR_OFFSET

        )

        # перейти к следующему ряду
        if multiple_rows and flask_idx == flask_row_delimiter:
            flask_x = multiple_row_offset
            flask_y += FLASK_GRAPHIC_HEIGHT + space_between_flasks
        else:
            flask_x += FLASK_GRAPHIC_WIDTH + space_between_flasks
        flask_graphics.append(flask_graphic)
    return flask_graphics


def detect_flask_selection(flask_graphic):
    # проверьте, выбрана ли текущая графика. если да, то слегка поднимите его через flaskGraphic.raise_visual_indicator()
    mouse_focused_on_game = pg.mouse.get_focused() != 0
    left_mouse_clicked = pg.mouse.get_pressed()[0]
    mouse_flask_collision = flask_graphic.flask_graphic.collidepoint(pg.mouse.get_pos())
    flask_empty = flask_graphic.flask.is_empty()

    if mouse_focused_on_game and left_mouse_clicked and mouse_flask_collision and not flask_empty:
        flask_graphic.raise_visual_indicator()


def deselect_and_detect_flask_target(target_flask_graphic: FlaskGraphic, selected_flask_graphic: FlaskGraphic):
    # жидкость не может перетекать из колбы в саму себя
    # вместо этого рассматривайте это как отмену выбора колбы
    if target_flask_graphic.is_selected:  # проще, чем проверить, flask_graphic == selected_flask
        target_flask_graphic.lower_visual_indicator()
        return

    # определить, нажимает ли пользователь на колбу
    mouse_focused_on_game = pg.mouse.get_focused() != 0
    left_mouse_clicked = pg.mouse.get_pressed()[0]
    mouse_flask_collision = target_flask_graphic.flask_graphic.collidepoint(pg.mouse.get_pos())

    if mouse_focused_on_game and left_mouse_clicked and mouse_flask_collision:
        # перелейте жидкость, если это возможно
        if selected_flask_graphic.flask.can_move_liquid_into(target_flask_graphic.flask):
            selected_flask_graphic.flask.move_liquid(target_flask_graphic.flask)
            selected_flask_graphic.lower_visual_indicator()
            # опубликовать событие, чтобы перерисовать цвета колбы, поскольку содержимое изменилось
            pg.event.post(pg.event.Event(UPDATE_FLASK_EVENT))


def detect_interactions(flask_graphics: List[FlaskGraphic], flask_num=-1):
    any_flask_selected = any(tg.is_selected for tg in flask_graphics)
    if any_flask_selected:
        selected_flask_graphic = [tg for tg in flask_graphics if tg.is_selected][0]
    for flask_graphic in flask_graphics:
        if flask_num >= 0:
            flask_graphic_id = flask_graphics.index(flask_graphic)
            if any_flask_selected:
                # noinspection PyUnboundLocalVariable
                deselect_and_check_flask_target(selected_flask_graphic, flask_num, flask_graphic, flask_graphic_id)
            else:
                check_flask_selection(flask_num, flask_graphic, flask_graphic_id)

        else:
            # одновременно можно выбрать только одну колбу
            # если пробирка уже выбрана, следите за выбором другой пробирки в качестве целевой пробирки для перекачки жидкостей
            if any_flask_selected:
                # noinspection PyUnboundLocalVariable
                deselect_and_detect_flask_target(flask_graphic, selected_flask_graphic)
            else:
                detect_flask_selection(flask_graphic)


def check_flask_selection(flask_num, flask_graphic, flask_graphic_id):
    if flask_graphic_id == flask_num and not flask_graphic.flask.is_empty():
        flask_graphic.raise_visual_indicator()


def deselect_and_check_flask_target(selected_flask_graphic, flaskNum, flask_graphic, flask_graphic_id):
    if flask_graphic.is_selected:  # проще, чем проверить, flask_graphic == selected_flask
        flask_graphic.lower_visual_indicator()
    elif flask_graphic_id == flaskNum:
        # noinspection PyUnboundLocalVariable
        if selected_flask_graphic.flask.can_move_liquid_into(flask_graphic.flask):
            selected_flask_graphic.flask.move_liquid(flask_graphic.flask)
            selected_flask_graphic.lower_visual_indicator()
            # опубликовать событие, чтобы перерисовать цвета трубки, поскольку содержимое трубки изменилось
            pg.event.post(pg.event.Event(UPDATE_FLASK_EVENT))


def draw_flask_colors(window, flask_graphic):
    for color_idx, color_rect in enumerate(flask_graphic.color_graphics):
        # нарисуйте цвет внутри границ трубы
        drawing_last_color = color_idx == len(flask_graphic.flask.data) - 1

        # нарисовать сектор жидкости
        corresponding_color = flask_graphic.flask.data[color_idx]
        color = COLORS[corresponding_color]
        if drawing_last_color:
            pg.draw.rect(window, color, color_rect,
                         border_bottom_left_radius=FLASK_BORDER_RADIUS,
                         border_bottom_right_radius=FLASK_BORDER_RADIUS)
        else:
            pg.draw.rect(window, color, color_rect)


def draw_flasks(window, flask_graphics: List[FlaskGraphic]):
    for flask_graphic in flask_graphics:
        # нарисовать контур пробирки
        pg.draw.rect(window, COLORS["BLACK"], flask_graphic.flask_graphic, width=FLASK_BORDER_WIDTH,
                     border_bottom_left_radius=FLASK_BORDER_RADIUS, border_bottom_right_radius=FLASK_BORDER_RADIUS)

        # скрыть верхнюю границу колбы, чтобы она казалась открытой
        pg.draw.rect(window, BACKGROUND_COLOR, flask_graphic.flask_graphic_top_cover)

        # нарисовать цвета внутри трубки
        draw_flask_colors(window, flask_graphic)


#def draw_move_text(window, move_count: int):
    #font = pg.font.SysFont('helvetica', 25)
    #draw_text = font.render("Move Count: " + str(move_count), True, COLORS["BLACK"])
    #padding = 20
    #window.blit(draw_text, (padding, HEIGHT - padding - draw_text.get_height()))


def draw_window(window, flask_graphics: List[FlaskGraphic], move_count: int):
    # установить цвет фона
    window.fill(BACKGROUND_COLOR)

    #draw_move_text(window, move_count)
    draw_flasks(window, flask_graphics)


# сообщение о выигрыше\проигрыше
def draw_text_center_screen(window, text: str, font: str = 'comicsans', font_size: int = 100):
    font = pg.font.SysFont(font, font_size)
    draw_text = font.render(text, True, COLORS["WHITE"])
    window.blit(draw_text, ((WIDTH - draw_text.get_width()) // 2, (HEIGHT - draw_text.get_height()) // 2))
    pg.display.update()
