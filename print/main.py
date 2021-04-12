#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()
screen = ev3.screen

screen.print("HelloWorld")
screen.print("VeryVeryVeryVeryLong")
screen.print("HelloWorld2")
screen.print("HelloWorld3")
screen.print("HelloWorld4")
screen.print("HelloWorld5")

wait(5000)
