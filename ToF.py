# in powershell $env:BLINKA_MCP2221=1
# in cmd set BLINKA_MCP2221=1
import board
print(dir(board))
import adafruit_vl53l4cd
import time

i2c = board.I2C()

vl53 = adafruit_vl53l4cd.VL53L4CD(i2c)

# # OPTIONAL: can set non-default values
vl53.inter_measurement = 0
vl53.timing_budget = 200

# print("VL53L4CD Simple Test.")
# print("--------------------")
# model_id, module_type = vl53.model_info
# print("Model ID: 0x{:0X}".format(model_id))
# print("Module Type: 0x{:0X}".format(module_type))
# print("Timing Budget: {}".format(vl53.timing_budget))
# print("Inter-Measurement: {}".format(vl53.inter_measurement))
# print("--------------------")

vl53.start_ranging()

while True:
    # while not vl53.data_ready:
    #     pass
    vl53.clear_interrupt()
    print("Distance: {} cm".format(vl53.distance))
    time.sleep(0.2)