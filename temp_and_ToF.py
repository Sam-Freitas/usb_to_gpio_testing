# in powershell $env:BLINKA_MCP2221=1
# in cmd set BLINKA_MCP2221=1
# import os
# os.system('set BLINKA_MCP2221=1')
# os.system('$env:BLINKA_MCP2221=1')

# sometime the I2C ports might get messed up. unplug everything from the breadboard and wait a minute then plug back in

import time
import board
import digitalio
import adafruit_pct2075
import adafruit_vl53l4cd
import sys

i2c = board.I2C()  # uses board.SCL and board.SDA
pct = adafruit_pct2075.PCT2075(i2c)

vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)

pct.high_temperature_threshold = 35.5
pct.temperature_hysteresis = 30.0
pct.high_temp_active_high = False
print("High temp alert active high? %s" % pct.high_temp_active_high)

vl53.start_ranging()

g0 = digitalio.DigitalInOut(board.G0)
g0.direction = digitalio.Direction.INPUT

while True:
    sys.stdout.flush()
    T = pct.temperature
    vl53.clear_interrupt()
    D = vl53.distance
    print("Termperature:", str(T) + "C","\t", " Distance:", str(D*10) + "mm")
    # print("Temperature: %.2f C" % pct.temperature)
    # print("Distance: {} cm".format(vl53.distance))
    # print(g0.value)
    # time.sleep(0.1)