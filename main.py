from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Classic")
screen.tracer(0)

# Code below deprecated > see snake class @ snake.py
# snake_body_segment = []
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# for position in starting_positions:
#     snake_segment = Turtle(shape="square")
#     snake_segment.penup()
#     snake_segment.goto(position)
#     snake_segment.color("white")
#     snake_body_segment.append(snake_segment)

# Objects Created
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Code below deprecated > see snake class @ snake.py
    # for seg_num in range(len(snake_body_segment) - 1, 0, -1):
    #     new_x = snake_body_segment[seg_num - 1].xcor()
    #     new_y = snake_body_segment[seg_num - 1].ycor()
    #     snake_body_segment[seg_num].goto(new_x, new_y)
    #
    # snake_body_segment[0].forward(20)

    snake.move()
    # Detect Collision with food, and adding score when collision detected with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect Collision with snake own body part(s)
    for segment in snake.snake_body_segment[1:]:
        # if segment == snake.head:
        #     pass

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail :
        # Trigger game_over sequence

screen.exitonclick()
