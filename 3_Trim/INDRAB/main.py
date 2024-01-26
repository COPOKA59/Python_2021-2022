import pygame

from constants import *
from graphics.scenes.title import title_scene


def run_game(width, height, fps, starting_scene):
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    active_scene = starting_scene

    # начало тут
    while active_scene is not None:

        # нажатие на клавишу
        pressed_keys = pygame.key.get_pressed()

        filtered_events = []

        # Выход на esc или alt+f4
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene()
            else:
                filtered_events.append(event)

        active_scene.ProcessInput(filtered_events)

        active_scene.Update(screen)

        active_scene.Render(screen, filtered_events)

        active_scene = active_scene.next

        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__':
    run_game(WIDTH, HEIGHT, FPS, title_scene.TitleScene())
