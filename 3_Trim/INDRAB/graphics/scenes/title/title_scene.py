import pygame
import pygame_widgets

from constants import *
from graphics.graphics_objects.puzzle_selection_graphic import PuzzleSelectionGraphic
from graphics.scenes.puzzle import puzzle_scene
from graphics.scenes.scene import SceneBase
from puzzles import puzzles


class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        # переменные по умолчанию
        self.puzzle_selection_graphic = None

    def ProcessInput(self, events):
        for event in events:

            #кнопки мышью
            #if event.type == PUZZLE_SELECTION_EVENT:
                #puzzle_id = event.__dict__["puzzle_id"]

            #клавиатура
            if event.type == pg.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:

                    # получить головоломку по идентификатору и переключиться на сцену головоломки
                    next_puzzle = puzzles.get_puzzle(event.key - pygame.K_0)
                    self.SwitchToScene(puzzle_scene.PuzzleScene(next_puzzle,event.key - pygame.K_0))

    def Update(self,screen):
        pass

    def Render(self, screen, events):
        # фон
        screen.fill(BACKGROUND_COLOR)

        Font = pygame.font.Font(None, 36)
        text = Font.render('Выход ESC или Alt+F4', True, (180, 0, 0))
        screen.blit(text, (45, 50))

        # здесь создаются кнопки выбора пазла
        if self.puzzle_selection_graphic is None:
            self.puzzle_selection_graphic = PuzzleSelectionGraphic(screen)

        # нарисовать фон выбора пазла
        pygame.draw.rect(screen, self.puzzle_selection_graphic.mid_background_color,
                         self.puzzle_selection_graphic.mid_background_rect)

        # рисовать кнопки выбора пазла
        pygame_widgets.update(events)

    #def ClearWidgets(self):
        #self.puzzle_selection_graphic.clear_widgets()
