"""
SnakeGame:

List of entity
A snake, a fruit eatable

Rules of the game
The user controls the snake from left to right and up and down in a confined area to seek fruits.
The snake grows when he eats a fruit. Only one fruit is displayed at a time.
The game is over when the snake hits the end of the area or eats itself.
"""

from curses import KEY_LEFT, KEY_RIGHT
from nis import match
from construct import Switch
import numpy as np
import random
from snake import Snake, Orientation
import sys
import time
import pygame
import pygame.font
from pygame.locals import *

class GameArea:
    def __init__(self, _width, _height) -> None:
        self.width = _width
        self.height = _height
    
    def check_wall_collision(self, _snake: Snake) -> None:
        return True

    def draw():
        pass

class SnakeGame:
    def __init__(self) -> None:
        self.game_area = GameArea(500, 500)
        self.screen = pygame.display.set_mode((self.game_area.width, self.game_area.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))
        pygame.display.set_caption("Snake")
        pygame.display.flip()
        self.game_over = False
        self.snake = Snake(self.game_area.width, self.game_area.height, 5, 100)
        self.orientation = Orientation.UP
        self.fruit = [0, 0]
        self.score = 0
        # random fruit position discretize to 5x5
        self.fruit[0] = np.linspace(0, self.game_area.width, num=self.game_area.width//5, endpoint=False, dtype=int)[random.randint(0, self.game_area.width//5-1)]
        self.fruit[1] = np.linspace(0, self.game_area.width, num=self.game_area.height//5, endpoint=False, dtype=int)[random.randint(0, self.game_area.width//5-1)]

    def check_eat(self) -> None:
        if self.snake.position[0][0] == self.fruit[0] and self.snake.position[0][1] == self.fruit[1]:
            self.fruit[0] = np.linspace(0, self.game_area.width, num=self.game_area.width//5, endpoint=False, dtype=int)[random.randint(0, self.game_area.width//5-1)]
            self.fruit[1] = np.linspace(0, self.game_area.width, num=self.game_area.height//5, endpoint=False, dtype=int)[random.randint(0, self.game_area.width//5-1)]
            self.snake.eat()
            self.score += 1
            print("Eat fruit")

    def play_game(self) -> None:
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    print("User requested to quit.")
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN and self.orientation != Orientation.UP:
                        self.orientation = Orientation.DOWN
                        print("User requested to down.")
                    elif event.key == K_UP and self.orientation != Orientation.DOWN:
                        self.orientation = Orientation.UP
                        print("User requested to up.")
                    elif event.key == K_LEFT and self.orientation != Orientation.RIGHT:
                        self.orientation = Orientation.LEFT
                        print("User requested to left.")
                    elif event.key == K_RIGHT and self.orientation != Orientation.LEFT:
                        self.orientation = Orientation.RIGHT
                        print("User requested to right.")
                    else:
                        pass
            self.snake.update_position(self.orientation)
            self.game_over = self.game_area.check_wall_collision(self.snake.position)
            self.game_over = self.snake.check_self_kill()
            self.check_eat()
            self.screen.fill([0, 0, 0])
            pygame.draw.rect(self.screen, pygame.Color(255, 0, 0), pygame.Rect(self.snake.position[0][0]+1, self.snake.position[0][1]+1, 4, 4))
            for snake_member in range(1, len(self.snake.position)):
                pygame.draw.rect(self.screen, pygame.Color(200, 200, 200), pygame.Rect(self.snake.position[snake_member][0]+1, self.snake.position[snake_member][1]+1, 4, 4))
            pygame.draw.rect(self.screen, pygame.Color(0, 255, 0), pygame.Rect(self.fruit[0], self.fruit[1], 5, 5))
            if pygame.font:
                font = pygame.font.Font(None, 64)
                text = font.render("Score: " + str(self.score), True, (255, 255, 255))
                textpos = text.get_rect(centerx=self.background.get_width() / 2, y=10)
                self.background.blit(text, textpos)
            pygame.display.set_caption("Snake, Score: " + str(self.score))
            pygame.display.update()
            pygame.time.delay(100)

pygame.init()
snake_game = SnakeGame()
snake_game.play_game()