from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_pos,y_pos)
        self.write(self.score, font=("Arial", 40, "bold"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, font=("Arial", 40, "bold"))
