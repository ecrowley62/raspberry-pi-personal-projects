from typing import Dict, List, Tuple, Optional, Union
from venv import create
import RPi.GPIO as GPIO


class GpioOutputChannel:
    """ 
        Object represents a RPi.GPIO output channel. The output
        channel can be turned on/off but returns no data.

        Params
        ------
        number : int
            The board number for the pin used by this channel
        initial_state : int, optional
            The initial state the channel should be set to.
            Defaults to low (off)
    """

    def _setup_channel(self) -> None:
        """ Create a GCPIO output channel"""
        GPIO.setup(self.number, GPIO.OUT, initial=self.initial_state)

    def __init__(self, 
                 number: int,
                 initial_state: int = GPIO.LOW
                 ) -> None:
        self.number = number
        self.initial_state = initial_state
        self._setup_channel()

    def turn_on(self) -> bool:
        """ Send an on signal to the channel """
        GPIO.output(self.number, GPIO.HIGH)
        return True

    def turn_off(self) -> bool:
        """ Send an off signal to the channel """
        GPIO.output(self.number, GPIO.LOW)
        return True

    def cleanup(self) -> bool:
        """ Delete the channel from the current context """
        GPIO.cleanup(self.number)
        return True


class SimpleGpio:
    """
        Interface for doing basic GPIO interactios on the Raspberryi Pi.
        This interface as an abstraction allows us to do simple GPIO things
        easily. This includes things such as turning output channels on and
        off. The interface implements a context operation which will on exit
        automatically cleanup any in-use channels

        Params
        ------
        gpio_mode : int
            The mode to use when referencing pins on the GPIO
            interface of the Raspberry Pi
        set_warnings : bool
            Flag to indicate if warnings should be displayed 
            by GPIO

    """

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
        """ When entering the GPIO context set the GPIO mode"""
        GPIO.setmode(self.gpio_mode)
        GPIO.setwarnings(self.set_warnings)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """ Upon exiting the context, remove any channels that got created """
        channel_ids = [pin_num for pin_num in self.channels.keys()]
        GPIO.cleanup(channel_ids)

    def pin_is_in_use(self, pin_number: int) -> bool:
        """ 
            Check if this pin is already in use by a channel this
            interface created. TODO: Actually do a global check to
            see if RPi.GPIO is using this pin anywhere.
        """
        try:
            channel = self.channels[pin_number]
        except KeyError:
            return False
        else:
            return True

    def get_channel(self, 
                    pin_number: int,
                    create_if_not_exists: bool = True
                    ) -> GpioOutputChannel:
        """
            For the given pin number, return a channel object.
            If a channel object does not exist, and the applicable
            param is true, create the channel, else throw an error
        """
        if self.pin_is_in_use(pin_number):
            return self.channels[pin_number]
        else:
            if create_if_not_exists:
                new_channel = GpioOutputChannel(pin_number)
                return new_channel
            else:
                raise RuntimeError('Channel already exists!!')
        
    def turn_on_output(self, pin_number: int) -> bool:
        """ For the given pin, send a on signal to the channel """
        channel = self.get_channel(pin_number)
        result = channel.turn_on()
        return result

    def turn_off_output(self, pin_number: int) -> None:
        """ For the given pin, send a off signal to the channel """
        channel = self.get_channel(pin_number)
        result = channel.turn_off()
        return result