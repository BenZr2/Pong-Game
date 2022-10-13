from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player=1):
        super().__init__()
        self.player = player
        self.shape("square")
        self.left(90)
        self.shapesize(0.5, 3)
        self.penup()
        self.color("white")

        if player == 1:
            self.goto(-280, 0)
        elif player == 2:
            self.goto(280, 0)

    def move_up(self):
        if self.pos()[1] < 205:
            self.forward(20)

    def move_down(self):
        if self.pos()[1] > -205:
            self.backward(20)
