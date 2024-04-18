from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"{self.left_score}      {self.right_score}", align="center", font=("Geometric", 24, "normal"))
        self.center_line()

    def center_line(self):
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(50):
            self.forward(6)
            self.pendown()
            self.forward(6)
            self.penup()

    def right_scores(self):
        self.right_score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.left_score}      {self.right_score}", align="center", font=("Geometric", 24, "normal"))
        self.center_line()

    def left_scores(self):
        self.left_score += 1
        self.clear()
        self.goto(0, 260)
        self.write(f"{self.left_score}      {self.right_score}", align="center", font=("Geometric", 24, "normal"))
        self.center_line()
