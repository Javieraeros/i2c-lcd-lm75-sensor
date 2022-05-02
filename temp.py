import I2C_LCD_driver
from time import *
from subprocess import check_output
from gpiozero import CPUTemperature

def get_temp():
    process = check_output(['ssh', 'javi@zero2pi', 'sh', 'scripts/lm75.sh'])
    return process.decode('utf-8')

mylcd = I2C_LCD_driver.lcd()

while True:
    cpu = str(round(CPUTemperature().temperature, 1)).replace("\n", "") + " C"
    internal = "Internal: {}".format(cpu)
    external = "External: {}".format(get_temp())
    print(get_temp())
    mylcd.lcd_display_string(internal, 1)
    mylcd.lcd_display_string(external, 2)
    sleep(5)
