import time
from turtle import Screen, Turtle
from Ball import Ball
from Paddle import Paddle
from Score_board import Scoreboard

gail = Turtle()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

screen.tracer(0)

gail.pencolor('white')
gail.penup()
gail.goto(0,300)
gail.setheading(270)
while gail.ycor() > -300:
    gail.pendown()
    gail.forward(30)
    gail.penup()
    gail.forward(30)

gail.hideturtle()

screen.update()

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
r_board = Scoreboard(150, 240)
l_board = Scoreboard(-150, 240)

screen.onkey(r_paddle.user_paddle_up, "Up")
screen.onkey(r_paddle.user_paddle_down, "Down")
screen.onkey(l_paddle.user_paddle_up, "w")
screen.onkey(l_paddle.user_paddle_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if r_paddle.distance(ball) < 50 and ball.xcor() > 330 or l_paddle.distance(ball) < 50 and l_paddle.xcor() < -330:
        ball.bounce_paddle()

    elif r_paddle.distance(ball) < 20 or l_paddle.distance(ball) < 20:
        ball.bounce_paddle()



    if ball.xcor() > 390:
        ball.reset_position()
        l_board.increase_score()

    if ball.xcor() < -390:
        ball.reset_position()
        r_board.increase_score()



screen.exitonclick()