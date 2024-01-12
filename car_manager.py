from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.turtlesize(1, 2, None)
        self.shape("square")
        self.current_movement_speed = STARTING_MOVE_DISTANCE
        self.goto(x=300, y=random.randint(-250, 270))

    def move(self):
        self.forward(self.current_movement_speed)

    def increase_movement_speed(self, level):
        self.current_movement_speed += ((level - 1) * MOVE_INCREMENT)
