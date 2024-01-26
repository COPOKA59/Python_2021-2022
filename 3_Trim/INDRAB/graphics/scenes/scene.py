import pygame

from constants import WIDTH, HEIGHT, FPS
import graphics.scenes.title.title_scene as title_scene


class SceneBase:
    def __init__(self):
        self.next = self

    def ClearWidgets(self):
        pass

    # очистить и на след сцену
    def SwitchToScene(self, next_scene):
        # self.ClearWidgets()
        self.next = next_scene