from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.player = direction
        if direction == "1":
            xcor = -280

        else:
            xcor = 260
        self.penup()
        self.setpos(xcor, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Player {self.player}: {self.score}", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()