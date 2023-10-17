import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.01)
    car_manager.move_cars()

    if player.ycor() > 280:
        player.goto(player.xcor(), -290)
        car_manager.increase_difficulty()
        scoreboard.increase_level()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_orver()

    screen.update()

screen.exitonclick()