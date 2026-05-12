from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.screen = Screen()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x_pos, y_pos)

        self.screen.update()

    def user_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def user_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

