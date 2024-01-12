from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level_count = 1
        self.hideturtle()
        self.goto(-280, 260)
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level_count}", False, "left", FONT)

    def update_level(self):
        self.level_count += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, "center", FONT)



