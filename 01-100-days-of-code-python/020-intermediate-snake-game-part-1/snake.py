from turtle import Turtle

MOVE_DISTANCE = 25
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake = []
        self._create_snake()
        self.head = self.snake[0]

    def _create_snake(self):
        for _ in range(0, 3):
            self.add_segment()

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        if self.snake:
            new_segment.setx(self.snake[-1].xcor() - 25)
        self.snake.append(new_segment)

    def move(self):
        for segment_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_num - 1].xcor()
            new_y = self.snake[segment_num - 1].ycor()
            self.snake[segment_num].goto(new_x, new_y)
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
