from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.title("CRUZ SNAKE GAME")
screen.bgcolor("black")
screen.setup(width=600, height=600)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect Collision with Tail
    for segment in snake.snake_segments[1:]:
        # Usually segment value will be the value of head. So it considers as it's collided.
        # To avoid that we should check segment should not be the head.
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()
