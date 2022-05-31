import time
import board
print(dir(board))
import digitalio
from numpy import invert

def step(n, direction, dir_pin, step_pin, step_delay = 5000/(10**6)):

    step_pin.value = False

    for i in range(n):
        step_pin.value = True
        dir_pin.value = direction

        time.sleep(10/(10**6))
        step_pin.value = False
        time.sleep(step_delay)
        pass


dir_pin = digitalio.DigitalInOut(board.G0)
dir_pin.direction = digitalio.Direction.OUTPUT

step_pin = digitalio.DigitalInOut(board.G1)
step_pin.direction = digitalio.Direction.OUTPUT

direction = False
while True:
    direction = invert(direction)
    print(direction)
    step(200, direction, dir_pin, step_pin)