import numpy as np
import pygame
import random
from game_area import GameArea

class Fruit:
    def __init__(self, _game_area: GameArea) -> None:
        print("fruit: spawn")
        self.position = [
            np.linspace(0, _game_area.width, num=_game_area.width//5, endpoint=False, dtype=int)[random.randint(0, _game_area.width//5-1)],
            np.linspace(0, _game_area.width, num=_game_area.height//5, endpoint=False, dtype=int)[random.randint(0, _game_area.width//5-1)]]

    def __del__(self):
        print("fruit: eaten")

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 5, 5))