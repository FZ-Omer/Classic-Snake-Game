from turtle import Turtle

ALL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in ALL_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        snake = Turtle("square")
        snake.color("red")
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def reset_snake(self):
        """After moving old segments to beyond screen, it clears all previous segments and
        creates new snake segments and assigns head as its initial value"""
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def extend(self):
        self.add_segments(self.snake_segments[-1].position())

    def move(self):
        # Important and Confusing part: Explains how to move and turn the snake without deforming its shape
        # Here 3rd seg moves to 2nd seg pos and 2nd to 1st seg position, so that it follows the head[0] (1st seg)
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
# Let ME KNOW IF you BEAT my HIGHSCORE .. YAAY!!! 
