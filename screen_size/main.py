#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait

ev3 = EV3Brick()

screen = ev3.screen

width = screen.width # 获取屏幕宽度
height = screen.height # 获取屏幕高度

screen.print("Width: " + str(width))
screen.print("Height: " + str(height))

wait(5000)

