#!/usr/bin/python3
from typing import Dict, List, Tuple
import RPi.GPIO as GPIO

BUTTON_PIN = 35

def setup() -> None:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def register_button_push_input() -> None:
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        print("Button has been pushed\n")

def main() -> None:
    setup()
    while True:
        register_button_push_input()

if __name__ == '__main__':
    main()