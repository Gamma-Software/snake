import enum
import numpy as np
import pygame

class Orientation (enum.Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3

class Snake:
    def __init__(self, _width, _length, _size, _start_members) -> None:
        # Start in the center
        self.position = [(_width/2, _length/2)]
        for i in range(1, _start_members):
            self.position.append((self.position[0][0], self.position[0][1]+i*_size))
        self.orientation = Orientation.UP
        self.size = _size
        

    def update_position(self, _orientation: Orientation):
        self.orientation = _orientation

        for i in range(len(self.position)-1, 0, -1):
            self.position[i] = self.position[i-1]

        # Update the position of the head
        if self.orientation == Orientation.DOWN:
            self.position[0] = (self.position[0][0], self.position[0][1]+self.size)
        if self.orientation == Orientation.UP:
            self.position[0] = (self.position[0][0], self.position[0][1]-self.size)
        if self.orientation == Orientation.LEFT:
            self.position[0] = (self.position[0][0]-self.size, self.position[0][1])
        if self.orientation == Orientation.RIGHT:
            self.position[0] = (self.position[0][0]+self.size, self.position[0][1])

    """
    if the snake eats no need to update the position
    """
    def eat(self):
        if self.orientation == Orientation.DOWN:
            self.position.insert(0, (self.position[0][0], self.position[0][1]+self.size))
        if self.orientation == Orientation.UP:
            self.position.insert(0, (self.position[0][0], self.position[0][1]-self.size))
        if self.orientation == Orientation.LEFT:
            self.position.insert(0, (self.position[0][0]-self.size, self.position[0][1]))
        if self.orientation == Orientation.RIGHT:
            self.position.insert(0, (self.position[0][0]+self.size, self.position[0][1]))
        
    def check_self_kill(self) -> bool:
        for i in range(2, len(self.position)):
            if self.position[0] == self.position[i]:
                return True
        return False

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, pygame.Color(255, 0, 0), pygame.Rect(self.position[0][0]+1, self.position[0][1]+1, 4, 4))
        for snake_member in range(1, len(self.position)):
            pygame.draw.rect(surface, pygame.Color(200, 200, 200), pygame.Rect(self.position[snake_member][0]+1, self.position[snake_member][1]+1, 4, 4))
        pass

def test_movement():
    snake = Snake(10, 10, 1, 3)
    assert snake.position == [(5, 5), (5, 6), (5, 7)]
    assert snake.orientation == Orientation.UP
    
    snake.update_position(Orientation.UP)
    assert snake.position == [(5, 4), (5, 5), (5, 6)]
    assert snake.orientation == Orientation.UP
    
    snake.update_position(Orientation.LEFT)
    assert snake.position == [(4, 4), (5, 4), (5, 5)]
    assert snake.orientation == Orientation.LEFT
    
    snake.update_position(Orientation.DOWN)
    assert snake.position == [(4, 5), (4, 4), (5, 4)]
    assert snake.orientation == Orientation.DOWN
    
    snake.update_position(Orientation.RIGHT)
    assert snake.position == [(5, 5), (4, 5), (4, 4)]
    assert snake.orientation == Orientation.RIGHT

def test_eat():
    snake = Snake(10, 10, 1, 3)
    snake.update_position(Orientation.UP)
    snake.eat()
    assert snake.position == [(5, 3), (5, 4), (5, 5), (5, 6)]
    assert snake.orientation == Orientation.UP

def test_self_kill():
    snake = Snake(10, 10, 1, 3)
    snake.eat()
    snake.eat()
    snake.update_position(Orientation.LEFT)
    assert snake.check_self_kill() == False
    snake.update_position(Orientation.DOWN)
    assert snake.check_self_kill() == False
    snake.update_position(Orientation.RIGHT)
    assert snake.check_self_kill() == True
