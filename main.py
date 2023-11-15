import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard_game = Scoreboard(-200, 260)
scoreboard_game_over = Scoreboard(0, 0)
scoreboard_game.update_score()
game_car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move, "Up")

num = 0.1
count = 0
game_is_on = True
while game_is_on:
    time.sleep(num)
    screen.update()
    if player.end_of_level():
        scoreboard_game.increase_score()
        num -= 0.01
    if count == 6:
        game_car_manager.car_spawn()
        count = 0
    else:
        count += 1
    game_car_manager.cars_move()
    if game_car_manager.collides(player):
        game_is_on = False
        scoreboard_game_over.game_over()

screen.exitonclick()
