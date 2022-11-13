#!/usr/bin/python
import time

# Custom modules
from src.simple_pi_io.interfaces import SimpleGpio

# Default sleep time
SLEEP_FOR = 0.3

# Default GPIO pin connected to the led
DEFAULT_PIN = 15

# Simple program for turning the LED off and on in a loop
def main() -> None:
    with SimpleGpio() as gpio:
        for _ in range(10):
            print('Turning on LED')
            gpio.turn_on_output(pin_number=DEFAULT_PIN)
            time.sleep(SLEEP_FOR)
            print('Turning off LED')
            gpio.turn_off_output(pin_number=DEFAULT_PIN)
            time.sleep(SLEEP_FOR)

if __name__ == '__main__':
    main()
