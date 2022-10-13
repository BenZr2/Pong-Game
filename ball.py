from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed(2)
        self.x_cor = 2
        self.y_cor = 3

    def move(self):
        new_x = self.pos()[0] + self.x_cor
        new_y = self.pos()[1] + self.y_cor
        self.goto(new_x, new_y)

    def check_for_paddle_collision(self, paddle):
        if (self.distance(paddle) < 32) and ((self.pos()[0] == 278) or (self.pos()[0] == -278)):
            self.x_cor *= -1

    def check_for_wall_collision(self):
        if (self.pos()[1] > 240) or (self.pos()[1] < -240):
            self.y_cor *= -1

    def check_for_goal(self):
        if self.pos()[0] > 300:
            self.goto(0, 0)
            return 1
        elif self.pos()[0] < -300:
            self.goto(0, 0)
            return 2
