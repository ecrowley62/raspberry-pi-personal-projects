from time import sleep
import RPi.GPIO as GPIO

# Set GPIO to use the IO pin board numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
led_pin = 24 # GPIO 24, pin 18 (might need to ry with 18)
GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    print('Turning on LED')
    GPIO.output(led_pin, GPIO.HIGH)
    print('LED has been turned ON')
    sleep(2)
    print('Turning off LED')
    GPIO.output(led_pin, GPIO.LOW)
    print('Turned off LED')
    sleep(2)