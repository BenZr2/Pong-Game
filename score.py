from turtle import Turtle


class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.points = 0

        if player == 1:
            self.goto(-150, 200)
        elif player == 2:
            self.goto(150, 200)

        self.write(str(self.points), align="center",
                   font=("Arial", 30, "normal"))

    def draw(self):
        self.write(str(self.points), align="center",
                   font=("Arial", 30, "normal"))
