#!/usr/bin/python
import time
import RPi.GPIO as GPIO

# Default sleep time
SLEEP_FOR = 0.3

# Default GPIO pin connected to the led
DEFAULT_PIN = 15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

def set_pin(pin_num=None):
    pn = pin_num if pin_num else DEFAULT_PIN
    GPIO.setup(pn, GPIO.OUT)
    return pn

def main():
    setup()
    active_pn = set_pin()

    # Flash the LED
    for _ in range(20):        
        GPIO.output(active_pn, GPIO.HIGH)
        time.sleep(SLEEP_FOR)
        GPIO.output(active_pn, GPIO.LOW)
        time.sleep(SLEEP_FOR)

    else:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
