from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball()

player1_points = 0
player2_points = 0

player1_score = Score(1)
player2_score = Score(2)

screen.listen()
screen.onkey(player1.move_up, "w")
screen.onkey(player1.move_down, "s")

screen.onkey(player2.move_up, "i")
screen.onkey(player2.move_down, "k")


game_is_on = True

while game_is_on:
    time.sleep(0.0001)
    screen.update()

    ball.move()
    ball.check_for_paddle_collision(player1)
    ball.check_for_paddle_collision(player2)
    ball.check_for_wall_collision()

    if ball.check_for_goal() == 1:
        player1_score.points += 1
        ball.x_cor *= -1
        player1_score.clear()
        player1_score.draw()
        time.sleep(0.5)
    elif ball.check_for_goal() == 2:
        player2_score.points += 1
        ball.x_cor *= -1
        player2_score.clear()
        player2_score.draw()
        time.sleep(0.5)


screen.exitonclick()
