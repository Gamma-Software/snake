from snake import Snake, Orientation
import pygame

class GameArea:
    def __init__(self, _width, _height) -> None:
        self.width = _width
        self.height = _height
        self.background = pygame.display.set_mode((self.width, self.height))
        self.background.fill((0, 0, 0))
    
    def check_wall_collision(self, _snake: Snake) -> bool:
        check_left = _snake.position[0][0] < 0
        check_right = _snake.position[0][0] > self.width
        check_top = _snake.position[0][1] < 0
        check_bottom = _snake.position[0][1] > self.height
        return check_left or check_right or check_top or check_bottom

    def draw(self):
        self.background.fill((0, 0, 0))

def test_gamearea_check_well_collision():
    game_area = GameArea(10, 10)
    snake = Snake(10, 10, 1, 3)
    snake.update_position(Orientation.UP)
    assert not game_area.check_wall_collision(snake)
    snake.update_position(Orientation.UP)
    assert not game_area.check_wall_collision(snake)
    snake.update_position(Orientation.UP)
    assert not game_area.check_wall_collision(snake)
    snake.update_position(Orientation.UP)
    assert not game_area.check_wall_collision(snake)
    snake.update_position(Orientation.UP)
    assert not game_area.check_wall_collision(snake)
    snake.update_position(Orientation.UP)
    assert game_area.check_wall_collision(snake)