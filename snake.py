from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # self.screen = Screen()
        self.snake_body_segment = []
        self.create_snake()
        self.head = self.snake_body_segment[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # self.screen.update()

    def move(self):
        for seg_num in range(len(self.snake_body_segment) - 1, 0, -1):
            new_x = self.snake_body_segment[seg_num - 1].xcor()
            new_y = self.snake_body_segment[seg_num - 1].ycor()
            self.snake_body_segment[seg_num].goto(new_x, new_y)

        self.snake_body_segment[0].forward(MOVE_DISTANCE)

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

    def add_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.goto(position)
        snake_segment.color("white")
        self.snake_body_segment.append(snake_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake_body_segment[-1].position())
