from controller_py.start import PinConfiguration
from controller_py.gamepad_manager import GamepadController

pin_config = PinConfiguration("settings.json")
gp = GamepadController(pin_config.face_buttons, pin_config.joystick1_pins, pin_config.joystick2_pins)

gp.start()