# I accidentally put 5V through the 3v system and it died so i guess it doesnt work anymore
import time
import board
from datetime import datetime
import digitalio
import analogio
print(dir(board))
import serial
uart = serial.Serial("COM3", baudrate=9600, timeout=10)
# import adafruit_hcsr04

# sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.G0, echo_pin=board.G1,_USE_PULSEIO = False)

trigger_pin = digitalio.DigitalInOut(board.G1)
trigger_pin.direction = digitalio.Direction.OUTPUT

echo_pin = digitalio.DigitalInOut(board.G2)
echo_pin.direction = digitalio.Direction.INPUT

count = 0
while True:

    initial_time = datetime.now()
    trigger_pin.value = False
    trigger_pin.value = True
    time.sleep(15/(10**6))
    trigger_pin.value = False

    count = 0
    while echo_pin.value is not True:
        count += 1
        if count > 1000:
            break
        pass

    final_time = datetime.now()

    # for i in range(100):
    #     if echo_pin.value:
    #         final_time = datetime.now()
    #         break
    #     else:
    #         final_time = initial_time

    duration = final_time - initial_time
    duration_in_s = duration.microseconds
    print(duration_in_s)

    time.sleep(0.02)

    # initial_time = datetime.now()
    # time.sleep(0.00001)
    # final_time = datetime.now()

    # duration = final_time - initial_time

    # duration_in_s = duration.total_seconds()
    # print(duration_in_s)