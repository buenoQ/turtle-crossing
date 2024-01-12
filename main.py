import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# sets up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# makes player object
player = Player()

# make cars list which is used to store CarManager objects and then will have the counter and timer to randomly add
# cars to the screen
cars = []
car_spawn_counter = 0
car_spawn_timer = random.randint(1, 5)

scoreboard = Scoreboard()

# listens to player inputs and will move
screen.listen()
screen.onkey(player.move, "Up")

# runs game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # spawns cars at a random rate
    if len(cars) == 0:
        cars.append(CarManager())
    elif car_spawn_counter == car_spawn_timer:
        cars.append(CarManager())
        cars[-1].increase_movement_speed(scoreboard.level_count)
        car_spawn_counter = 0
        car_spawn_timer = random.randint(1, 5)
    else:
        car_spawn_counter += 1

    # move cars, gets rid of car from cars list if it goes past the left edge of the screen, checks for collisions with
    # player
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

        if car.xcor() < -350:
            car.hideturtle()
            cars.remove(car)

    # resets player if he reaches end of screen, updates level, and increases movement speed of cars
    if player.ycor() > 280:
        player.reset_turtle()
        scoreboard.update_level()
        for car in cars:
            car.increase_movement_speed(scoreboard.level_count)


screen.exitonclick()
