from typing import Dict, List, Tuple, Optional, Union
import RPi.GPIO as GPIO


class GpioOutputChannel:

    def _setup_channel(self) -> None:
        GPIO.setup(self.number, GPIO.OUT, initial=self.initial_state)

    def __init__(self, 
                 number: int,
                 initial_state: int = GPIO.LOW
                 ) -> None:
        self.number = number
        self.initial_state = initial_state
        self._setup_channel()

    def turn_on(self) -> bool:
        GPIO.output(self.number, GPIO.HIGH)
        return True

    def turn_off(self) -> bool:
        GPIO.output(self.number, GPIO.LOW)
        return True

    def cleanup(self) -> bool:
        GPIO.cleanup(self.number)
        return True


class SimpleGpio:

    DEFAULT_MODE = GPIO.BOARD
    SET_WARNINGS = False

    def __init__(self,
                 gpio_mode: int = DEFAULT_MODE,
                 set_warnings: bool = SET_WARNINGS
                 ) -> None:
        self.gpio_mode = gpio_mode
        self.set_warnings = set_warnings
        self.channels = {}

    def __enter__(self) -> None:
        GPIO.setmode(self.gpio_mode)
        GPIO.setwarnings(self.set_warnings)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        channel_pins = [pin for pin in self.channels.keys()]
        GPIO.cleanup(channel_pins)

    def get_channel(self, pin_number: int) -> GpioOutputChannel:
        try:
            channel = self.channels[pin_number]
        except KeyError:
            channel = GpioOutputChannel(pin_number)
            self.channels[pin_number] = channel
        finally:
            return channel

    def turn_on_output(self, pin_number: int) -> bool:
        channel = self.get_channel(pin_number)
        result = channel.turn_on()
        return result

    def turn_off_output(self, pin_number: int) -> None:
        channel = self.get_channel(pin_number)
        result = channel.turn_off()
        return result