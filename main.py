from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")
player_a_score = Scoreboard("1")
player_b_score = Scoreboard("2")
ball = Ball()
ball.setheading(145)

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_on= True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.bounce()

    elif ball.xcor() >= 390:
        #score increases
        player_a_score.increase_score()
        ball.reset_position()

    elif ball.xcor() <= -390:
        #score increases
        player_b_score.increase_score()
        ball.reset_position()

    elif ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if player_b_score.score > 6:
        screen.textinput(f"Player B Wins", "Congrats")
        game_on = False
    if player_a_score.score > 6:
        screen.textinput(f"Player A Wins", "Congrats")
        game_on = False

screen.exitonclick()