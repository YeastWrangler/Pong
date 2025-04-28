from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        if direction == "left":
            x_value = -350
        else:
            x_value = 350
        self.setpos(x_value,0)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(),self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)