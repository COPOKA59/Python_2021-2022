import pygame as pg

# DEBUG_LOGGING = True
EMPTY_SYMBOL = '-'
FLASK_HEIGHT = 4  # высота пробирки

FPS = 15

# все цвета, используемые в качестве значений RGB
COLORS = {
    "BLACK": (0, 0, 0),
    "GRAY": (77, 77, 77),
    "WHITE": (255, 255, 255),
    "BLUE": (0, 0, 255),
    "ORANGE": (255, 153, 51),
    "MINT_GREEN": (128, 255, 128),
    "BROWN": (165, 42, 42),
    "RED": (255, 26, 26),
    "BEIGE": (244, 226, 198),
    "YELLOW": (255, 255, 0),
    "DARK_GREEN": (19, 57, 19),
    "GREEN": (0, 204, 0),
    "PINK": (255, 192, 203),
    "CYAN": (51, 204, 255),
    "PURPLE": (128, 0, 128),
    "INDIGO": (75, 0, 130),
    "VIOLET": (153, 0, 204),
    "SKY": (128, 255, 255),
    EMPTY_SYMBOL: (127, 127, 127)  # СЕРЫЙ - цвет фона по умолчанию
}

# установить цвет фона по умолчанию
BACKGROUND_COLOR = COLORS[EMPTY_SYMBOL]

# графические константы
WIDTH, HEIGHT = WINDOW_SIZE = (1400, 800)

FLASK_GRAPHIC_WIDTH, FLASK_GRAPHIC_HEIGHT = WIDTH // 16, HEIGHT // 3
FLASK_BORDER_WIDTH = 5  # толщина стенок
FLASK_BORDER_RADIUS = FLASK_GRAPHIC_WIDTH // 2  # изгиб снизу
FLASK_VISUAL_INDICATOR_OFFSET = 20  # подъем

PUZZLES_PER_ROW = 4
PUZZLES_PER_COLUMN = 4
PUZZLES_PER_PAGE = PUZZLES_PER_ROW * PUZZLES_PER_COLUMN

# pygame events
user_event_offset = 0


def define_event():
    global user_event_offset
    user_event_offset += 1
    return pg.USEREVENT + user_event_offset


# события титульной сцены
PUZZLE_SELECTION_EVENT = define_event()

# puzzle_scene events
UPDATE_FLASK_EVENT = define_event()
HINT_BUTTON_EVENT = define_event()
