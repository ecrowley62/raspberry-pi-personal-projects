from RPLCD.i2c import CharLCD

I2C_ADDRESS = '0x3f'
I2C_PORT_EXPANDER = 'PCF8574'


def main() -> None:

    # Create an interface for the LCD screen then
    # write a string to it
    lcd = CharLCD(I2C_PORT_EXPANDER, I2C_ADDRESS)
    lcd.write_string('Hello Govena')

if __name__ == '__main__':
    main()