# in powershell $env:BLINKA_MCP2221=1
# in cmd set BLINKA_MCP2221=1
# import os
# os.system('set BLINKA_MCP2221=1')
# os.system('$env:BLINKA_MCP2221=1')

# sometime the I2C ports might get messed up. unplug everything from the breadboard and wait a minute then plug back in

import time
import board
print(dir(board))
import digitalio
from numpy import invert
from threading import Event
from random import randint

def step(n, direction, dir_pin, step_pin, step_delay = 0):

    step_pin.value = False
    dir_pin.value = direction

    for i in range(n):
        step_pin.value = True
        # Event().wait(0.05)
        # Event().wait(0.0001)
        # time.sleep(10/(10**6))
        step_pin.value = False
        Event().wait(step_delay)
        # time.sleep(step_delay)
        pass


dir_pin = digitalio.DigitalInOut(board.G0)
dir_pin.direction = digitalio.Direction.OUTPUT

step_pin = digitalio.DigitalInOut(board.G1)
step_pin.direction = digitalio.Direction.OUTPUT

direction = False
while True:
    direction = invert(direction)
    Event().wait(0.5)
    n_steps = randint(1,200)
    print(direction,n_steps)
    step(n_steps, direction, dir_pin, step_pin)