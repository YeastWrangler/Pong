from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x,new_y)
    def bounce(self):
        self.y_move *= -1
    def paddle_bounce(self):
        self.x_move *= -1
        if self.x_move > 0:
            self.x_move += 3
        else:
            self.x_move -= 3

    def reset_position(self):
        self.setposition(0,0)
        if self.x_move > 0:
            self.x_move = -10
        else:
            self.x_move = 10




