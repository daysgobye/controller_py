

import analogio
import digitalio
import usb_hid
from gamepad import Gamepad


class GamepadController:
    def __init__(self, button_pins: tuple, joystick1_pins: tuple, joystick2_pins: tuple,debug: bool = False) -> None:
        """
        This is the initialization function for a gamepad device that sets up button and joystick inputs.
        
        :param button_pins: A tuple containing the pins used for the buttons on the gamepad
        :type button_pins: tuple
        :param joystick1_pins: A tuple containing the pins for the first joystick's X and Y axes,
        respectively
        :type joystick1_pins: tuple
        :param joystick2_pins: The `joystick2_pins` parameter is a tuple containing two pins that are used
        to read the analog input values for the second joystick's x and y axes
        :type joystick2_pins: tuple
        :param debug: A boolean value indicating whether or not to enable debug mode. If set to True,
        additional debug information will be printed to the console, defaults to False
        :type debug: bool (optional)
        """
        self._gamepad_device = Gamepad(usb_hid.devices)
        self.buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
        for button in self.buttons:
            button.direction = digitalio.Direction.INPUT
            button.pull = digitalio.Pull.UP

        self.joystick1_x = analogio.AnalogIn(joystick1_pins[0])
        self.joystick1_y = analogio.AnalogIn(joystick1_pins[1])

        self.joystick2_x = analogio.AnalogIn(joystick2_pins[0])
        self.joystick2_y = analogio.AnalogIn(joystick2_pins[1])
        self.debug = debug


    def press_buttons(self, *button_numbers: int) -> None:
        for button_num in button_numbers:
            self._gamepad_device.press_buttons(button_num)

    def release_buttons(self, *button_numbers: int) -> None:
        for button_num in button_numbers:
            self._gamepad_device.release_buttons(button_num)

    def move_joysticks(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._gamepad_device.move_joysticks(x=x1, y=y1, z=x2, r_z=y2)

    def map_range(self, x: int, in_min: int, in_max: int, out_min: int, out_max: int) -> int:
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    def update(self) -> None:
        for i, button in enumerate(self.buttons):
            gamepad_button_num = i + 1
            if button.value:
                self.release_buttons(gamepad_button_num)
                if self.debug:
                    print(" release", gamepad_button_num, end="")
            else:
                self.press_buttons(gamepad_button_num)
                if self.debug:
                    print(" press", gamepad_button_num, end="")

        x1_value = self.map_range(self.joystick1_x.value, 0, 65535, -127, 127)
        y1_value = self.map_range(self.joystick1_y.value, 0, 65535, -127, 127)
        x2_value = self.map_range(self.joystick2_x.value, 0, 65535, -127, 127)
        y2_value = self.map_range(self.joystick2_y.value, 0, 65535, -127, 127)
        self.move_joysticks(x1=x1_value, y1=y1_value, x2=x2_value, y2=y2_value)

        if self.debug:
            print(" x1", self.joystick1_x.value, "y1", self.joystick1_y.value)
            print(" x2", self.joystick2_x.value, "y2", self.joystick2_y.value)

    def start(self):
        while True:
            self.update()



# Usage
# button_pins = (board.D2, board.D3, board.D4, board.D5)
# joystick1_pins = (board.A4, board.A5)
# joystick2_pins = (board.A6, board.A7)

# gp = GamepadController(button_pins, joystick1_pins, joystick2_pins)

# gp.start()