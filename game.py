"""
SnakeGame:

List of entity
A snake, a fruit eatable

Rules of the game
The user controls the snake from left to right and up and down in a confined area to seek fruits.
The snake grows when he eats a fruit. Only one fruit is displayed at a time.
The game is over when the snake hits the end of the area or eats itself.
"""

import time


import math
from snake import Snake, Orientation
import sys
import pygame
import pygame.font
from pygame.locals import *
from fruit import Fruit
from hud import HUD
from game_area import GameArea

class SnakeGame:
    def __init__(self) -> None:
        self.game_area = GameArea(200, 200)
        pygame.display.set_caption("Snake")
        pygame.display.flip()
        self.game_over = False
        self.snake = Snake(self.game_area.width, self.game_area.height, 5, 5)
        self.orientation = Orientation.UP
        self.fruit = Fruit(self.game_area)
        self.score = 0
        self.hud = HUD(self.game_area.width, self.game_area.height)
        self.hud.update_score(self.score)
        self.start_time = round(time.time())
        
    def check_eat(self) -> None:
        if self.snake.position[0][0] == self.fruit.position[0] and self.snake.position[0][1] == self.fruit.position[1]:
            del self.fruit
            self.fruit = Fruit(self.game_area)
            self.snake.eat()
            self.score += 1
            self.hud.update_score(self.score)
            print("Eat fruit")

    def play_game(self) -> None:
        while not self.game_over:
            orientation_key_pressed = False
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    print("User requested to quit.")
                    sys.exit()
                if event.type == pygame.KEYDOWN and not orientation_key_pressed:
                    if event.key == K_DOWN and self.orientation != Orientation.UP:
                        self.orientation = Orientation.DOWN
                        orientation_key_pressed = True
                        print("User requested to down.")
                    elif event.key == K_UP and self.orientation != Orientation.DOWN:
                        self.orientation = Orientation.UP
                        orientation_key_pressed = True
                        print("User requested to up.")
                    elif event.key == K_LEFT and self.orientation != Orientation.RIGHT:
                        self.orientation = Orientation.LEFT
                        orientation_key_pressed = True
                        print("User requested to left.")
                    elif event.key == K_RIGHT and self.orientation != Orientation.LEFT:
                        self.orientation = Orientation.RIGHT
                        orientation_key_pressed = True
                        print("User requested to right.")
                    else:
                        pass
            self.snake.update_position(self.orientation)
            self.game_over = self.game_area.check_wall_collision(self.snake) or self.snake.check_self_kill()
            self.check_eat()
            self.game_area.draw()
            current_time = round(time.time()) - self.start_time
            self.hud.update_time(current_time%60, math.trunc(current_time/60))
            self.snake.draw(self.game_area.background)
            self.fruit.draw(self.game_area.background)
            self.hud.draw(self.game_area.background)
            self.draw()
            pygame.time.delay(100)

    def draw(self) -> None:
        pygame.display.flip()
        pygame.display.set_caption("Snake, Score: " + str(self.score))
        pygame.display.update()
        pygame.time.delay(100)

if __name__ == "__main__":
    pygame.init()
    snake_game = SnakeGame()
    snake_game.play_game()