#!/usr/bin/python
from typing import Tuple

# Modules for data IO
import Adafruit_DHT
from RPLCD.i2c import CharLCD

# Temp pin
TEMPERATURE_PIN = 4

def get_current_temp_humidity(pin: int = TEMPERATURE_PIN, 
                              sensor_type: int = 11
                              ) -> Tuple(float, float):
    """ Get the current temperature"""
    humidity, temp =  Adafruit_DHT.read_retry(sensor_type, pin)
    return humidity, temp

def write_to_lcd(msg: str) -> None:
    """ Write a message to a LCD screen """
    i2c_address = 0x3f
    i2c_port_expander = 'PCF8574'
    lcd = CharLCD(i2c_address, i2c_port_expander)
    lcd.write_string(msg)

def main() -> None:
    """ 
        Program for getting the current temperature then 
        writing it to an lcd display
    """
    humidity, temp = get_current_temp_humidity()
    fare_temp = temp * (9/5) + 32
    msg = f"Temp is {fare_temp} F."
    write_to_lcd(msg)

if __name__ == '__main__':
    main()