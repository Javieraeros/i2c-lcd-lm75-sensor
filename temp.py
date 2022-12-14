import I2C_LCD_driver
from paramiko import SSHClient
from time import *
from subprocess import check_output
from gpiozero import CPUTemperature

client = SSHClient()
client.load_system_host_keys()
#client.load_host_keys("~/.ssh/known_hosts")
#client.set_missing_host_key_policy(AutoAddPolicy())

client.connect("zero2pi", username="javi")

def get_temp():
    try:
        stdin, process, out = client.exec_command("sh scripts/lm75.sh")
        result = process.read().decode('utf-8')
    except:
        result = "Error ssh"
    stdin.close()
    process.close()
    out.close()
    return result

mylcd = I2C_LCD_driver.lcd()


while True:
    cpu = str(round(CPUTemperature().temperature, 1)).replace("\n", "") + " C"
    internal = "Internal: {}".format(cpu)
    external = "External: {}".format(get_temp())
    #print(get_temp())
    mylcd.lcd_display_string(internal, 1)
    mylcd.lcd_display_string(external, 2)
    sleep(5)
