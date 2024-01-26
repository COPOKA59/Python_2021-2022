import copy

import pygame as pg
import pygame.display

from constants import UPDATE_FLASK_EVENT, HINT_BUTTON_EVENT, WIDTH
from data.level import Level
from data.graph import Graph
from graphics.scenes.puzzle.puzzle_renderer import create_flask_graphics, detect_interactions, draw_window, \
    draw_text_center_screen
from graphics.scenes.scene import SceneBase
from graphics.scenes.title import title_scene
from puzzles import puzzles
from puzzles.puzzles import story

class_name = "PuzzleScene"


class PuzzleScene(SceneBase):
    def __init__(self, game_puzzle: Level, p_id):
        SceneBase.__init__(self)
        self.p_id = p_id
        # Содержание сцены
        self.puzzle = copy.deepcopy(game_puzzle)
        self.flask_graphics = create_flask_graphics(self.puzzle)

        # инициализации по умолчанию
        self.move_counter = 0

        # авторешатель
        self.help = game_puzzle.help
        self.puzzle_solved = False
        self.puzzle_failed = False
        self.hint_button_pressed = False
        self.puzzle_solver_attempted = False
        self.solved_node_move_index = 0
        self.solved_node = None

        # widgets
        self.hint_button = None

    def ProcessInput(self, events):
        for event in events:

            # управление на мышь
            # if event.type == pg.MOUSEBUTTONDOWN:
            # detect_interactions(self.flask_graphics)

            # управление на клаву
            if event.type == pg.KEYDOWN:
                if pygame.K_a <= event.key <= pygame.K_z:
                    detect_interactions(self.flask_graphics, event.key - pygame.K_a)

                if event.key == pygame.K_F1:
                    pygame.event.post(pygame.event.Event(HINT_BUTTON_EVENT))

                if event.key == pygame.K_BACKSPACE:
                    self.SwitchToScene(title_scene.TitleScene())

            # это событие срабатывает, когда жидкость переливается из одной пробирки в другую
            if event.type == UPDATE_FLASK_EVENT:
                self.move_counter += 1

            if event.type == HINT_BUTTON_EVENT:
                self.hint_button_pressed = True

    def Update(self, screen):
        self.puzzle_solved = self.puzzle.is_solved()

        # если нажата кнопка подсказки и головоломка создана, но еще не решена, решите ее
        if self.hint_button_pressed and not self.puzzle_solver_attempted:
            self.puzzle_solver_attempted = True
            result, final_node = Graph.solve(self.puzzle)
            if result:
                if self.help == True:
                    self.solved_node = final_node
                else:
                    draw_text_center_screen(screen, 'Попробуй сам')
                    pg.time.delay(2000)
            else:
                self.puzzle_failed = True

        # если головоломка решена (через кнопку подсказки), отображать каждый ход в течение 1,5 с
        if self.hint_button_pressed and \
                self.solved_node is not None and \
                self.solved_node_move_index < len(self.solved_node.move_list):
            i, j = self.solved_node.move_list[self.solved_node_move_index]
            self.flask_graphics[i].flask.move_liquid(self.flask_graphics[j].flask)

            # обновить счетчик ходов и перейти к следующему шагу, чтобы решить
            self.move_counter += 1
            self.solved_node_move_index += 1

            # сброс кнопки подсказки, чтобы ее можно было нажать снова
            self.hint_button_pressed = False

    def Render(self, screen, events):

        # окно
        draw_window(screen, self.flask_graphics, self.move_counter)
        font = pygame.font.Font(None, 36)
        text = font.render('F1 - подсказка         Backspace - главный экран ', True, (180, 0, 0))
        screen.blit(text, (45, 50))
        text1 = font.render('      '.join(chr(ord('A') + i) for i in range(len(self.puzzle.data))), True, (180, 0, 0))
        screen.blit(text1, ((WIDTH - text1.get_width()) // 2, 710))

        if self.puzzle_solved:
            draw_text_center_screen(screen, 'Победа!')
            pg.time.delay(2000)  # через 2 секунды на главный экран
            story[self.p_id] = True
            self.SwitchToScene(title_scene.TitleScene())

        if self.puzzle_failed:
            draw_text_center_screen(screen, 'Попробуй ещё раз!')
            pg.time.delay(2000)  # через 2 секунды на главный экран

            self.SwitchToScene(title_scene.TitleScene())

        # события не должны обрабатываться здесь, но это необходимо:
        # если в методе Update вызывается обновление виджетов pygame, кнопка будет отрисовываться за экраном
        # pygame_widgets.update(events)

        # pygame.display.update()

    # очистка
    # def ClearWidgets(self):
    # logging.info(f"{class_name}: Clear Widgets")
    # widgets = WidgetHandler.getWidgets()
    # widgets.remove(self.hint_button)
