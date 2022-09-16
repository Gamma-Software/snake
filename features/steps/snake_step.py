from behave import *
from snake import *


@given('snake direction is up')
def step_impl(context):
    context.snake = Snake(10, 10, 1, 3)
    assert context.snake.position == [(5, 5), (5, 6), (5, 7)]
    assert context.snake.orientation == Orientation.UP

@when('snake direction is already up')
def step_impl(context):
    context.snake.update_position(Orientation.UP)

@then('snake keeps its direction’s up')
def step_impl(context):
    assert context.snake.position == [(5, 4), (5, 5), (5, 6)]
    assert context.snake.orientation == Orientation.UP

    
    
#    snake.update_position(Orientation.UP)
#    assert snake.position == [(5, 4), (5, 5), (5, 6)]
#    assert snake.orientation == Orientation.UP
#    
#    snake.update_position(Orientation.LEFT)
#    assert snake.position == [(4, 4), (5, 4), (5, 5)]
#    assert snake.orientation == Orientation.LEFT
#    
#    snake.update_position(Orientation.DOWN)
#    assert snake.position == [(4, 5), (4, 4), (5, 4)]
#    assert snake.orientation == Orientation.DOWN
#    
#    snake.update_position(Orientation.RIGHT)
#    assert snake.position == [(5, 5), (4, 5), (4, 4)]
#    assert snake.orientation == Orientation.RIGHT
#