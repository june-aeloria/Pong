from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.move = 0.1
        self.x = 10
        self.y = 10

    def ball_move(self):
        x_pos = self.xcor() + self.x
        y_pos = self.ycor() + self.y
        self.goto(x_pos,y_pos)

    def bounce(self):
        self.y  *= -1
        self.move = self.move * 0.9

    def bounce_paddle(self):
        self.x *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move = 0.1
        self.x *= -1



